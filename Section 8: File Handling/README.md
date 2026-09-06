# Section 8: File Handling

## What You Learn
- Reading files with open()
- Writing and appending files
- Working with CSV files
- with statement best practice
- File modes — r, w, a, x

## Files

| File | Description |
|---|---|
| reading_files.py | read(), readline(), readlines() |
| writing_files.py | write(), writelines(), append mode |
| csv_files.py | csv.reader, csv.writer, DictReader |
| students.txt | Sample text data file |
| students.csv | Sample CSV data file |
| student_data_manager.py | 🏆 Mini Project |

## Mini Project — Student Data Manager

Complete student management system with permanent CSV storage!

```python
# Save student to CSV
with open(FILE_NAME, "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([name, roll, course, percentage])

# Load all students from CSV
with open(FILE_NAME, "r") as file:
    reader = csv.DictReader(file)
    students = list(reader)
```

## Key Concepts

### File Modes
| Mode | Meaning |
|---|---|
| r | Read — file must exist |
| w | Write — creates or overwrites |
| a | Append — adds to existing |
| x | Create — fails if exists |

### CSV Methods
```python
csv.reader()      # reads rows as lists
csv.DictReader()  # reads rows as dictionaries
csv.writer()      # writes lists to CSV
csv.DictWriter()  # writes dicts to CSV
```

### Best Practice
```python
# Always use with statement!
with open("file.txt", "r") as file:
    content = file.read()
# File automatically closed here!
```
