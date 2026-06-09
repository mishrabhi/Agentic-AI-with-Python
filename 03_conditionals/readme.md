## Conditionals

**Conditionals** let your program make decisions — executing different blocks of code based on whether a condition is `True` or `False`. Python supports several forms: simple `if`, multi-branch `if/elif/else`, nested conditions, ternary expressions, and the modern `match-case`.

---

### `if` — Simple Condition

The most basic form: run a block only when a condition is true.

```python
kettle_boiled = True

if kettle_boiled:
    print("Kettle done! Time to make chai")
```

> Any truthy value (non-zero number, non-empty string, `True`) triggers the `if` block. Falsy values (`False`, `0`, `None`, `""`, `[]`) skip it.

---

### `if / elif / else` — Multiple Branches

Use `elif` to check additional conditions in order, and `else` as a final catch-all.

```python
cup = input("Choose your cup size (small/medium/large): ").lower()

if cup == 'small':
    print("Price is ₹10")
elif cup == "medium":
    print("Price is ₹15")
elif cup == "large":
    print("Price is ₹20")
else:
    print("Unknown cup size")
```

Python evaluates each condition **top to bottom** and executes only the **first** matching branch. The `else` block runs if no condition matched.

| Branch | Purpose |
|---|---|
| `if` | First condition to check |
| `elif` | Additional conditions (as many as needed) |
| `else` | Fallback when nothing else matches |

---

### Nested `if` — Conditions Inside Conditions

You can place an `if` block inside another to check compound situations step by step.

```python
device_status = 'active'
temperature = 33

if device_status == 'active':
    if temperature > 35:
        print("High temperature alert!")
    else:
        print("Temperature is normal")
else:
    print("Device is offline")
```

> **Tip:** Avoid deeply nesting conditionals — more than 2-3 levels becomes hard to read. Consider restructuring with `and`/`or` or early returns where possible.

---

### Ternary Operator — Inline Conditions

Python's ternary (conditional) expression lets you write a simple `if/else` in a single line.

**Syntax:** `value_if_true if condition else value_if_false`

```python
order_amount = int(input("Enter the order amount: "))

delivery_fees = 0 if order_amount > 300 else 30
print(f"Delivery fees is: ₹{delivery_fees}")
```

This is equivalent to:

```python
if order_amount > 300:
    delivery_fees = 0
else:
    delivery_fees = 30
```

> Use the ternary operator for **simple, readable** assignments. For complex logic, stick to a full `if/else` block for clarity.

---

### `match-case` — Structural Pattern Matching

Introduced in **Python 3.10**, `match-case` is the clean alternative to long `if/elif` chains when comparing a value against multiple fixed options.

```python
seat_type = input("Enter seat type (sleeper/AC/general/luxury): ").lower()

match seat_type:
    case "sleeper":
        print("Sleeper - No AC, but beds are available")
    case "ac":
        print("AC - Air conditioned")
    case "general":
        print("General - Cheapest option, no reservation required")
    case "luxury":
        print("Premium seats with meals")
    case _:
        print("Invalid seat type")
```

| Element | Role |
|---|---|
| `match value` | The value being examined |
| `case "x"` | Matches when value equals `"x"` |
| `case _` | Wildcard — matches anything (like `else`) |

> **`match-case` vs `if/elif`:** Prefer `match-case` when branching on a single variable against known fixed values. Use `if/elif` when conditions involve comparisons, ranges, or multiple variables.

---

### Quick Reference

| Form | Best Used When |
|---|---|
| `if` | Single condition to check |
| `if / elif / else` | Multiple discrete options |
| Nested `if` | A condition depends on a prior one being true |
| Ternary `x if cond else y` | Simple two-outcome assignments in one line |
| `match-case` | Matching one variable against several fixed values |