## Functions

A **function** is a reusable block of code that performs a specific task. Instead of writing the same logic repeatedly, you define it once and call it whenever needed. Functions make your code cleaner, easier to read, and simpler to maintain.

**Syntax:**
```python
def function_name(parameters):
    # code block
    return value   # optional
```

---

### Defining and Calling a Function

Use the `def` keyword to define a function, followed by its name and any parameters in parentheses.

```python
def print_order(name, chai_type):
    print(f"{name} ordered {chai_type} chai")

print_order("Aman", "Masala")
print_order("Priti", "Ginger")
print_order("Shubham", "Mint")
```

Output:
```
Aman ordered Masala chai
Priti ordered Ginger chai
Shubham ordered Mint chai
```

- **Parameters** (`name`, `chai_type`) are the variables the function expects as input.
- **Arguments** (`"Aman"`, `"Masala"`) are the actual values passed when calling the function.
- The same function is called three times — write once, reuse many times.

---

### Functions Calling Other Functions

Functions can call other functions, letting you break complex tasks into smaller, focused pieces. This keeps each function doing **one thing well**.

```python
def fetch_sales():
    print("Fetching the sales data")

def filter_valid_sales():
    print("Filtering valid sales data")

def summarize_data():
    print("Summarizing sales data")

def generate_report():
    fetch_sales()
    filter_valid_sales()
    summarize_data()
    print("Report is ready!")

generate_report()
```

Output:
```
Fetching the sales data
Filtering valid sales data
Summarizing sales data
Report is ready!
```

> This is called **function decomposition** — breaking a large task (`generate_report`) into smaller, named steps. Each sub-function can be tested, reused, or swapped out independently.

---

### Returning Values

A function can compute a result and **return** it to the caller using the `return` keyword. The returned value can be stored in a variable or used directly.

```python
def calculate_bills(cups, price_per_cup):
    return cups * price_per_cup

my_bill = calculate_bills(3, 15)
print(f"Total bill: ₹{my_bill}")              # ₹45

print(f"Table 2:", calculate_bills(2, 100))   # ₹200 — used directly
```

- Without `return`, a function returns `None` by default.
- The returned value can be stored in a variable (`my_bill`) or used inline in another expression.

---

### Using Functions Inside Loops

Functions pair naturally with loops — apply the same logic to every item in a collection without repeating code.

```python
def add_vat(price, vat_rate):
    return price * (100 + vat_rate) / 100

orders = [100, 150, 200]

for price in orders:
    final_amount = add_vat(price, 10)
    print(f"Original: ₹{price}, With VAT: ₹{final_amount}")
```

Output:
```
Original: ₹100, With VAT: ₹110.0
Original: ₹150, With VAT: ₹165.0
Original: ₹200, With VAT: ₹220.0
```

> The VAT logic lives in one place. If the formula ever changes, you update it in the function — not in every loop.

---

### Key Properties of Functions

| Concept | Description |
|---|---|
| `def` | Keyword used to define a function |
| Parameters | Variables listed in the function definition |
| Arguments | Actual values passed when calling the function |
| `return` | Sends a value back to the caller; exits the function |
| No `return` | Function implicitly returns `None` |
| Reusability | Define once, call as many times as needed |
| Decomposition | Large tasks broken into smaller, focused functions |

---

### Why Use Functions?

```python
# Without functions — logic repeated everywhere
bill1 = 3 * 15
bill2 = 2 * 100
bill3 = 5 * 20

# With functions — one place to update, used everywhere
def calculate_bills(cups, price_per_cup):
    return cups * price_per_cup

bill1 = calculate_bills(3, 15)
bill2 = calculate_bills(2, 100)
bill3 = calculate_bills(5, 20)
```

| Benefit | Description |
|---|---|
| **DRY principle** | Don't Repeat Yourself — write logic once |
| **Readability** | Named functions read like plain English |
| **Maintainability** | Fix a bug in one place, fixed everywhere |
| **Testability** | Each function can be tested in isolation |

>  *This section covers the fundamentals — defining functions, returning values, decomposition, and using functions with loops. More concepts (default arguments, `*args`, `**kwargs`, scope, lambda) will be added as the course continues.*

## Gobal and Local Scope

## 🌐 Scope

**Scope** determines where a variable can be accessed in your code. Python follows the **LEGB rule** when resolving a name:

