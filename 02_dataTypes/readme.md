# Data Types and Mutability

This section explores Python's built-in data types and the concept of mutability, which is fundamental to understanding how Python manages data in memory.

## Everything is an Object

In Python, everything is an object. Each object has three key properties:

* **Identity**: A unique identifier (memory address)
* **Type**: The object's type (`int`, `str`, `list`, etc.)
* **Value**: The actual data stored

You can inspect these properties using built-in functions:

```python
x = 42

print(id(x))    # Identity
print(type(x))  # Type
print(x)        # Value
```

## Mutability

### Mutable vs Immutable

* **Mutable**: Objects whose value can be changed after creation.
* **Immutable**: Objects whose value cannot be changed after creation.

An object's identity determines whether modifications occur in place. When you "change" an immutable object, Python creates a new object with a new identity.

## Immutable Objects

Numbers, strings, and tuples are immutable.

### Example

```python
# Numbers are immutable

sugar_amount = 30
print(f"Initial value: {sugar_amount}, ID: {id(sugar_amount)}")

sugar_amount = 50  # Creates a new object
print(f"New value: {sugar_amount}, ID: {id(sugar_amount)}")
```

### Common Immutable Types

* `int`
* `float`
* `bool`
* `str`
* `tuple`

## Mutable Objects

Lists, dictionaries, and sets are mutable.

### Example

```python
# Sets are mutable

spice_mix = set()

print(f"Initial ID: {id(spice_mix)}")
print(f"Initial set: {spice_mix}")

spice_mix.add("ginger")
spice_mix.add("cardamom")

print(f"After changes ID: {id(spice_mix)}")  # Same ID
print(f"Modified set: {spice_mix}")
```

### Common Mutable Types

* `list`
* `dict`
* `set`
* `bytearray`

## Key Takeaway

* Immutable objects cannot be modified after creation; any apparent modification creates a new object.
* Mutable objects can be modified in place while retaining the same identity.
* Understanding mutability helps prevent unexpected behavior and improves memory management in Python programs.

# Numeric Types

Python supports several numeric types, all of which are immutable.

## Integers (int)

Whole numbers without decimal points. In Python 3, integers can be arbitrarily large.

### Key Points:

- Unlimited precision (no overflow like in C/Java)
- Efficient storage for small integers (-5 to 256 are interned)
- Support for binary, octal, hexadecimal literals

```python
# Basic arithmetic
black_tea_grams = 14
ginger_grams = 5
total_grams = black_tea_grams + ginger_grams
print(f"Total grams: {total_grams}")

# Remainder and exponentiation
remainder = 10 % 3
result = 5 ** 3
print(f"Remainder: {remainder}, 5^3: {result}")

# Large numbers with underscores for readability
bignumber = 1_000_000_000
```

## Floating-Point Numbers (float)

Double-precision floating-point numbers (IEEE 754 standard).

### Key Points:

- Limited precision (about 15 decimal digits)
- Represented as float type
- Special values: inf, -inf, nan
- Use decimal.Decimal for financial calculations requiring exact decimal representation

```python
milk_liters = 7
servings = 4
milk_per_serving = milk_liters / servings
print(f"Milk per serving: {milk_per_serving} liters")

price_per_kg = 2.5
weight_kg = 3.2
total_cost = price_per_kg * weight_kg
print(f"Total cost: ${total_cost:.2f}")
```

## Strings

A **string** is a sequence of characters enclosed in single or double quotes. Python strings are **immutable** — once created, their content cannot be changed.

```python
chai_type = "Ginger Chai"
customer_name = "Priya"
print(f"Order for {customer_name}: {chai_type} please!")
# Output: Order for Priya: Ginger Chai please!
```

### String Slicing

Strings support slicing using the syntax `string[start:stop:step]`.

```python
chai_discription = "Aromatic and Bold"

print(chai_discription[0:8])    # "Aromatic"  → characters from index 0 to 7
print(chai_discription[0:8:1])  # "Aromatic"  → same, step=1 (default)
print(chai_discription[:8])     # "Aromatic"  → start defaults to 0
print(chai_discription[12:])    # "Bold"       → from index 12 to end
print(chai_discription[::-1])   # "dloB dna citamorA" → reverses the string
```

| Syntax | Meaning |
|---|---|
| `s[a:b]` | Characters from index `a` up to (not including) `b` |
| `s[:b]` | From the beginning up to index `b` |
| `s[a:]` | From index `a` to the end |
| `s[::-1]` | Reverse the entire string |

> **Note:** String indices start at `0`. Negative step (`-1`) reverses direction.

---

## 📦 Tuples

A **tuple** is an ordered collection of items enclosed in parentheses `()`. Unlike lists, tuples are **immutable** — their elements cannot be added, removed, or changed after creation.

