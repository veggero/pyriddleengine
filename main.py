from telegram.ext import Updater, MessageHandler, CommandHandler, Filters
from telegram import Bot, ReplyKeyboardMarkup, ReplyKeyboardRemove
from dataclasses import dataclass, field
import os, os.path, time, logging, json, sys
from collections import Counter, defaultdict
import random, datetime, pickle

TOKEN = ""
with open("./.BOT_TOKEN", 'r') as ff:
    TOKEN = ff.read().strip()

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%H:%M:%S', level=logging.INFO)

@dataclass
class Stats:
    path: str

    def __post_init__(self):
        if not os.path.isfile(f'.{self.path}.pickle'):
            self.times = defaultdict(int)
            self.users = defaultdict(set)
            self.stuck = []
        else:
            self.times, self.users, self.stuck = pickle.load(open(f'.{self.path}.pickle', 'rb'))

    def usernum(self, day, hour):
        return len(self.users[(day, hour)])

    def ping(self, userid):
        now = datetime.datetime.now()
        self.times[(now.day, now.hour)] += 1
        self.users[(now.day, now.hour)].add(userid)
        self.save()

    def save(self):
        pickle.dump((self.times, self.users, self.stuck), open(f'.{self.path}.pickle', 'wb'))

    def update(self):
        with open(self.path+'.md', 'w') as file:
            # Timetable
            print('**Timetable**:\n', file=file)
            for sections in (range(8), range(8, 16), range(16, 24)):
                print('| |', file=file, end='')
                for hour in sections: print(f'{hour}:00', '|', file=file, end='')
                print('', file=file)
                print('| --- |', file=file, end='')
                for hour in sections: print('----', '|', file=file, end='')
                print('', file=file)
                for day in {3, 4, 5}:
                    print(f'| {day} June', '|', end='', file=file)
                    for hour in sections:
                        print(self.times[(day, hour)], '/', self.usernum(day, hour), '|', file=file, end='')
                    print('', file=file)
                print('\n', file=file)

            # Users
            users = [json.load(open('data/'+name)) for name in os.listdir('data/')
                    if name.endswith('.json')]
            filenames = set(user.get('__filename') for user in users)
            for filename in filter(bool, filenames):
                print(f'**{filename}**:', file=file)
                print('', file=file)
                print('| section | users |', file=file)
                print('| ------- | ----- |', file=file)
                places = Counter([s for user in users if (s:=user.get('__section'))
                                  and user.get('__filename') == filename])
                for key, value in places.items():
                    print('|', key.ljust(max(map(len, places))), '|', value, '|',file=file)
                print('', file=file)
            print('\nStuck users:', str(self.stuck), file=file)


@dataclass
class DataFolder:
    path: str
    start: str

    def __post_init__(self):
        self.mdfiles = [MdFile(self.path, name) for name in os.listdir(self.path)
                        if name.endswith('.md')]
        assert self.start in [m.filename for m in self.mdfiles]
        logging.info("Running static links check")
        self.links_check()

    def fetch(self, filename, sectionname, defaultmd=None):
        logging.debug(f"Currently fetching {filename}#{sectionname}")
        try: return next((m for m in self.mdfiles if m.filename == filename),
                    defaultmd).section_named(sectionname)
        except StopIteration:
            logging.error(f"Could not find linked section {filename}#{sectionname}")

    def links_check(self):
        for mdfile in self.mdfiles: mdfile.links_check(self)

    @property
    def starting_md(self): return next(m for m in self.mdfiles if m.filename == self.start)

@dataclass
class UserDict:
    user_id: str = ''

    def __post_init__(self):
        self.filename, self.data, self.sync = f'data/{self.user_id or "global"}.json', {}, {}
        if not os.path.isfile(self.filename):
            self.data = {"id": self.user_id, "start_time": time.time()}
            open(self.filename, 'w').write(json.dumps(self.data))
        else: self.data = json.load(open(self.filename))
        for (filename, name) in self.data.get('__sync', ()):
            self.sync[name] = UserDict(filename)
            self.data[name] = self.sync[name].data


    def set_section(self, sectionname, filename):
        self.data.update({'__section': sectionname, '__filename': filename,
                          '__previous': '#'+self.data.get('__section', '')})

    def get_section(self, message, datafolder, user):
        if '__section' not in self.data: return datafolder.starting_md.starting_section
        current = datafolder.fetch(self.data['__filename'], self.data['__section'])
        if not message in (l := current.links) and '*' not in l: return None
        link = l[message] if message in l else l['*']
        return datafolder.fetch(*link.enter(user, message), current.parent)

    def save(self):
        json.dump(self.data, open(self.filename, 'w'))
        for sub in self.sync.values(): sub.save()

