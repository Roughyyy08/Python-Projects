# Computer Choice 

- It should be random, can be done using `random` built-in module in python
- It should be only between these three numbers `[-1, 0, 1]`

---

# User Choice

- Take input from user using `input()`
- It should be only between these three numbers `[-1, 0, 1]`

---

# Defining Numbers

- `-1` means Rock
- `0` means Paper
- `1` means Scissors

---

# Rules of Game

- Rock vs Paper
- Rock vs Scissors
- Paper vs Scissors
- Rock vs Rock
- Paper vs Paper
- Scissors vs Scissors

---

# Action Plan

- using class because i want to store the scores and decide a winner
- fix the choices [rock, paper, scissors]
- deciding what functions to make
    1. Computer Choice
    2. Player Input
    3. Play a Round
    4. Deciding Winner
    5. Round Score
    6. Final Result

- Design
    START game
        LOOP forever:
            ask player for input
            IF input is "quit" → BREAK
            IF input is invalid → ask again
            generate computer choice
            compare choices → find winner
            update score
            show result and score
        END LOOP
           show final result
    END

# Problems I Faced

- winner_map was wrong
- score used to reset after every game
- game was ending after every round
- if input was invalid the game ends automatically
- when invalid input was given computer output used to be printed

---

# Solutions

- do it from one pov so that either player or computer wins all the time and use that in determine_winner
- store scores in `__init__` because it belongs to object not function 
    1. scores are stores
    2. accessible by multiple methods 
- return True in `play_round()` after `show_score()`
- return True after invalid choices case in `play_round()`
- initialize the computer variable after the if else of player is finished

---