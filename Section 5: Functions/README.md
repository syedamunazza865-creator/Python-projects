# Section 5: Functions

## What You Learn
- Defining functions with def
- Parameters and arguments
- Return statement
- Default parameters
- Keyword arguments
- Modular programming

## Files

| File | Description |
|---|---|
| functions_basic.py | Defining and calling functions |
| function_parameters.py | Single and multiple parameters |
| return_statement.py | Return values and combining functions |
| default_keyword_params.py | Default and keyword arguments |
| quiz_game.py | 🏆 Mini Project |

## Mini Project — Simple Quiz Game

Interactive Python quiz using 4 functions working together!

```python
def ask_question(question, correct_answer):
    user_answer = input(question)
    if user_answer.lower() == correct_answer.lower():
        return True
    return False

def run_quiz():
    score = 0
    if ask_question("Q1. What keyword defines a function?", "def"):
        score += 1
    # ... more questions
```

## Key Concepts
- def keyword
- Parameters vs arguments
- return statement
- Default parameter values
- Keyword arguments
- Modular programming approach
- Functions calling other functions
