## Python Objects: Mutable vs Immutable

In Python, every value is an object. Objects can be classified based on whether their state can be changed after creation.

### Immutable Objects
Immutable objects cannot be modified after they are created. Any operation that appears to change them actually creates a new object.

Examples:
- int
- float
- str
- tuple
- bool

Example:
```python
x = 10
print(id(x))

x = x + 5
print(id(x))  # Different ID (new object created)
```

### Mutable Objects
Mutable objects can be modified after creation without changing their identity.

Examples:
- list
- dict
- set
- bytearray

Example:
```python
nums = [1, 2, 3]
print(id(nums))

nums.append(4)
print(id(nums))  # Same ID (object modified)
```

### Difference

| Mutable | Immutable |
|----------|------------|
| Can be changed after creation | Cannot be changed after creation |
| Same object is updated | New object is created |
| Examples: list, dict, set | Examples: int, str, tuple |

### Conclusion
Understanding mutable and immutable objects is important for managing memory, avoiding unexpected side effects, and writing efficient Python code.