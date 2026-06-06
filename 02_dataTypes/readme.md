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