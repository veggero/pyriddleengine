# Tests

Tests.

First is about code in links.

Second is about custom user input.

Third is about sub-user syncing.

> [First](#first)

> [Second](#second)

> [Third](#third)

# First

Okay, first test, all buttons should bring you to the first section.

```
print("I should see this")
user["sect"] = "#one"
gram
```

> [Button zero](#one)

> [Button one](`"#one"`)

> [Button two](`user["sect"]`)

> [Done](#tests)

## One

This is section one!

> [Get back](#first)

> [Get back but complex](`user["__previous"]`)

# Second

Okay, try writing something that's not "apple" and then "apple"

> [Done](#tests)

> `"#incorrect" if message != "apple" else "#correct"`

## Incorrect

Not apple. Try again

> [Get back](`user["__previous"]`)

## Correct

Yeah, this was apple.

> [Get back](`user["__previous"]`)

# Third

```
gram["test"] = True
user["__sync"] = [('global', 'whops'), ('test123', 'yaya')]
```

Ok, I've set up the sync now.

> [Let's test it then](#test-sync)

### Test sync

Okay, so, the interesting stuff is in theory in `str(user["whops"])`. Check in the files too. I've set some properties.

```
user["whops"]["test-a"] = True
user["yaya"]["test-b"] = True
```

> [Done?](#tests)


