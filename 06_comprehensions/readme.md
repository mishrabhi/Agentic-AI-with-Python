##  Comprehensions

**Comprehensions** offer a concise way to create collections (lists, sets, dicts, etc.) by transforming and/or filtering an iterable — all in a single readable line, instead of writing a `for` loop with `.append()`.

---

### List Comprehension

**Syntax:** `[expression for item in iterable if condition]`

```python
menu = [
    "Masala Chai",
    "Iced Lemon Tea",
    "Green Tea",
    "Iced Peach Tea",
    "Ginger Chai"
]

iced_tea = [tea for tea in menu if "Iced" in tea]
print(iced_tea)
```

Output:
```
['Iced Lemon Tea', 'Iced Peach Tea']
```

This is equivalent to the traditional loop:

```python
iced_tea = []
for tea in menu:
    if "Iced" in tea:
        iced_tea.append(tea)
```

| Part | Role |
|---|---|
| `tea` (expression) | What gets added to the new list — can be `tea`, `tea.upper()`, etc. |
| `for tea in menu` | Iterates over each item |
| `if "Iced" in tea` | Optional filter — only items satisfying this are included |

> The result is always a **new list**. The original `menu` is unchanged.

---

### Set Comprehension

**Syntax:** `{expression for item in iterable if condition}`

Same idea as a list comprehension, but produces a **set** — so duplicates are automatically removed and order is not guaranteed.

#### Basic Set Comprehension with Filtering

```python
favourite_chais = [
    "Masala Chai",
    "Green tea",
    "Masala chai",
    "Lemon tea",
    "Green Tea",
    "Elaichi tea"
]

unique_chai = {chai for chai in favourite_chais if len(chai) < 8}
print(unique_chai)
```

Output (order may vary):
```
{'Green tea', 'Lemon tea', 'Green Tea'}
```

> Note: `"Masala Chai"` and `"Masala chai"` are both excluded since their length (`11`) is not `< 8`. Also note that `"Green tea"` and `"Green Tea"` are treated as **different strings** (case-sensitive) — both pass the filter and both appear since sets only remove *exact* duplicates.

#### Nested Iteration in a Comprehension

Comprehensions can loop over **nested structures** — here, over each list of ingredients inside a dictionary's values.

```python
recipes = {
    "Masala Chai": ["ginger", "cardamom", "clove"],
    "Elaichi Chai": ["cardamom", "milk"],
    "Spicy Chai": ["ginger", "black pepper", "clove"]
}

unique_spices = {spice for ingredients in recipes.values() for spice in ingredients}
print(unique_spices)
```

Output (order may vary):
```
{'ginger', 'cardamom', 'clove', 'milk', 'black pepper'}
```

This is equivalent to:

```python
unique_spices = set()
for ingredients in recipes.values():
    for spice in ingredients:
        unique_spices.add(spice)
```

> In a comprehension, multiple `for` clauses are read **left to right**, just like nested loops — the leftmost `for` is the outer loop.

---

### List vs Set Comprehension

| | List Comprehension | Set Comprehension |
|---|---|---|
| **Brackets** | `[ ]` | `{ }` |
| **Result** | Ordered, allows duplicates | Unordered, unique elements only |
| **Use when** | Order matters / duplicates are meaningful | You need uniqueness automatically |

---

## Dictionary Comprehension

**Syntax:** `{key_expression: value_expression for item in iterable if condition}`

Same idea as list/set comprehensions, but produces a **dictionary** — the expression is a `key: value` pair instead of a single value.

```python
tea_prices_inr = {
    "Masala chai": 40,
    "Green tea":   50,
    "Lemon tea":   200
}

tea_prices_usd = {tea: price / 80 for tea, price in tea_prices_inr.items()}
print(tea_prices_usd)
```

Output:
```
{'Masala chai': 0.5, 'Green tea': 0.625, 'Lemon tea': 2.5}
```

Breaking it down:

- `tea_prices_inr.items()` yields each `(key, value)` pair — unpacked as `tea, price`
- `tea: price / 80` is the `key: value` expression that builds each entry in the new dictionary
- The result is a **brand new dictionary**; the original `tea_prices_inr` is unchanged

Equivalent traditional loop:

```python
tea_prices_usd = {}
for tea, price in tea_prices_inr.items():
    tea_prices_usd[tea] = price / 80
```

> Dictionary comprehensions are especially useful for **transforming values** (like unit conversions), **renaming keys**, or **filtering out entries** — all without mutating the original.

---

## Generator Comprehension (Generator Expression)

**Syntax:** `(expression for item in iterable if condition)`

A generator comprehension looks like a list comprehension but uses **parentheses** `()` instead of brackets `[]`. The key difference: it produces a **generator object** — a lazy iterator that computes values **one at a time on demand**, rather than building the entire collection in memory upfront.

```python
daily_sales = [5, 10, 12, 8, 15, 4]

total_cups = sum(sale for sale in daily_sales if sale > 5)
print(total_cups)   # 45
```

Here, `sum()` consumes the generator one value at a time — `10`, `12`, `8`, `15` — without ever creating an intermediate list.

Equivalent list comprehension:

```python
total_cups = sum([sale for sale in daily_sales if sale > 5])
```

Both produce the same result (`45`), but the generator version is more **memory-efficient** — it never holds all the filtered values in memory at once.

> Generators are especially valuable when working with **large datasets** — processing a million sales records with a generator uses a constant, small amount of memory, whereas a list comprehension would load all million values into memory first.

---

## All Four Comprehensions — Side by Side

| Type | Syntax | Result | Ordered | Unique |
|---|---|---|---|---|
| List | `[expr for x in it]` | `list` | Yes | No |
| Set | `{expr for x in it}` | `set` | No | Yes |
| Dictionary | `{k: v for x in it}` | `dict` | Yes (3.7+) | Keys unique |
| Generator | `(expr for x in it)` | `generator` | Yes (lazy) | No |

### When to Use Which

- **List** — when you need an ordered, indexable collection with duplicates allowed
- **Set** — when you need uniqueness and don't care about order
- **Dictionary** — when you need key-value pairs, typically transforming an existing dict
- **Generator** — when passing results directly into a function (`sum`, `max`, `any`, etc.) or when working with large data and memory efficiency matters