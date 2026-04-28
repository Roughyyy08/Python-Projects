# Rent Calculator

A simple Python tool to split shared living expenses equally among friends. Enter your rent, food, and electricity details and it instantly tells you how much each person owes.

---

## What Problem Does This Solve?

Living with friends or flatmates means splitting bills every month. Doing this manually leads to confusion, arguments, and someone always getting the math wrong.

This tool takes all three major shared expenses, adds them up, and divides fairly — in seconds.

---

## What It Calculates

| Expense | How It Works |
|--------|--------------|
| Rent | Fixed amount entered directly |
| Food | Total monthly food spend |
| Electricity | Units consumed × charge per unit |
| **Total** | Rent + Food + Electricity bill |
| **Per Person** | Total ÷ Number of friends |

---

## How to Run

**Requirements:** Python 3.x — no external libraries needed.

```bash
python main.py
```

You'll be prompted to enter:

```
Number of friends: 3
Rent of Room/PG: 9000
Total amount spent on food: 3000
No. of units consumed: 80
Charge per unit: 8
```

**Output:**
```
Total amount to be paid is 12640
Hence, the split among each member is 4213.33
```

---

## Project Structure

```
rent-calculator/
├── main.py       ← All the code
├── notes.md      ← My raw thought process, mistakes, and fixes
└── README.md     ← You are here
```

---

## Concepts Used

- Object Oriented Programming (Classes, `__init__`, methods)
- User input handling
- Exception handling (`try` / `except` for invalid inputs)
- f-strings for formatted output
- Edge case handling (zero friends check)

---

## What I Learned Building This

This was my first project applying OOP to a real-world problem instead of just practicing syntax.

The key shift was thinking in objects — a `RentCalculator` isn't just a function, it's something that holds data (`rent`, `food`, `units`) and knows how to act on it (`calculate_total()`, `split()`). That mental model clicked here.

Also handled two edge cases I didn't think about at first:
- What if someone enters zero friends? (division by zero)
- What if someone types letters instead of numbers? (ValueError)

Small project. Real thinking.

---

## Part of My 365 Day AI Journey

This project is part of my public learning challenge to become an AI/ML Engineer in 365 days.

**Day 16** — Python fundamentals complete. Building projects while moving into NumPy and Pandas.

→ [View the full journey](https://github.com/Roughyyy08/Python-Projects)
