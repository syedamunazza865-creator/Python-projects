# Section 7: String Operations

## What You Learn
- String case methods
- String cleaning methods
- String searching methods
- String formatting with f-strings
- String slicing and indexing

## Files

| File | Description |
|---|---|
| string_methods.py | upper, lower, strip, replace, split, join |
| string_formatting.py | f-strings, .2f, number formatting |
| string_slicing.py | Indexing, slicing, [::-1] reversal |
| text_analyser.py | 🏆 Mini Project |

## Mini Project — Text Analyser

Analyses any text and generates detailed statistics!

```python
total_words = len(text.split())
vowel_count = sum(1 for char in text if char in "aeiouAEIOU")
most_common = max(word_count, key=word_count.get)
```

## Key Concepts

### Case Methods
```python
text.upper()      # HELLO WORLD
text.lower()      # hello world
text.title()      # Hello World
text.strip()      # removes spaces
```

### F-Strings
```python
name = "Syeda"
print(f"Hello {name}!")           # Hello Syeda!
print(f"Percentage: {85.678:.2f}") # 85.68
print(f"Salary: {75000:,}")        # 75,000
```

### Slicing
```python
text = "Python"
text[0]     # P
text[-1]    # n
text[::-1]  # nohtyP (reversed!)
```