@dataclass
class SafeLink:
    filename: str
    section: str

    def enter(self, user, m=None): return self.filename, self.section

@dataclass
class CodeLink:
    code: str

    def enter(self, user, m=None):
        result = eval(self.code.replace('`', ''),
                      {'user': user.data, 'gram': gram.data, 'message': m})
        filen, _, section = result.partition('#')
        return filen.strip(), section.strip()

@dataclass
class Section:
    name: str
    messages: list[str, ...]
    links: dict[str, SafeLink | CodeLink]
    code: str
    parent: 'MdFile'

    def enter(self, bot, user, gram):
        user.set_section(self.name, self.parent.filename)
        exec(self.code, {'user': user.data, 'gram': gram.data})
        messages = list(filter(len, self.messages))
        for i, message in enumerate(messages):
            time.sleep(2)
            kb = self.keyboard if i==len(messages)-1 else ReplyKeyboardRemove()
            bot.send_message(user.user_id, self.eval_message(message, user, gram),
                             'Markdown', reply_markup=kb)
        gram.save(), user.save()
        if not self.links and (next_section := self.parent.section_after(self)):
            next_section.enter(bot, user, gram)

    def links_check(self, datafolder):
        for link in self.links.values():
            if isinstance(link, SafeLink):
                datafolder.fetch(*link.enter(None), self.parent)

    @property
    def keyboard(self):
        return ReplyKeyboardMarkup([[a] for a in self.links if a!='*']) if self.links else None

    @staticmethod
    def eval_message(message, user, gram):
        while '`' in message:
            before, _, partial = message.partition('`')
            code, _, after = partial.partition('`')
            message = before + str(eval(code, {'gram': gram.data, 'user': user.data})) + after
        return message

@dataclass
class MdFile:
    path: str
    filename: str

    def __post_init__(self):
        md = open(os.path.join(self.path, self.filename)).read()
        while '<!--' in md: md = md[:md.index('<!--')] + md[md.index('-->')+3:]
        md, self.sections = md.strip().split('\n'), []
        while md: self.sections.append(self.parse_section(md, self))

    @property
    def starting_section(self): return self.sections[0]

    def links_check(self, datafolder):
        for section in self.sections: section.links_check(datafolder)

    def section_named(self, name):
        return next(s for s in self.sections if s.name == name)

    def section_after(self, section):
        return next((b for a, b in zip(self.sections, self.sections[1:])
                    if a.name == section.name), None)

    @staticmethod
    def parse_section(md, parent):
        name = md.pop(0).replace('#', '').strip().replace(' ', '-').lower()
        messages, links, code = [''], {}, ''
        while md:
            if (l := md.pop(0).strip()).startswith('>'):
                l = l.replace('>', '').strip()
                if l.startswith('`'):
                    links['*'] = CodeLink(l)
                else:
                    l = l[1:-1]
                    message, _, link = l.partition('](')
                    if link.startswith('`'): links[message.strip()] = CodeLink(link)
                    else:
                        link_file, _, link_section = link.partition('#')
                        links[message.strip()] = SafeLink(link_file.strip(), link_section.strip())
            elif l.startswith('```'):
                assert l == '```'
                while not (l := md.pop(0)).endswith('```'): code += l + '\n'
            elif l == '' and messages[-1] != '': messages.append('')
            elif l.startswith('#'):
                md.insert(0, l)
                break
            elif l: messages[-1] += l + '\n'
        return Section(name, messages, links, code, parent)

updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

gram = UserDict()
docs = DataFolder('documents/', sys.argv[1]+'.md' if len(sys.argv) == 2 else 'main.md')

def reply(update, context):
    logging.info(f'Received «{update.message.text}» from {update.effective_chat.id}')
    stats.ping(update.effective_chat.id)
    user = UserDict(update.effective_chat.id)
    stats.stuck.append(user.user_id), stats.save()
    section = user.get_section(update.message.text, docs, user)
    if not section: context.bot.send_message(user.user_id, "I'm sorry, I didn't get that")
    else: section.enter(context.bot, user, gram)
    gram.save(), user.save()
    stats.stuck.remove(user.user_id), stats.update(), stats.save()

def purge(update, context):
    logging.warning(f'Received purge request from {update.effective_chat.id}')
    user = UserDict(update.effective_chat.id)
    user.data = {"id":update.effective_chat.id,"start_time":time.time()}
    user.save()
    docs.starting_md.starting_section.enter(context.bot, user, gram)

stats = Stats('stats')
stats.update()

echo_handler = MessageHandler(Filters.text & (~Filters.command), reply)
purge_handler = CommandHandler('purge', purge)
dispatcher.add_handler(echo_handler)
dispatcher.add_handler(purge_handler)
updater.start_polling()
