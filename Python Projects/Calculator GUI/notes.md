# Calculator Project — Dev Notes
> tkinter · Python · OOP

---

## 1. Setting Up the Window

The first step is creating the root window and locking its size so the layout never shifts.

**What I used to do:**
```python
root.minsize(280, 420)
root.maxsize(280, 420)
```

**Better way (new learning):**
```python
root.resizable(0, 0)   # single call — disables both axes at once
```

The two arguments map to `(x-axis, y-axis)`. Passing `0` for both locks the window completely. Cleaner and more explicit than setting min/max separately.

---

## 2. Designing the Grid Layout

To get a real calculator look — rows and columns of buttons — the right geometry manager is `grid()`, not `pack()`.

**Why not `pack()`?**
- `pack()` stacks widgets linearly (top-to-bottom or left-to-right)
- `grid()` lets you place each widget at an exact `(row, col)` cell
- `grid()` is the only realistic choice for any 2-D layout

**Display label placement:**

Place the result label at `row=0` spanning all 4 columns so it sits above the button grid:
```python
result_label.grid(row=0, column=0, columnspan=4, sticky="e")
```
`sticky="e"` pins the text to the east (right) edge — just like a real calculator display.

---

## 3. State — What the Program Must Remember

Before writing any logic, identify what the calculator needs to hold in memory between button presses:

| Variable | Type | Purpose |
|---|---|---|
| `first_number` | `float` | Number saved when an operator is pressed |
| `operator` | `str` | The operation to perform (`+`, `-`, `*`, `/`) |
| `reset_next` | `bool` | If `True`, next digit starts fresh instead of appending |

These three variables are the entire brain of the calculator. Everything else is just reading or writing them.

---

## 4. Writing Button Logic

### 4a. Digit Buttons

When a digit is pressed, either start fresh or append to what's on the display:

```python
def _digit(self, d):
    if self.reset_next or self.display.get() == "0":
        self.display.set(d)        # replace
        self.reset_next = False
    else:
        self.display.set(self.display.get() + d)  # append
```

> ✗ **Mistake:** Fetched the digit as `int` — concatenating `"5" + 5` crashes. Keep everything as `str` on the display.

---

### 4b. Operator Buttons

Three things happen when an operator is pressed:
1. Save the current display value as `first_number` (as `float`)
2. Save which operator was clicked
3. Set `reset_next = True` so the next digit starts a fresh number

```python
def _operator(self, op):
    if self.first_number is not None and not self.reset_next:
        self._calculate()          # chain: evaluate pending op first
    self.first_number = float(self.display.get())
    self.operator = op
    self.reset_next = True
```

The chain-check at the top enables expressions like `3 + 5 - 2` without pressing `=` in between.

---

### 4c. Equals Button

Read the second number, apply the saved operator, show the result:

```python
ops = {"+": lambda a, b: a + b,
       "-": lambda a, b: a - b,
       "*": lambda a, b: a * b,
       "/": lambda a, b: a / b}

result = ops[self.operator](self.first_number, second)
```

Using a dict of lambdas instead of a long `if/elif` chain — shorter and easy to extend.

**Edge cases handled:**
- Divide by zero → `ZeroDivisionError` caught → display shows `"Error"`
- Whole number result (e.g. `6.0`) → shown as `6`, not `6.0`

---

### 4d. Clear Button

Reset everything — display back to `"0"`, all state variables back to `None` / `False`:

```python
def _clear(self):
    self.display.set("0")
    self.first_number = None
    self.operator = None
    self.reset_next = False
```

---

### 4e. Decimal Button

Two guards before appending a dot:
- If `reset_next` is `True`, start with `"0."` instead of appending
- If `"."` already exists in the display string, ignore the press

```python
def _decimal(self):
    if self.reset_next:
        self.display.set("0.")
        self.reset_next = False
    elif "." not in self.display.get():
        self.display.set(self.display.get() + ".")
```

---

## 5. Bugs Encountered & Fixed

1. ✗ **Display expanding and pushing buttons right** — fixed by adding `columnspan=4` to the label so it owns all 4 columns and the grid stays stable.

2. ✗ **Button `0` had no command** — pressing it did nothing. Fixed by wiring it to `press_digit("0")`.

3. ✗ **Division returned a float** (e.g. `3.0`) even for whole results. Fixed: check `if result == int(result)`, then cast.

4. ✗ **`finally` block in `calculate()` always ran** — even on early `return`, resetting state incorrectly. Removed `finally`; state reset now only happens after a real computation.

5. ✗ **All lambdas in the loop captured the last loop variable** — all buttons triggered the same digit. Fixed with the default-argument trick:
    ```python
    lambda l=label: self._handle(l)
    ```

---

## 6. New Learnings

1. ✓ `resizable(0, 0)` replaces the min/maxsize pattern — one call, two axes.

2. ✓ `StringVar` + `textvariable=` is the correct tkinter pattern for dynamic labels. Avoids `label["text"] = ...` scattered everywhere.

3. ✓ **List of tuples as a button layout table** — store `(label, row, col)` as data, then one loop builds all buttons. DRY principle in action:
    ```python
    BUTTONS = [
        ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
        ...
    ]
    for label, row, col in BUTTONS:
        Button(...).grid(row=row, column=col)
    ```

4. ✓ `lambda l=label` captures the loop value at that moment. Without it, all lambdas share the last value of the variable.

5. ✓ **Single `_handle()` dispatcher** — every button sends its label to one function which routes it. Adding a new button = one tuple in the list, nothing else.

6. ✓ **Dict of lambdas** for operators replaces `if/elif` chains — cleaner, easier to extend.

7. ✓ **Class-level constants** (`BUTTONS`, `OPERATORS`) belong outside `__init__` — they never change per instance.

---

## 7. Final Class Architecture

```
Calculator
│
├── __init__     →  sets state variables, calls _build_ui()
├── _build_ui    →  creates display label + all buttons via loop
├── _handle      →  single router called by every button
├── _digit       →  append or replace digit on display
├── _decimal     →  add decimal point safely
├── _operator    →  save first_number + op, set reset flag
├── _calculate   →  do the math, show result, reset state
└── _clear       →  reset everything to initial state
```

> Line count: ~120 lines (original) → 75 lines (refactored). Same functionality, zero bugs.