```python
masala_spices = ("cardamom", "cloves", "cinnamon")
```

### Unpacking

Tuple elements can be unpacked directly into individual variables:

```python
(spice1, spice2, spice3) = masala_spices
print(f"Main masala spices: {spice1}, {spice2}, {spice3}")
# Output: Main masala spices: cardamom, cloves, cinnamon
```

### Variable Swapping

Python allows swapping variable values in a single line using tuple-style assignment — no temporary variable needed:

```python
ginger_ratio, cardamom_ratio = 2, 1
print(f"ginger ratio is: {ginger_ratio}, cardamom ratio is: {cardamom_ratio}")
# Output: ginger ratio is: 2, cardamom ratio is: 1

ginger_ratio, cardamom_ratio = cardamom_ratio, ginger_ratio
print(f"ginger ratio is: {ginger_ratio}, cardamom ratio is: {cardamom_ratio}")
# Output: ginger ratio is: 1, cardamom ratio is: 2
```

### Membership Testing

Use the `in` keyword to check if a value exists in a tuple:

```python
print("ginger" in masala_spices)    # False
print("cinnamon" in masala_spices)  # True
```

### Key Properties of Tuples

| Property | Description |
|---|---|
| **Ordered** | Elements maintain their insertion order |
| **Immutable** | Cannot be modified after creation |
| **Allows Duplicates** | Same value can appear multiple times |
| **Indexed** | Access elements via `tuple[index]` |

> **When to use a Tuple vs a List?** Use a tuple when the data should not change (e.g., coordinates, config values, days of the week). Use a list when you need a mutable, dynamic collection.

## Lists

A **list** is an ordered, **mutable** collection of items enclosed in square brackets `[]`. Unlike tuples, lists can be freely modified — elements can be added, removed, or rearranged after creation.

```python
ingredients = ['water', 'milk', 'black tea']
```

### Common List Methods

#### Adding Elements

```python
ingredients.append('sugar')
# ['water', 'milk', 'black tea', 'sugar'] → adds to the end

chai_ingredients.insert(2, "black tea")
# Inserts "black tea" at index 2, shifting other elements right

chai_ingredients.extend(spice_options)
# Merges another list into the end of chai_ingredients (modifies in place)
```

| Method | Description |
|---|---|
| `.append(item)` | Adds a single item to the **end** |
| `.insert(index, item)` | Inserts an item at a specific **index** |
| `.extend(iterable)` | Appends **all items** from another list/iterable |

#### Removing Elements

```python
ingredients.remove('water')
# Removes the first occurrence of 'water'

last_added = chai_ingredients.pop()
# Removes and returns the last element
```

| Method | Description |
|---|---|
| `.remove(item)` | Removes the **first occurrence** of the given value |
| `.pop()` | Removes and **returns** the last item (or item at given index) |

#### Reordering

```python
chai_ingredients.reverse()   # Reverses the list in place
chai_ingredients.sort()      # Sorts the list in place (ascending by default)
```

> **Note:** Both `.reverse()` and `.sort()` modify the list **in place** and return `None`.

#### Aggregations

```python
sugar_levels = [1, 2, 3, 4, 5]
print(max(sugar_levels))   # 5
print(min(sugar_levels))   # 1
```

---

### Operator Overloading with Lists

Python's `+` and `*` operators work on lists with intuitive behaviour:

```python
# + concatenates two lists into a new list
base_liquid = ['water', 'milk']
extra_flavour = ['ginger']
full_liquid_mix = base_liquid + extra_flavour
# ['water', 'milk', 'ginger']

# * repeats the list n times
strong_brew = ['black tea'] * 3
# ['black tea', 'black tea', 'black tea']

strong_brew = ['black tea', 'water'] * 3
# ['black tea', 'water', 'black tea', 'water', 'black tea', 'water']
```

| Operator | Behaviour |
|---|---|
| `list1 + list2` | Returns a **new** combined list |
| `list * n` | Returns a **new** list with elements repeated `n` times |

> **Key difference from `.extend()`:** The `+` operator creates a **new list** and does not modify either original. `.extend()` modifies the list in place.

---

## Sets

A **set** is an **unordered** collection of **unique** items enclosed in curly braces `{}`. Sets automatically eliminate duplicates and are optimised for membership testing and mathematical set operations.

```python
essential_spices = {'cardamom', 'ginger', 'cloves'}
optional_spice   = {'cinnamon', 'ginger', 'black pepper'}
```

> **Note:** Since sets are unordered, the printed output may appear in a different order each time.

### Set Operations

Python sets support standard mathematical set operations using operators:

