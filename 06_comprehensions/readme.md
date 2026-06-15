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