| Scope | Meaning |
|---|---|
| **L**ocal | Inside the current function |
| **E**nclosing | In the nearest enclosing function (for nested functions) |
| **G**lobal | At the top level of the script/module |
| **B**uilt-in | Provided by Python itself (e.g. `print`, `len`) |

Python searches in this order — **Local → Enclosing → Global → Built-in** — and uses the first match it finds.

---

### Local Scope

A variable created **inside a function** belongs to that function only. It doesn't affect a variable of the same name outside it.

```python
def serve_chai():
    chai_type = "Masala"   # local scope
    print(f"Inside function: {chai_type}")

chai_type = "lemon"
serve_chai()
print(f"Outside function: {chai_type}")
```

Output:
```
Inside function: Masala
Outside function: lemon
```

> The `chai_type` inside `serve_chai()` and the one outside are **two separate variables** that just happen to share a name.

---

### Enclosing Scope

When a function is defined **inside another function** (nested), the inner function can read variables from the outer (enclosing) function — but assigning to the same name inside creates a new **local** variable instead.

```python
def chai_counter():
    chai_order = 'lemon'        # enclosing scope (for print_order)

    def print_order():
        chai_order = 'Ginger'   # this creates a NEW local variable
        print("Inner:", chai_order)

    print_order()
    print("Outer:", chai_order)  # unchanged

chai_order = "Tulsi"             # global scope
chai_counter()
print("Global:", chai_order)
```

Output:
```
Inner: Ginger
Outer: lemon
Global: Tulsi
```

> Three different `chai_order` variables exist here — one global, one enclosing, one local — each independent unless explicitly linked.

---

### `nonlocal` — Modifying the Enclosing Variable

To **modify** (not just read) a variable from the enclosing scope, use `nonlocal`.

```python
def update_order():
    chai_type = "Elaichi"

    def kitchen():
        nonlocal chai_type
        chai_type = "Kesar"

    kitchen()
    print(f"After kitchen update: {chai_type}")

update_order()
```

Output:
```
After kitchen update: Kesar
```

> Without `nonlocal`, `chai_type = "Kesar"` inside `kitchen()` would create a new local variable instead of updating the enclosing one.

---

### `global` — Modifying the Global Variable

To **modify** a global variable from inside a function (even a nested one), use `global`.

```python
chai_type = "Plain"

def front_desk():
    def kitchen():
        global chai_type
        chai_type = "Irani"
    kitchen()

front_desk()
print("Final global chai:", chai_type)
```

Output:
```
Final global chai: Irani
```

| Keyword | Used to... |
|---|---|
| `nonlocal` | Modify a variable from the **nearest enclosing function's** scope |
| `global` | Modify a variable from the **module-level (global)** scope |

> Use `global`/`nonlocal` sparingly — modifying outer-scope variables from within functions can make code harder to trace and debug.

---

## 📥 Input Parameters

### Mutable Arguments Are Passed by Reference

Lists (and other mutable objects) passed to a function can be **modified in place** — changes are visible outside the function too.

```python
chai = [1, 2, 3]

def edit_chai(cup):
    cup[1] = 41

edit_chai(chai)
print(chai)   # [1, 41, 3]
```

> Unlike numbers or strings (immutable), mutable objects like lists are shared — the function receives a reference to the **same object**, not a copy.

---

### Positional vs Keyword Arguments

```python
def make_chai(tea, milk, sugar):
    print(tea, milk, sugar)

make_chai("Darjeeling", "Yes", "Low")              # positional
make_chai(tea="Green", sugar="low", milk="yes")    # keyword
```

| Type | Description |
|---|---|
| **Positional** | Arguments matched to parameters by **order** |
| **Keyword** | Arguments matched to parameters by **name** — order doesn't matter |

> Keyword arguments improve readability, especially when a function has many parameters.

---

### `*args` and `**kwargs`

Use these to accept a **variable number of arguments**.

```python
def special_chai(*ingredients, **extras):
    print("Ingredients:", ingredients)
    print("Extras:", extras)

special_chai("cinnamon", "cardamom", sweetener="honey", foam="yes")
```

Output:
```
Ingredients: ('cinnamon', 'cardamom')
Extras: {'sweetener': 'honey', 'foam': 'yes'}
```

| Syntax | Collects | Type |
|---|---|---|
| `*args` | Extra **positional** arguments | `tuple` |
| `**kwargs` | Extra **keyword** arguments | `dict` |

---

