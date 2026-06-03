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