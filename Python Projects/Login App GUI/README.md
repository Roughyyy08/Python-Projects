# Tkinter Login Page

A simple login page built with Python's Tkinter library. Not a real authentication system — built purely to understand how Tkinter works and how to build a basic GUI in Python.

---
<img width="448" height="676" alt="image" src="https://github.com/user-attachments/assets/5668f9c5-e9f9-43a7-9e5a-a4e421daf365" />

---

## Why I Built This

After learning Python fundamentals, I wanted to understand how to build desktop GUIs before moving deeper into the AI/ML stack.

Tkinter is Python's built-in GUI library — no installation needed, straightforward to learn, and a solid starting point for understanding how UI components work in code.

This project was my first hands-on session with Tkinter.

---

## What It Does

- Displays a login window with an image, title, email field, password field, and a login button
- Validates that both fields are filled before doing anything
- Checks if the email contains `@gmail.com`
- Shows a success or error popup depending on the result
- Password field hides characters while typing

---

## How to Run

**Requirements:** Python 3.x

Pillow is the only external library needed:

```bash
pip install pillow
```

Then run:

```bash
python main.py
```

Make sure `login-image.png` and `favicon.ico` are in the same folder as `main.py` before running.

---

## Project Structure

```
tkinter-login-page/
├── main.py            ← All the code
├── login-image.png    ← Image displayed on the UI
├── favicon.ico        ← Window icon
├── notes.md           ← My learning notes while building this
└── README.md          ← You are here
```

---

## Tkinter Concepts I Practiced

- Initializing a window with `Tk()` and `mainloop()`
- Setting window size, min/max size, title, and favicon
- `Label` — for displaying text and images
- `Entry` — for text input fields
- `Button` — with a `command` linked to a function
- `pack()` — geometry manager with `pady` and `ipady` for spacing
- `messagebox` — for success and error popups
- Loading and resizing images using `Pillow` (`PIL`)
- Using `pathlib` for reliable file paths across different machines
- Separating UI setup into a `setup_ui()` function to avoid cluttered global scope

---

## Good Practices I Applied

- Moved all widget creation into `setup_ui()` — keeps global scope clean
- Loaded all assets before building the UI
- Used `strip()` on inputs to catch empty spaces
- Used `show="•"` on the password field so characters are hidden
- Passed integers not strings to Tkinter parameters like `width`, `ipady`, `borderwidth`
- Used plain `if` after `return` instead of `elif` — cleaner control flow

---

## What I Learned

Tkinter works by attaching widgets to a root window and using a geometry manager (`pack`, `grid`, or `place`) to position them. Everything runs inside `mainloop()` which keeps the window alive and listens for events like button clicks.

The biggest thing that clicked: **UI in code is just creating objects and telling them where to go.** A button is an object. A text field is an object. You configure them, pack them, and connect them to functions.

Also learned that `pathlib` is the right way to handle file paths in Tkinter projects — hardcoded paths break when the project is opened on a different machine.

---

## Part of My 365 Day AI Journey

This project is part of my public learning challenge to become an AI/ML Engineer in 365 days.

**Day 19** — Python fundamentals complete. Exploring Tkinter before moving into NumPy and Pandas.

→ [View the full journey](https://github.com/Roughyyy08/Python-Projects)