### ⚠️ Mutable Default Arguments — A Common Pitfall

```python
def chai_order(order=[]):
    order.append("Masala")
    print(order)

chai_order()   # ['Masala']
chai_order()   # ['Masala', 'Masala']  ⚠️ Not a fresh list!
```

> **Default argument values are evaluated only ONCE**, when the function is defined — not each time it's called. A mutable default (like `[]`) is **shared across all calls**, leading to unexpected accumulation.
>
> **Fix:** Use `None` as the default and create a new list inside the function:
> ```python
> def chai_order(order=None):
>     if order is None:
>         order = []
>     order.append("Masala")
>     print(order)
> ```

---

## ↩️ Return Statement

### Implicit `None`

A function with no `return` statement (or just `pass`) returns `None`.

```python
def idle_chaiwala():
    pass

print(idle_chaiwala())   # None
```

### Returning a Value

```python
def make_chai():
    return "Abhishek, here is your masala chai"

return_value = make_chai()
print(return_value)
```

### Early Return

`return` immediately exits the function — useful for handling special cases first.

```python
def chai_status(cups_left):
    if cups_left == 0:
        return "Sorry! Chai over"
    return "Chai is ready"

print(chai_status(0))   # Sorry! Chai over
print(chai_status(5))   # Chai is ready
```

### Returning Multiple Values

Python lets you return multiple values, packed as a **tuple**, and unpack them directly.

```python
def chai_report():
    return 100, 20   # sold, remaining

sold, remaining = chai_report()
print("sold:", sold)
print("remaining:", remaining)
```

| Return Style | Example | Result |
|---|---|---|
| Nothing / `pass` | `idle_chaiwala()` | `None` |
| Single value | `return "Chai is ready"` | The value itself |
| Early return | `if x: return ...` | Exits function immediately |
| Multiple values | `return a, b` | A tuple `(a, b)`, often unpacked |

---

## 🏷️ Types of Functions

### Pure Functions

A **pure function** always produces the same output for the same input and has **no side effects** (doesn't modify anything outside itself).

```python
def pure_functions(cups):
    return cups * 10
```

### Impure Functions

An **impure function** relies on or modifies state **outside its own scope** — making it less predictable and harder to test.

```python
total_chai = 0

def impure_chai(cups):
    global total_chai
    total_chai += cups
```

> ⚠️ Impure functions are generally **not recommended** — prefer pure functions where possible for predictability and easier testing.

### Recursive Functions

A **recursive function** calls itself, with a **base case** to stop the recursion.

```python
def pour_chai(n):
    print(n)
    if n == 0:
        return "All cups poured"
    return pour_chai(n - 1)

print(pour_chai(3))
```

Output:
```
3
2
1
0
All cups poured
```

> Every recursive function needs a **base case** (`n == 0` here) — without it, the function would call itself forever and raise a `RecursionError`.

### Lambda (Anonymous) Functions

A **lambda** is a small, unnamed function defined in a single line — useful for short operations passed to other functions like `filter()`, `map()`, or `sorted()`.

**Syntax:** `lambda arguments: expression`

```python
chai_types = ["light", "kadak", "ginger", "kadak"]

strong_chai = list(filter(lambda chai: chai == "kadak", chai_types))
print(strong_chai)   # ['kadak', 'kadak']
```

> Lambdas can only contain a **single expression** (no statements, no multiple lines). For anything more complex, use a regular `def` function.

---

### Quick Reference

| Function Type | Description |
|---|---|
| **Pure** | Same input → same output, no side effects |
| **Impure** | Depends on / modifies external state |
| **Recursive** | Calls itself; needs a base case |
| **Lambda** | Anonymous, single-expression function |

---

### Summary Table — Scope & Function Concepts

| Concept | Keyword/Pattern | Purpose |
|---|---|---|
| Local scope | (default) | Variable exists only inside its function |
| Enclosing scope | nested `def` | Inner function can read outer function's variables |
| Modify enclosing | `nonlocal` | Allows inner function to modify outer function's variable |
| Modify global | `global` | Allows any function to modify a module-level variable |
| `*args` | tuple of extra positional args | Accept variable number of positional arguments |
| `**kwargs` | dict of extra keyword args | Accept variable number of keyword arguments |
| Mutable default arg | `def f(x=[])` | ⚠️ Pitfall — shared across calls; use `None` instead |
| `return` | — | Sends value(s) back; exits function immediately |