# Rent Calculator | Notes

## Inputs Needed From User

- Number of friends / people living together
- Total rent of Room / PG
- Total amount spent on food
- Electricity units consumed
- Charge per unit

---

## Expected Output

- Total amount to be paid
- Share of each member

---

## How I Planned It

- One class `RentCalculator` to hold all the data and logic
- `calculate_total()` to add rent + food + electricity bill
- `split()` to divide total by number of friends
- Take all inputs outside the class, create an object, call the methods

---

## Mistakes I Made

| Mistake | Why It Was a Problem |
|--------|----------------------|
| Did not convert input using `int()` | `input()` always returns a string, math operations fail on strings |
| Wrote everything directly with no structure | Hard to read, reuse, or fix later |
| Did not handle division by zero | Crashes the program if friends = 0 |
| Did not check if friends = 0 before creating object | The error shows up inside the class instead of being caught early |
| Used `return` outside a function | Syntax error, `return` only works inside a function |
| No exception handling | Any wrong input like letters instead of numbers crashes everything |

---

## How I Fixed It

- Wrapped all inputs in `int()` to convert string to number
- Used a class with separate methods for total and split calculation
- Added a check before object creation — if `friends == 0`, print error and `exit()`
- Also added the same check inside `split()` as a safety net
- Wrapped all inputs in `try / except ValueError` to handle wrong input gracefully
- Kept the class reusable — it only does calculations, input/output stays outside

---

## What I Learned

- `input()` always returns a string — always convert it
- Classes are not just for complex programs, even small tools benefit from structure
- Handle edge cases before they reach your logic, not inside it
- `try / except` should wrap the risky part only, not the entire program