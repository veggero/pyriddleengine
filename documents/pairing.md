# Inside

Ok, I'm in.

```
if not "garden-users" in gram:
    gram["garden-users"] = 1
    gram["meetings"] = {}
    gram["unpaired"] = None
else:
    gram["garden-users"] += 1
```

> [Ok so? How's the castle?](#just-a-sec)

## Just A Sec

Wait a second! Actually, I wanted to talk to you about a thing, first.

> [Ehm, okay?](#alone)

> [Sure but... right now!?](#yeah)

### Yeah

Well, yeah, it's not like we're in a hurry anyway. I need to get this off my chest.

> [Shoot...](#alone)

## Alone

I feel alone.

> [But you've got me!](#you-got-me)

> [Oh! Why's that?](#why-is-that)

> [You kinda are](#you-are)

> [I'll find you someone](#find-you)

### You got me

I mean... I can't even see you. I'm out here, speaking english, and I barely understand what's going on around me. I feel terribly lost in this country.

> [You kinda are alone indeed](#you-are)

> [Anything I can do?](#what-can-i)

> [I can understand you...](#relatable)

### You Are

Yeah! Nobody to talk to... except you, obviously, but that barely counts. I'd like to be able to find someone else.

> [What can I do for you?](#what-can-i)

> [Relatable!](#relatable)

### Why is that

Well... I'm here, alone, not talking the native language, surrounded by Italians, barely understanding what's going on... let's just say, I've been through better times.

> [Anything I can do?](#what-can-i)

> [You know, I feel the same](#relatable)

> [You kinda are alone indeed](#you-are)

### What Can I

I'm not sure. Could I ask you to find me somebody to talk with?

> [Can we discuss this later on?](#later)

> [Uh... sure, ideas?](#ideas)

### Relatable

Ah, so you are in the same position as me? Well, actually, I have an idea that might be able to save us both.

> [Err, maybe not now?](#later)

> [Shoot!](#ideas)

### Find you

Right... actually, I have an idea that might make it easier for both of us.

> [What's that?](#ideas)

> [We can figure it out later tbh](#later)

### Later

HONESTLY NO. Like, I cannot survive any longer if I don't get to talk to somebody.

> [FINE!](#new-meeting)

### Ideas

Hear me out: I'm 100% sure that there are other people, like us, that are in contact with people from YOUR time.

My idea is to find a teammate in YOUR time, that's then going to have a linked person in MY time.

> [Err, okay](#new-meeting)

> [...Maybe later](#later)

### New Meeting

Let's go for it. I would say, I should probably be able to find somebody here and then tell you where to find its owner. But of course, to do that, I need to find some info about how to find YOU.

As an example, could you... bring or wear something recognizable? like, ...

> [A long plastic sword?](`user.update(appearance=message) or "#meeting-two"`)

> [A NSFW Star Wars t-shirt?](`user.update(appearance=message) or "#meeting-two"`)

> [Underwear on my head?](`user.update(appearance=message) or "#meeting-two"`)

> [Duct tape on my forehead?](`user.update(appearance=message) or "#meeting-two"`)

> [Three full cans of Pringles?](`user.update(appearance=message) or "#meeting-two"`)

> [A chessboard or two?](`user.update(appearance=message) or "#meeting-two"`)

> [An upside-down backpack?](`user.update(appearance=message) or "#meeting-two"`)

> [An inside-out Py t-shirt?](`user.update(appearance=message) or "#meeting-two"`)

> [A tic tac toe game drawn on my arm?](`user.update(appearance=message) or "#meeting-two"`)

> [A sign with "Python Sucks" on it?](`user.update(appearance=message) or "#meeting-two"`)

> [A sign with "I ♥ Marco Beri" on it?](`user.update(appearance=message) or "#meeting-two"`)

### Meeting Two

Err, I wasn't exactly thinking that, but whatever floats your boat! That's probably not specific enough, though. What about a secret phrase, so that when you think you met the right person, you can exchange your secret phrases and check that they're indeed correct?

Well, it's not necessary to actually make it a "secret" phrase, I guess that the more you say that phrase around, the easier it is to find the right person.

> ["Vim is clearly better than Nano"](`user.update(phrase=message) or "#meeting-three"`)

> ["Nobody would actually USE Windows"](`user.update(phrase=message) or "#meeting-three"`)

> ["GNOME is the best desktop!"](`user.update(phrase=message) or "#meeting-three"`)

> ["Tabs over spaces, anytime."](`user.update(phrase=message) or "#meeting-three"`)

> ["8 spaces to indent is better than 4"](`user.update(phrase=message) or "#meeting-three"`)

> ["There's no actual reason to use Rust"](`user.update(phrase=message) or "#meeting-three"`)

> ["Exiting Vim is actually pretty easy"](`user.update(phrase=message) or "#meeting-three"`)

> ["Dvorak is highly overrated"](`user.update(phrase=message) or "#meeting-three"`)

> ["Privacy is not actually that important"](`user.update(phrase=message) or "#meeting-three"`)

> ["PHP is not as bad as people put it"](`user.update(phrase=message) or "#meeting-three"`)

> ["Modern Javascript is a great tool"](`user.update(phrase=message) or "#meeting-three"`)

### Meeting Three

That should be enough. Let me see if I can find anybody.

...

...

...

```
proposal = {"id": user["id"], "appearance": user["appearance"][:-1], "phrase": user["phrase"]}
if gram["unpaired"]:
    user["teamid"] = str(user["id"]) + "&" + str(gram["unpaired"]["id"])
    user["__sync"] = [(user["teamid"], "team")]
    gram["meetings"][gram["unpaired"]["id"]] = (user["teamid"], proposal)
    user["paired"], user["other"] = True, gram["unpaired"]
    gram["unpaired"] = None
else:
    gram["unpaired"] = proposal
    user["paired"] = False
```

> [...and!?](`"#quickpaired" if user["paired"] else "#unpaired"`)

### QuickPaired

OOhh, I found somebody!

```
user["team"]["id"] = user["teamid"]
```

Ok ok, let me tell you how to recognize them. Or rather, their puppeteer.

Their special appearance is "`user["other"]["appearance"]`"

Their phrase is `user["other"]["phrase"]`

Go find them, now! Meanwhile, I'll go on with exploring the castle, now that I got in. You don't have to tell me when you find your new partner in crime, just make it sure to find them before getting to the next enigma, as it seems like some help there is necessary.

> [Gotcha](inside.md#garden)

### Unpaired

Err, nothing yet. Could you ping me again in, dunno, ten minutes? An hour? I'm not sure how much time I'll need until somebody else comes along.

```
if (not gram["unpaired"]) or (gram["unpaired"]["id"] != user["id"]):
    user["teamid"], user["other"] = gram["meetings"][str(user["id"])]
    user["__sync"] = [(user["teamid"], "team")]
    user["paired"] = True
```

> [I'm waiting.](`"#quickpaired" if user["paired"] else "#unpaired"`)
