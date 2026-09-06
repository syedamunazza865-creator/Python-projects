# Section 6: Data Structures

## What You Learn
- Lists — ordered changeable collections
- List methods — append, remove, sort etc
- Tuples — ordered unchangeable collections
- Dictionaries — key-value pairs
- Sets — unique unordered collections

## Files

| File | Description |
|---|---|
| lists_basics.py | Creating and accessing lists |
| list_methods.py | append, insert, remove, sort etc |
| tuples.py | Tuples and immutability |
| dictionaries.py | Key-value pairs and methods |
| sets.py | Unique items and set operations |
| student_management.py | 🏆 Mini Project |

## Mini Project — Student Management System

Uses ALL 4 data structures together!

```python
students = []          # LIST — all student records
courses = set()        # SET — unique courses
system_info = ("Student Management System", "v1.0")  # TUPLE
student = {            # DICT — each student's details
    "name": "Rahul",
    "course": "BCA"
}
```

## Key Concepts

| Data Structure | Syntax | Mutable | Ordered | Unique |
|---|---|---|---|---|
| List | [] | ✅ | ✅ | ❌ |
| Tuple | () | ❌ | ✅ | ❌ |
| Dictionary | {} | ✅ | ✅ | Keys only |
| Set | set() | ✅ | ❌ | ✅ |
