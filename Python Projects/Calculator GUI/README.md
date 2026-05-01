# Calculator GUI

A fully functional desktop calculator built with Python and Tkinter. Supports addition, subtraction, multiplication, division, decimal input, and chained operations — all inside a clean dark-themed window.

---

## What It Does

- Basic arithmetic: `+` `-` `*` `/`
- Decimal number support with duplicate dot prevention
- Chained operations — press an operator without hitting `=` first and it calculates automatically
- Division by zero handled gracefully — displays `Error` instead of crashing
- Results shown as integers when possible — `5.0` becomes `5`, `5.5` stays `5.5`
- `C` button resets everything back to `0`
- Fixed window size — no resizing, clean consistent layout

---

## How to Run

**Requirements:** Python 3.x — no external libraries needed. Tkinter comes built-in.

```bash
python main.py
```

---

## Project Structure

```
calculator-gui/
├── main.py       ← All the code
├── notes.md      ← My learning notes while building this
└── README.md     ← You are here
```

---

## How It Works

The entire calculator lives inside a `Calculator` class. Three pieces of state are tracked in `__init__`:

| Variable | What It Stores |
|----------|---------------|
| `first_number` | The first operand, saved when an operator is pressed |
| `operator` | The operator selected (`+`, `-`, `*`, `/`) |
| `reset_next` | A flag — when `True`, the next digit press clears the display and starts fresh |

**`press_digit()`**
Appends the digit to the display. If `reset_next` is `True` or the display shows `0`, it replaces the display instead of appending.

**`press_operator()`**
Saves the current display as `first_number`, stores the operator, and sets `reset_next = True` so the next digit starts a fresh number. If an operator is pressed while a calculation is already pending (chained operation), it calls `calculate()` first.

**`press_decimal()`**
Adds a decimal point only if one doesn't already exist — prevents inputs like `3..5`.

**`calculate()`**
Performs the operation using `first_number`, the stored `operator`, and the current display as `second`. Uses `finally` to always reset state after calculation, whether it succeeded or raised an error.

**`clear()`**
Resets all three state variables and sets the display back to `0`.

**Button layout**
All buttons are defined in a list of tuples `(text, row, col, span, command)` and rendered in a single loop using `.grid()`. The `=` button spans all 4 columns using `columnspan=4`.

---

## Concepts I Practiced

- Full OOP structure — entire app lives inside one class
- `StringVar` for live display updates without manually refreshing the label
- `.grid()` geometry manager with `columnspan` and `sticky`
- State management across multiple methods using instance variables
- `finally` block to guarantee state reset even when an exception occurs
- `__name__ == "__main__"` guard for clean entry point

---

## What I Learned

The most interesting part of building this was the `reset_next` flag.

Without it, pressing `5 + 3` would show `53` on the display instead of `3` — because the digit just appends to whatever is there. The flag tells `press_digit()` to wipe the display and start fresh the next time a digit is pressed, without actually clearing it immediately (so the user can still see the result of the previous calculation).

The second thing was chained operations. Pressing `5 + 3 * 2` without hitting `=` in between should work. The fix was simple — if `first_number` is already set and `reset_next` is `False` when an operator is pressed, call `calculate()` first, then set up the new operation with the result.

The `finally` block in `calculate()` was also new territory. It guarantees that `first_number`, `operator`, and `reset_next` are always reset after every calculation attempt, even if a `ZeroDivisionError` is raised. Without it, the calculator could end up in a broken half-calculated state after an error.

---

## Part of My 365 Day AI Journey

This project is part of my public learning challenge to become an AI/ML Engineer in 365 days.

**Day 22** — Python fundamentals complete. Exploring Tkinter before moving into NumPy and Pandas.

→ [View the full journey](https://github.com/Roughyyy08/Python-Projects)