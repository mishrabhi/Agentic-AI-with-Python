## Generators

A **generator** is a special type of function that produces values **one at a time, on demand** — instead of computing everything upfront and returning it all at once. Generators are memory-efficient and ideal for sequences that are large, infinite, or expensive to compute.

The key difference: a generator function uses **`yield`** instead of `return`.



### `yield` vs `return`

```python
# Regular function — computes all values, returns them at once
def get_chai_list():
    return ["Cup 1", "Cup 2", "Cup 3"]

# Generator function — produces one value at a time
def get_chai_gen():
    yield "Cup 1"
    yield "Cup 2"
    yield "Cup 3"
```

| | Regular Function | Generator Function |
|---|---|---|
| Keyword | `return` | `yield` |
| Returns | All values at once | One value at a time |
| Memory | Stores full result | Stores only current state |
| Reusable | Yes | Exhausted after one full pass |

When a generator function is called, it **doesn't execute immediately** — it returns a **generator object**. The body runs only when you request the next value.



### `next()` — Pulling Values One at a Time

Use the built-in `next()` function to manually advance a generator to its next `yield`.

```python
chai = get_chai_gen()

print(next(chai))   # Cup 1
print(next(chai))   # Cup 2
print(next(chai))   # Cup 3
# print(next(chai)) # StopIteration — generator is exhausted
```

Each call to `next()`:
1. Resumes the function from where it last paused (after the previous `yield`)
2. Runs until the next `yield` statement
3. Returns the yielded value and **pauses again**

> Calling `next()` after all values have been yielded raises a `StopIteration` exception. A `for` loop handles this automatically and stops cleanly.

### Iterating with a `for` Loop

```python
stall = serve_chai()
for cup in stall:
    print(cup)
```

This is the most common way — the `for` loop calls `next()` internally and stops when `StopIteration` is raised.



### Infinite Generators

Because generators produce values lazily, they can represent **sequences that never end** — something impossible with a regular list.

```python
def infinite_chai():
    count = 1
    while True:
        yield f"Refill #{count}"
        count += 1

refill = infinite_chai()

for _ in range(5):
    print(next(refill))
# Refill #1 ... Refill #5

for _ in range(2):
    print(next(refill))
# Refill #6, Refill #7  ← resumes from where it left off
```

Each generator object maintains its **own independent state**:

```python
user2 = infinite_chai()   # a completely separate generator, starts at Refill #1
```

> Never iterate over an infinite generator with a plain `for` loop — it will run forever. Always control how many values you pull using `range()`, a condition, or `itertools.islice()`.



### Sending Values into a Generator — `.send()`

Generators aren't just one-way — you can **send data back into a running generator** using `.send()`. The sent value becomes the result of the `yield` expression inside the generator.

```python
def chai_customer():
    print("Welcome! What chai would you like?")
    order = yield                  # pauses here; receives sent value
    while True:
        print(f"Preparing: {order}")
        order = yield              # pauses again; receives next sent value

stall = chai_customer()
next(stall)                        # must prime the generator first

stall.send("Masala Chai")          # Preparing: Masala Chai
stall.send("Lemon Chai")           # Preparing: Lemon Chai
```

**The priming step (`next()`) is mandatory.** A generator must run to its first `yield` before it can receive a value — calling `.send()` on an unstarted generator raises a `TypeError`.

| Method | What it does |
|---|---|
| `next(gen)` | Advances to the next `yield`; sent value is `None` |
| `gen.send(value)` | Advances to the next `yield`; the `yield` expression evaluates to `value` |

> Think of `yield` as a two-way door — it can **push a value out** (what the caller receives) and **receive a value in** (what `.send()` provides). Both can happen at the same `yield` point.



### How a Generator Remembers Its State

Unlike a regular function that starts fresh on every call, a generator **suspends** its entire execution frame — local variables, the current line, everything — between `yield` calls. This is what makes features like infinite sequences and stateful iteration possible.

```
Call next()  →  Generator resumes  →  Runs to next yield  →  Pauses  →  Returns value
```

