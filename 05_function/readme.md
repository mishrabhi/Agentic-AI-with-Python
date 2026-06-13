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