```python
all_spices = essential_spices | optional_spice
# Union → all unique items from both sets
# {'cardamom', 'ginger', 'cloves', 'cinnamon', 'black pepper'}

common_spices = essential_spices & optional_spice
# Intersection → only items present in BOTH sets
# {'ginger'}

only_in_essential = essential_spices - optional_spice
# Difference → items in essential that are NOT in optional
# {'cardamom', 'cloves'}
```

| Operator | Operation | Description |
|---|---|---|
| `A \| B` | **Union** | All unique elements from both sets |
| `A & B` | **Intersection** | Only elements common to both sets |
| `A - B` | **Difference** | Elements in `A` but not in `B` |
| `A ^ B` | **Symmetric Difference** | Elements in either set, but not both |

### Membership Testing

Sets are highly efficient for `in` checks (faster than lists for large data):

```python
print('cloves' in essential_spices)   # True
print('ginger' in essential_spices)   # True
print('cinnamon' in essential_spices) # False
```

### Key Properties of Sets

| Property | Description |
|---|---|
| **Unordered** | No guaranteed element order |
| **Unique** | Duplicate values are automatically removed |
| **Mutable** | Elements can be added/removed (but elements themselves must be immutable) |
| **No Indexing** | Cannot access elements by index |

> **List vs Set — which to use?**  
> Use a **list** when order matters or duplicates are meaningful (e.g., a queue of orders).  
> Use a **set** when you need uniqueness or fast membership checks (e.g., checking if an ingredient has already been added).


<!-- Since I was committing with wrong email -->
Here is the test commit just because I was adding the commits using a wrong email.


## 📖 Dictionaries

A **dictionary** is an ordered (Python 3.7+), **mutable** collection of **key-value pairs** enclosed in curly braces `{}`. Each key must be unique and is used to access its associated value — much like a real-world dictionary where a word (key) maps to its definition (value).

### Creating a Dictionary

There are two common ways to create a dictionary:

```python
# Using dict() constructor
chai_order = dict(type="Masala chai", size="Large", sugar=2)

# Using curly brace literal
chai_recipe = {}
chai_recipe["base"]   = 'black_tea'
chai_recipe["liquid"] = 'milk'
```

> **Note:** Keys can be any immutable type (strings, numbers, tuples). Values can be anything.

---

### Accessing Values

```python
print(chai_recipe['base'])              # 'black_tea' → direct key access
print(chai_order.get('Note', "No Note")) # 'No Note'  → safe access with a default
```

| Method | Behaviour |
|---|---|
| `dict[key]` | Returns the value; raises `KeyError` if key is missing |
| `.get(key, default)` | Returns the value, or `default` if key is not found (no error) |

> **Prefer `.get()` over `[]`** when the key may not exist — it avoids runtime errors.

---

### Modifying a Dictionary

```python
# Add or update a single key
chai_recipe["liquid"] = 'milk'

# Merge another dictionary in (modifies in place)
extra_spices = {"cardamom": "crushed", "ginger": "sliced"}
chai_recipe.update(extra_spices)
# chai_recipe now includes all keys from extra_spices
```

| Method | Description |
|---|---|
| `dict[key] = value` | Adds a new key or **overwrites** an existing one |
| `.update(other_dict)` | Merges `other_dict` into the dictionary; existing keys are overwritten |

---

### Removing Elements

```python
del chai_recipe['liquid']
# Removes the key 'liquid' entirely; raises KeyError if not found

last_item = chai_order.popitem()
# Removes and returns the last inserted key-value pair as a tuple
print(last_item)   # ('sugar', 1)
```

| Method | Description |
|---|---|
| `del dict[key]` | Deletes a specific key-value pair |
| `.popitem()` | Removes and returns the **last inserted** pair as `(key, value)` |
| `.pop(key, default)` | Removes a specific key and returns its value (optional default) |

---

### Viewing Keys, Values & Items

```python
chai_order.keys()    # dict_keys(['type', 'size', 'sugar'])
chai_order.values()  # dict_values(['Ginger chai', 'Medium', 1])
chai_order.items()   # dict_items([('type', 'Ginger chai'), ('size', 'Medium'), ('sugar', 1)])
```

These are especially useful when iterating:

```python
for key, value in chai_order.items():
    print(f"{key}: {value}")
```

---

### Key Properties of Dictionaries

| Property | Description |
|---|---|
| **Ordered** | Insertion order is preserved (Python 3.7+) |
| **Mutable** | Keys and values can be added, updated, or removed |
| **Unique Keys** | Duplicate keys are not allowed; later values overwrite earlier ones |
| **Flexible Values** | Values can be of any data type, including lists, sets, or other dicts |

> **When to use a Dictionary?**  
> Use a dictionary when data is naturally structured as labeled fields — like a form, a config file, or an API response — where you need to look things up by name rather than position.