## Loops

Loops let you repeat a block of code — either over a sequence of items (`for`) or as long as a condition holds (`while`).

---

### `for` Loop with `range()`

Use `range()` to loop a specific number of times. It generates a sequence of numbers you can iterate over.

```python
# Tokens 1 to 10
for token in range(1, 11):
    print(f"Serving chai to Token #{token}")

# 4 batches (1 to 4)
for batch in range(1, 5):
    print(f"Preparing chai for batch #{batch}")
```

**`range()` syntax:** `range(start, stop, step)`
- `start` — where to begin (inclusive, default `0`)
- `stop` — where to end (**exclusive**)
- `step` — increment between values (default `1`)

| Call | Produces |
|---|---|
| `range(5)` | `0, 1, 2, 3, 4` |
| `range(1, 5)` | `1, 2, 3, 4` |
| `range(0, 10, 2)` | `0, 2, 4, 6, 8` |

---

### `for` Loop over a List

You can iterate directly over any list — no index needed.

```python
orders = ['abhishek', 'aman', 'hitesh', 'shubham']

for name in orders:
    print(f"Order ready for #{name}")
```

---

### `enumerate()` — Loop with Index

When you need both the position and the value, use `enumerate()`. The optional `start` argument sets the starting index.

```python
menu = ['green tea', 'lemon tea', 'spiced tea', 'mint tea']

for idx, item in enumerate(menu, start=1):
    print(f"{idx} : {item}")
```

Output:
```
1 : green tea
2 : lemon tea
3 : spiced tea
4 : mint tea
```

> Without `start=1`, indexing begins at `0` by default.

---

### `zip()` — Loop over Two Lists Together

`zip()` pairs up elements from two (or more) lists and iterates over them in parallel.

```python
names = ["Abhishek", "Meera", "Rinki"]
bills = [50, 100, 70]

for name, amount in zip(names, bills):
    print(f"{name} paid ₹{amount}")
```

> `zip()` stops at the **shortest** list. If the lists are unequal in length, extra items in the longer one are ignored.

---

### `while` Loop

A `while` loop keeps running as long as its condition is `True`. Use it when you don't know the number of iterations in advance.

```python
temperature = 40

while temperature < 100:
    print(f"Current temperature: {temperature}°C")
    temperature += 15

print("Tea is ready to boil!")
```

Output:
```
Current temperature: 40°C
Current temperature: 55°C
Current temperature: 70°C
Current temperature: 85°C
Tea is ready to boil!
```

> Always make sure the condition will eventually become `False` — otherwise you get an **infinite loop**.

---

### `break` and `continue` — Loop Control

These keywords let you fine-tune loop behaviour mid-iteration.

```python
flavours = ['ginger', 'out of stock', 'lemon', 'discontinued', 'tulsi']

for flavour in flavours:
    if flavour == 'out of stock':
        continue        # skip this item, move to next
    if flavour == 'discontinued':
        break           # stop the loop entirely
    print(f"{flavour} item found!")

print("Outside of loop")
```

Output:
```
ginger item found!
lemon item found!
Outside of loop
```

| Keyword | Effect |
|---|---|
| `continue` | Skips the **rest of the current iteration** and moves to the next |
| `break` | **Exits the loop entirely**, regardless of remaining items |

> Code after the loop (outside the `for`/`while` block) always runs — even after a `break`.

---

## 🦦 Walrus Operator `:=`

Introduced in **Python 3.8**, the walrus operator (`:=`) lets you **assign and evaluate** a value in the same expression. It's useful for avoiding redundant calculations or extra lines.

**Syntax:** `variable := expression`

### In an `if` Statement

```python
# Without walrus
value = 13
remainder = value % 5
if remainder:
    print(f"Not divisible, remainder is {remainder}")

# With walrus — assign and check in one line
if (remainder := value % 5):
    print(f"Not divisible, remainder is {remainder}")
```

### In an `if` with `input()`

Capture user input and check it in a single expression:

```python
available_sizes = ["small", "medium", "large"]

if (requested_size := input("Enter your chai cup size: ")) in available_sizes:
    print(f"Serving {requested_size} chai")
else:
    print(f"Size unavailable - {requested_size}")
```

Without `:=`, you'd need two lines: one to capture input and one to check it. The walrus operator merges them cleanly.

### In a `while` Loop

The most common use case — keep looping until valid input is received:

```python
flavors = ["masala", "ginger", "lemon", "mint"]
print(f"Available flavors: {flavors}")

while (flavor := input("Choose your flavor: ")) not in flavors:
    print(f"Sorry, {flavor} is not available")

print(f"Your chosen flavor: {flavor} chai")
```

This assigns the user's input to `flavor` **and** checks it against `flavors` in the same line — no need to call `input()` twice.

---

### Quick Reference

| Tool | Best Used When |
|---|---|
| `for` + `range()` | Looping a fixed number of times |
| `for` over list | Iterating over every item in a sequence |
| `enumerate()` | You need both the index and the value |
| `zip()` | Iterating over two lists in parallel |
| `while` | Repeating until a condition changes |
| `break` | Exiting a loop early on a condition |
| `continue` | Skipping specific iterations |
| Walrus `:=` | Assigning and testing a value in one expression |