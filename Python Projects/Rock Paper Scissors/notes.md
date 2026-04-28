# Rock Paper Scissors | Notes

## Initial Idea (Before I Started Coding)

I first thought of using numbers to represent choices:
- `-1` = Rock
- `0` = Paper  
- `1` = Scissors

And taking number input from the user. But I switched to using the actual words `["rock", "paper", "scissors"]` — easier to read, easier to validate, less confusing overall.

---

## How I Planned It

### What the computer needs to do
- Pick randomly from `["rock", "paper", "scissors"]` using the `random` built-in module

### What the player needs to do
- Type their choice using `input()`
- Only valid inputs: `rock`, `paper`, `scissors`, or `quit` to exit

### Rules
| Round Matchup | Winner |
|---------------|--------|
| Rock vs Scissors | Rock |
| Scissors vs Paper | Scissors |
| Paper vs Rock | Paper |
| Rock vs Rock | Tie |
| Paper vs Paper | Tie |
| Scissors vs Scissors | Tie |

### Methods I planned
1. `computer_choice()` — random pick from choices list
2. `play_round()` — handles one full round, returns True/False to control the loop
3. `determine_winner()` — compares player and computer choice, returns who won
4. `show_score()` — prints current score after each round
5. `final_result()` — prints full summary when game ends
6. `start()` — runs the game loop

### Game Flow
```
START
  LOOP forever:
    ask player for input
    IF input is "quit" → BREAK
    IF input is invalid → ask again (don't end the game)
    generate computer choice
    compare choices → find winner
    update score
    show result and score
  END LOOP
  show final result
END
```

---

## Problems I Faced

| Problem | What Was Happening |
|--------|-------------------|
| `Winner_Map` was wrong | Some matchups were missing or mapped incorrectly so wrong player was winning |
| Scores reset after every round | I had scores inside the method, not in `__init__` |
| Game ended after one round | `play_round()` wasn't returning `True` to keep the loop going |
| Invalid input ended the game | No early `return True` after the invalid input check |
| Computer choice printed on invalid input | Computer choice was generated before input was validated |

---

## How I Fixed It

**`Winner_Map` wrong logic**
- Rewrote it from one consistent point of view — always player vs computer
- If the tuple `(player, computer)` is in the map, player wins. Otherwise computer wins. Simple and clean.

**Scores resetting**
- Moved `players_score`, `computers_score`, `ties`, `rounds_played` all into `__init__`
- This way they belong to the object, not the method — so they stay alive across every round and every method can access them

**Game ending after one round**
- Added `return True` at the end of `play_round()` after `show_score()`
- The `while True` loop in `start()` checks this return value — `True` keeps it going, `False` breaks it

**Invalid input ending the game**
- Added `return True` right after the invalid input `print` — this sends control back to the loop without breaking it

**Computer choice showing on invalid input**
- Moved `computer = self.computer_choice()` to after all input validation is done
- Computer only picks once we know the player input is valid

---

## What I Learned

- Store anything that needs to survive across multiple method calls in `__init__` — that's exactly what it's for
- `return True` and `return False` from inside a loop-controlling method is a clean way to manage game flow without messy `break` statements everywhere
- A dictionary as a lookup table (`Winner_Map`) beats a long chain of `if/elif` every time — shorter, readable, and easy to change
- Always validate input before doing anything else with it — generate computer choice after, not before
- One consistent point of view in logic (`player wins if tuple in map, else computer wins`) prevents confusing bugs