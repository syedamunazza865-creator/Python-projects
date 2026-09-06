# Section 9: Exception Handling

## What You Learn
- What exceptions are
- Try-except blocks
- Multiple except blocks
- Finally block
- Raising exceptions
- Custom exception classes

## Files

| File | Description |
|---|---|
| exceptions_basics.py | try-except, specific exceptions, else |
| multiple_except_finally.py | Multiple except, finally block |
| raising_exceptions.py | raise keyword, custom exceptions |
| safe_calculator.py | 🏆 Mini Project |

## Mini Project — Safe Calculator

A crash-proof calculator that NEVER crashes!

```python
class InvalidOperationError(Exception):
    pass

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid! Please enter a number!")
```

## Key Concepts

### Common Exceptions
| Exception | Cause |
|---|---|
| ValueError | Wrong data type conversion |
| ZeroDivisionError | Division by zero |
| TypeError | Wrong type operation |
| FileNotFoundError | File doesn't exist |
| KeyError | Dictionary key not found |
| IndexError | List index out of range |

### Try-Except Structure
```python
try:
    # code that might fail
except ValueError:
    # handle ValueError
except ZeroDivisionError:
    # handle ZeroDivisionError
except Exception as e:
    # handle any other error
else:
    # runs if NO error occurred
finally:
    # ALWAYS runs!
```

### Custom Exceptions
```python
class InvalidAgeError(Exception):
    pass

raise InvalidAgeError("Age cannot be negative!")
```
