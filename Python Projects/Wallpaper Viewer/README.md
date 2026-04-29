# Wallpaper Viewer

A desktop wallpaper browser built with Python and Tkinter. Drop your images into a folder, run the script, and browse through them one by one using Prev and Next buttons.

![App Preview](app-preview.png)
---

## What It Does

- Loads every image from the `Wallpapers` folder automatically — no hardcoding filenames
- Displays each image resized to `900x500` inside a `1000x600` window
- Prev and Next buttons to navigate through images
- Prev is disabled on the first image, Next is disabled on the last — no wrapping around
- Crashes early with a clear error if the `Wallpapers` folder is missing or empty — no silent failures
- Favicon support — shows a custom window icon if `favicon.ico` is present

---

## How to Run

**Requirements:** Python 3.x

Install the only external dependency:

```bash
pip install pillow
```

Add your images to the `Wallpapers` folder, then run:

```bash
python wallpaper_viewer.py
```

**Supported formats:** `.jpg` `.jpeg` `.png` `.bmp` `.gif` `.webp`

---

## Project Structure

```
wallpaper-viewer/
│
├── wallpaper_viewer.py   ← All the code
├── favicon.ico           ← Window icon (optional)
├── notes.md              ← My learning notes while building this
├── README.md             ← You are here
│
└── Wallpapers/           ← Put your images here
    ├── image1.jpg
    ├── image2.png
    └── ...
```

---

## How It Works

**Loading images**

`load_images()` iterates over the `Wallpapers` folder using `pathlib`, filters files by extension, resizes each one to `900x500` using Pillow, converts them to `ImageTk.PhotoImage` format, and stores them all in a list. This happens once at startup.

**Navigation**

A dictionary `state = {"index": 0}` tracks which image is currently displayed. A dictionary is used instead of a plain variable because inner functions in Python can read outer variables but cannot reassign them — a mutable dictionary gets around this cleanly.

Clicking Next increments the index, clicking Prev decrements it. After each click, both buttons are re-evaluated:

```python
prev_btn.configure(state="normal" if state["index"] > 0 else "disabled")
next_btn.configure(state="normal" if state["index"] < len(image_list) - 1 else "disabled")
```

**Error handling**

Two checks run before the UI builds:
- If the `Wallpapers` folder doesn't exist → `FileNotFoundError`
- If the folder exists but has no valid images → `ValueError`

This prevents the app from starting in a broken state silently.

---

## Concepts I Practiced

- Dynamically loading files from a folder using `pathlib`
- Filtering files by extension using a set (`valid_extensions`)
- Converting PIL images to Tkinter-compatible format with `ImageTk.PhotoImage()`
- Using a mutable dictionary for state that inner functions can modify
- Enabling and disabling buttons based on current state
- Early error raising with descriptive messages before the UI starts
- `sorted()` on folder contents so images load in consistent order

---

## What I Learned

The most important thing this project taught me was **why state needs to live in a mutable object**.

At first I tried tracking the index in a plain variable. The buttons could read it but couldn't change it — Python's scoping rules don't allow inner functions to reassign outer variables directly. Wrapping it in a dictionary (`state = {"index": 0}`) solved this because the functions aren't reassigning the variable, they're mutating the object it points to.

The second thing was **loading everything upfront**. All images are resized and converted once at startup and stored in a list. This makes navigation instant — no file reading or processing happening on every button click.

---

## Part of My 365 Day AI Journey

This project is part of my public learning challenge to become an AI/ML Engineer in 365 days.

**Day 15** — Python fundamentals complete. Exploring Tkinter before moving into NumPy and Pandas.

→ [View the full journey](https://github.com/Roughyyy08/Python-Projects)
