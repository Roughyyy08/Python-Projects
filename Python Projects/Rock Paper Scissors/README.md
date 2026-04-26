# Rock Paper Scissors

A terminal-based Rock Paper Scissors game in Python where you play multiple rounds against the computer, track scores, and get a final result at the end.

---

## What Makes This Different From a Basic Version

Most beginner Rock Paper Scissors projects are just:
- Get player input
- Generate random computer choice
- Compare and print result
- Done

This one is a full game loop with:
- Persistent score tracking across rounds
- Named reasons for each win (`"Rock Crushes Scissors"`, `"Scissors Cuts Paper"`)
- Invalid input handling without crashing the game
- A final result summary with an overall winner
- Clean OOP structure where scores belong to the object, not individual functions

---

## How to Run

**Requirements:** Python 3.x — no external libraries needed.

```bash
python main.py
```

**Gameplay:**

```
===================================
   ROCK PAPER SCISSORS
===================================

Round 1
Choose: rock, paper, scissors (or quit to exit)
Enter your choice: rock
Computer chose: scissors

You Win! Rock Crushes Scissors

Scores:
You: 1 | Computer: 0 | Ties: 0
---------------------------------------------
```

Type `quit` at any point to end the game and see your final result.

---

## Project Structure

```
rock-paper-scissors/
├── main.py       ← All the code
├── notes.md      ← My raw thought process, mistakes, and fixes
└── README.md     ← You are here
```

---

## How It Works

The entire game lives inside a `RockPaperScissors` class.

**`Winner_Map`** — a dictionary that maps winning combinations to their reason string. Instead of a long chain of `if/elif` comparisons, the winner check is just a dictionary lookup:

```python
Winner_Map = {
    ("paper", "rock")     : "Paper Covers Rock",
    ("rock", "scissors")  : "Rock Crushes Scissors",
    ("scissors", "paper") : "Scissors Cuts Paper",
}
```

**`determine_winner()`** — checks three cases: tie, player wins (tuple in Winner_Map), or computer wins (everything else).

**`play_round()`** — returns `True` to keep the game loop running, `False` only when the player types `quit`. This is what keeps the game alive across rounds.

**`__init__`** — stores all scores here so they persist across every round instead of resetting.

---

## Concepts Used

- Object Oriented Programming (class-level variables, instance variables, multiple methods)
- Dictionary as a lookup table (`Winner_Map`)
- `random.choice()` for computer selection
- Game loop with `while True` and controlled exit via `return False`
- Input validation without killing the game
- f-strings for formatted output

---

## Bugs I Hit and Fixed

| Bug | Fix |
|-----|-----|
| Scores reset after every round | Moved score variables to `__init__` so they belong to the object |
| Game ended after one round | `play_round()` now returns `True` to keep the loop running |
| Invalid input ended the game | Added early `return True` after the invalid input check |
| Computer choice printed even on invalid input | Moved `computer_choice()` call to after input validation |
| `Winner_Map` logic was wrong | Rewrote it from one consistent point of view (player perspective) |

---

## What I Learned Building This

The biggest lesson here was understanding **why scores go in `__init__`**.

At first I was tracking scores inside individual functions. They worked for one round, then vanished. Once I moved them to `__init__`, they became part of the object itself — accessible by every method, persistent for the entire game.

The second thing was the game loop design. Returning `True` or `False` from `play_round()` to control the `while` loop is a clean pattern I hadn't used before. It keeps the loop logic readable without needing `break` scattered everywhere.

And the `Winner_Map` dictionary approach taught me that a well-structured data structure can replace a mess of conditionals entirely.

---

## Part of My 365 Day AI Journey

This project is part of my public learning challenge to become an AI/ML Engineer in 365 days.

**Day 15** — Python fundamentals complete. Building projects while moving into NumPy and Pandas.

→ [View the full journey](https://github.com/Roughyyy08/Python-Projects)