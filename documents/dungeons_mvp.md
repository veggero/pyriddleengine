## start

You step on faulty stone, you loose your balance and you roll down
a small opening in the floor.

After a tachycardic long second of free fall you land on a pile of old branches and leafs.

> [Where am I?](#limbo)
> [try to go back](#no-way-back)


```
import time

if not gram.get("2"):
	print("creating gram")
	gram["2"] = {
		"code_submissions":{},
		"all_users":[],
		"waiting":[],
		"triples":{},
		"meetings": [{
			"code": "caress concur backed unneeded urban unripe",
			"code_hint": "parallel cities cookies",
			"recv_team_hint": "You are dressed as doppler effect and they walk like Zoiberg",
			"giving_team_hint": "They may look different if you move fast enough, They like anchovies",
			"time_hint": "When the sun set",
			"location_hint": "Garden"
		}]*20 # TESTMODE
	}

# TESTMODE
if not user.get("team"):
	user["team"] = {"id":len(gram["2"]["all_users"])}

if not user.get("2"):
	user["2"] = {"start_time": time.time()}

if not user["team"].get("2"):
	user["team"].update({
		"2": 1,
		"switches": {"0":0,"l":0,"2":0,"3":0},
		"attempts": {"0":[0], "1":[0],"2":[0],"3":[0],"4":[0]},
		"code_physical": "phy_secret",
		"hint_physical": "hidden under the shoes of Beri",
		"code_virtual": "virt_secret",
		"hint_virtual": "on this web page",
		"code_final": "final",
		"hint_final": "you are on it",
	})


if (tid:=user["team"]["id"]) not in gram["2"]["all_users"]:
	gram["2"]["all_users"].append(tid)

if (tid not in gram["2"]["waiting"]) and (tid not in gram["2"]["triples"].keys()):
	gram["2"]["waiting"].append(tid)

```


## check-info-torches

The light from the torch on the wall flickrs with a strange pattern,
some benevolent force is trying to comunicate with you ...

There are nr. `sum(user["team"]["switches"].values())` open gates.
There are nr. `len(gram["2"]["all_users"])` contestants in the dungeons.
There are nr. `len(gram["2"]["waiting"])` newcomers locked in dark rooms.

> [go back](`user["__previous"]`)

## limbo-help-success

The right stone stepped under your feet, the whole floor is shaking.

Part of the wall magically collapse on its onw immovability and a passage opens.

From a remote deep location your hear a familar sound, you are not sure if your heard your own eco
or if that was another voice...


> [There is no way back, let's go forward!](#node-1)


## limbo-help-fail

Dead silence ...

> [There must be someone coming down here at some point ...](#limbo)

## limbo-push

Nothing happens

## no-way-back-push

The walls are immovable huge blocks of stone, they cannot even be scratched

## no-way-back

The walls are slippery and flat.

There is no way back.

## limbo

You are trapped in a dark room

> [Try to push the walls](#limbo-push)
> [Try to call for help](#limbo-search-pairs)
> [There is something on the wall](#check-info-torches)


## limbo-search-pairs

The eco of your own voice are moning from all around.

You cannot tell if your voice is the only one.

> [Heeelloooo?! Is Anyboooody theeere?](#limbo-search-pairs)

```
# crate triples
id_a = user["team"]["id"]
if (id_a not in gram["2"]["triples"]) and len(w:=gram["2"]["waiting"]) > 2:
	#import random
	m_a = gram["2"]["meetings"].pop()
	m_b = gram["2"]["meetings"].pop()
	m_c = gram["2"]["meetings"].pop()

	# get id of companions
	id_a = w.pop(w.index(id_a))
	id_b = w.pop()
	id_c = w.pop()

	gram["2"]["triples"][id_a] = {
		"give": m_b,
		"give_id": id_b,
		"received": 0,
		"get": m_a,
		"get_id": id_c
	}
	gram["2"]["triples"][id_b] = {
		"give": m_c,
		"give_id": id_c,
		"received": 0,
		"get": m_b,
		"get_id": id_a
	}
	gram["2"]["triples"][id_c] = {
		"give": m_a,
		"give_id": id_a,
		"received": 0,
		"get": m_c,
		"get_id": id_b
	}

if id_a in gram["2"]["triples"].keys():
	user["__next_section"] = "limbo-help-success"
else:
	user["__next_section"] = "limbo-help-fail"
```

##  go-up

You are trying to see the maze from above.

`user["up_hatch_state"]`

<!-- > [Push the hatch above you](#final-question) -->

```
if all(user["team"]["switches"].values()):
	user["__next_section"] = "final-question"
	user["up_hatch_state"] = "The hatch seem alive and ready to shoot you outward, ... or inward"
else:
	user["up_hatch_state"] = "The hatch is seems locked, maybe some switches still need to be flipped"
	user["__next_section"] = user["__previous"]
```

## node-1
you are at a cross road, {{name_node_1}}

> [go right](#node-2)
> [go left](#node-3)
> [go back right](#node-4)
> [go back left](#node-4)
> [there is a switch](#door-0)
> [there is something written on the wall](#check-info-torches)
> ["jump"](#go-up)

## node-2
you are at a cross road, {{name_node_2}}

> [go right](#node-4)
> [go left](#node-4)
> [go back right](#node-1)
> [go back left](#node-3)
> [there is a switch](#door-1)
> [there is something written on the wall](#check-info-torches)
> ["jump"](#go-up)

## node-3
you are at a cross road, {{name_node_3}}

> [go right](#node-2)
> [go left](#node-2)
> [go back right](#node-1)
> [go back left](#node-4)
> [there is a switch](#door-2)
> [there is something written on the wall](#check-info-torches)
> ["jump"](#go-up)

## node-4
you are at a cross road, {{name_node_4}}

> [go right](#node-1)
> [go left](#node-3)
> [go back right](#node-2)
> [go back left](#node-2)
> [there is a switch](#door-2)
> [there is something written on the wall](#check-info-torches)
> ["jump"](#go-up)


## door-0
It's a `user["door-0-state"]` switch 🤔

> [open door](#ask-code)
> [close door](#deactivate-0)
> [go back](`user["__previous"]`)
```
user["door-0-state"] = "closed"
if user["team"]["switches"]["0"]: user["door-0-state"] = "open"
```
## door-1
It's a `user["door-1-state"]` switch 🤔

> [open door](#give-code)
> [close door](#deactivate-1)
> [go back](`user["__previous"])
```
user["door-1-state"] = "closed"
if user["team"]["switches"]["1"]: user["door-1-state"] = "open"
```
## door-2
It's a `user["door-2-state"]` switch 🤔

> [open door](#ask-virtual-code)
> [close door](#deactivate-2)
> [go back](`user["__previous"])

```
user["door-2-state"] = "closed"
if user["team"]["switches"]["2"]: user["door-2-state"] = "open"
```

## door-3
It's a `user["door-3-state"]` switch 🤔

> [open door](#ask-physical-code)
> [close door](#deactivate-3)
> [go back](`user["__previous"])

```
user["door-3-state"] = "closed"
if user["team"]["switches"]["3"]: user["door-3-state"] = "open"
```


## ask-code
The switch is asking for a secret code:

You have code had beeing given to previous prisoners find them and convince them to give you the key
You can recognize by the fact:  `gram["2"]["triples][user["team"]["id"]]["give"]["recv_team_hint"]`
you can find them at around this time:  `gram["2"]["triples][user["team"]["id"]]["give"]["time_hint"]`
where, maybe here:  `gram["2"]["triples][user["team"]["id"]]["give"]["location_hint"]`

> [I am not ready for this, I will go back](#door-0)

```
user["__parse_input"] = 1
user["__next_section"] = "parse-password-0"
```

## parse-password-0
The walls are shaking :O
> [aaaand?](#wrong-code-0)
```
user["team"]["attempts"]["0"].append(user["__message"])

team_id = user["team"]["id"]
pair_id = gram["2"]["triples"][team_id]["get_id"]
target_code = gram["2"]["triples"][team_id]["get"]["code"]

if user["__message"]==target_code:
	gram["2"]["triples"][team_id]["received"] = 1
	user["__next_section"] = "correct-code-0"
else:
	user["__next_section"] = "wrong-code-0"
```
## correct-code-0
Correct!
> [That was easy](#door-0)
> [It was just luck 😅](#door-0)
```
user["team"]["switches"]["0"] = 1
```
## wrong-code-0
Sorry the code:"`user["team"]["attempts"]["0"][-1]`" is not the right one
> [Wait, I will try again](#ask-code)
> [No clue, I will go back](#door-0)
## deactivate-0
The door is `user["door-0-state"]`
> [I want to close](#door-0)
```
user["door-0-state"] = "already closed"
if user["team"]["switches"]["0"]: user["door-0-state"] = "open"
user["team"]["switches"]["0"] = 0
```

## give-code
The switch is giving you a secret code

Thats is strange.

The code is: `gram["2"]["triples][user["team"]["id"]]["give"]["code"]`
you have to give to the team who is doing this:  `gram["2"]["triples][user["team"]["id"]]["give"]["recv_team_hint"]`
the location is:  `gram["2"]["triples][user["team"]["id"]]["give"]["time_hint"]`
the time is:  `gram["2"]["triples][user["team"]["id"]]["give"]["location_hint"]`

> [I delivered the code, did I?](#parse-password-1)
> [go back](#check-info-torches)

## parse-password-1
The walls are shaking :O
> [aaaand?](#wrong-code-1)
```
team_id = user["team"]["id"]
give_id = gram["2"]["triples"][team_id]["give_id"]

if gram["2"]["triples"][give_id]["received"]:
	user["__next_section"] = "correct-code-1"
else:
	user["__next_section"] = "wrong-code-1"
```
## correct-code-1
Correct!
> [That was easy](#door-1)
> [It was just luck 😅](#door-1)
```
user["team"]["switches"]["0"] = 1
```
## wrong-code-1
Sorry the code:"`user["team"]["attempts"]["0"][-1]`" is not the right one
> [Wait, I will try again](#give-code)
> [No clue, I will go back](#door-1)
## deactivate-1
The switch is `user["door_state"]`
> [I want to close](#door-1)
```
user["door-1-state"] = "already closed"
if user["team"]["switches"]["0"]: user["door-1-state"] = "open"
user["team"]["switches"]["0"] = 0
```

## ask-virtual-code
The switch is asking for a secret code:

This code must be found in the virtual world, here there is an hint for you: `user["team"]["hint_virtual"]`
Type the code now:


> [I am not ready for this, I will go back](#door-2)

```
user["__next_section"] = "parse-password-2"
```
## parse-password-2
The walls are shaking :O
> [aaaand?](#wrong-code-2)

```
user["team"]["attempts"]["2"].append(user["__message"])

team_id = user["team"]["id"]
pair_id = gram["2"]["triples"][team_id]["give_id"]

user["team"]["attempts"]["2"].append(user["__message"])
if user["__message"]==user["team"]["code_virtual"]: user["__next_section"] = "correct-code-2"
else: user["__next_section"] = "wrong-code-2"
```
## correct-code-2
Correct!
> [That was easy](#ask-virtual-code)
> [It was just luck 😅](#ask-virtual-code)
```
user["team"]["switches"]["2"] = 1
```
## wrong-code-2
Sorry the code:"`user["attempts"]["2"][-1]`" is not the right one
> [Wait, I will try again](#ask-virtual-code)
> [No clue, I will go back](#door-2)
## deactivate-2
The switch is `user["door-2-state"]`
> [I want to close](#door-2)
```
user["door-2-state"] = "already closed"
if user["switches"]["2"]: user["door-2-state"] = "open"
user["switch"] = 0
```
## ask-physical-code
The switch is asking for a secret code:

This code must be found in the virtual world, here there is an hint for you:
`user["team"]["hint_physical"]`

> [I am not ready for this, I will go back](`user["__previous"])

```
user["__next_section"] = "parse-password-3"
```

## parse-password-3
The walls are shaking :O
> [aaaand?](#wrong-code-3)
```
user["team"]["attempts"]["3"].append(user["__message"])

if user["__message"]==user["team"]["code_phyical"]: user["__next_section"] = "correct-code-3"
else: user["__next_section"] = "wrong-code-3"
```
## correct-code-3
Correct!
> [That was easy](#door-3)
> [It was just luck 😅](#door-3)
```
user["team"]["switches"]["3"] = 1
```
## wrong-code-3
Sorry the code:"`user["attempts"]["3"][-1]`" is not the right one
> [Wait, I will try again](#ask-physical-code)
> [No clue, I will go back](#node-1)
## deactivate-3
The switch is `user["door-3-state"]`
> [I want to close](#door-3)
```
user["door-3-state"] = "already closed"
if user["team"]["switches"]["3"]: user["door-3-state"] = "open"
user["team"]["switches"]["3"] = 0
```


## Final question
From above you have a glimpse of the structure of the maze,
it is enigmatic shape.

You go up further and you see it its entirity, it is a strange prespective.

You are far above it but still inside it, the magic power permeating this siniter location is too powerful.

The only way to defeat your cage is to say it's name

> [I will try!](#get-code-final)

## get-code-final
Do you really know the name of this prison?
```
user["__next_section"] = "parse-final"
```
## parse-final
The ceilings are shaking :O

> [aaaand?](#wrong-code-final)

```
print(user["__message"]))
user["team"]["attempts"]["4"].append(user["__message"])
if user["__message"]==user["team"]["code_final"]:
	user["__next_section"] = "correct-code-final"
else:
	user["__next_section"] = "wrong-code-final"
```
## correct-code-final
Correct! You are free!
> [Exit the dungeons](phase3.md#start)
> [It was just luck 😅](phase3.md#start)
## wrong-code-final
Sorry the code:'`user["team"]["attempts"]["4"][-1]`' is not the name of this cage
> [Wait, I will try again](#get-code-final)
> [No clue, I will go back](#node-1)
