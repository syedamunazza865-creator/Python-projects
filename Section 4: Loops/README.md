# Section 4: Loops

## What You Learn
- For loops with range()
- For loops with strings
- While loops
- Break, continue and pass
- Nested loops and patterns

## Files

| File | Description |
|---|---|
| for_loop.py | For loop with range and strings |
| while_loop.py | While loop with real examples |
| break_continue_pass.py | Loop control keywords |
| nested_loops.py | Star patterns and tables |
| atm_simulator.py | 🏆 Mini Project |

## Mini Project — ATM Simulator

Fully working ATM with PIN verification,
balance check and cash withdrawal!

```python
while attempts < max_attempts:
    pin = input("Enter PIN: ")
    if pin == correct_pin:
        print("Access granted!")
        break
    else:
        attempts += 1
```

## Key Concepts
- for loop syntax
- range(start, stop, step)
- while loop syntax
- break — stops loop
- continue — skips iteration
- pass — placeholder
- Nested loops for patterns
- enumerate() function
