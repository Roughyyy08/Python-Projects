Here's your updated `notes.md` — copy paste ready:

```markdown
# Wallpaper Viewer — Project Notes
*Python · Tkinter · PIL · pathlib*

---

## 1. The Problem

The goal was to build a desktop wallpaper viewer in Python that could display every image inside a folder, one at a time, with a Next and Prev button.

**The first challenge:**
- Too many images to label each one individually in code
- Images had to be loaded dynamically from a folder at runtime
- Every image needed to render in a loop — not be hardcoded

---

## 2. Building the GUI First

The GUI was set up first using Tkinter before tackling the image logic.

**What was set up:**
- `root = Tk()` — creates the main application window
- `root.title()` — sets the window title bar text
- `root.geometry('1000x600')` — defines the window size
- `root.minsize()` / `root.maxsize()` — locks the window to a fixed size
- `root.configure(background='#818181')` — sets a neutral grey background
- `root.iconbitmap(favicon_path)` — adds a custom icon to the title bar

**Paths were made reliable using pathlib:**
```python
favicon_path = Path(__file__).parent / "favicon.ico"
images_path  = Path(__file__).parent / "Wallpapers"
```
Using `__file__` means paths always resolve relative to the script itself,
regardless of where the script is run from.

---

## 3. The Real Challenge — Loading Images Dynamically

**Step 1 — Discover the files**

Instead of `os.listdir()`, pathlib's `folder.iterdir()` was used inside
the `load_images` function. `sorted()` is wrapped around it to keep the
order consistent across different operating systems:
```python
for file in sorted(folder.iterdir()):
```

**Step 2 — Filter only valid image files**

`os.listdir()` returns everything in the folder including hidden files like
`.DS_Store`. To avoid crashes, only files with valid extensions are processed:
```python
valid_extensions = {".jpg", ".jpeg", ".png", ".bmp", ".gif", ".webp"}

if file.suffix.lower() in valid_extensions:
```
`file.suffix` gives the extension e.g. `.jpg`. `.lower()` handles
uppercase extensions like `.JPG` or `.PNG`.

**Step 3 — Open, resize and convert each image**

For every valid file, the image is opened and resized in one line, then
converted to a Tkinter-compatible format and appended to the list:
```python
img = Image.open(file).resize((900, 500))
image_list.append(ImageTk.PhotoImage(img))
```
> **Why `ImageTk.PhotoImage()`?** Tkinter cannot display a PIL Image object
> directly. It must be converted before it can be used in a Label widget.

**Step 4 — Display the first image**

A Label widget displays the image since it accepts an `image` argument:
```python
image_label = Label(root, image=image_list[0], background="#818181")
image_label.pack(pady=(10, 10))
```

---

## 4. Handling Next and Prev Button Logic

### State — remembering which image is shown

Instead of a global variable, a mutable dictionary holds the current index:
```python
state = {"index": 0}
```
Functions can reach inside a dictionary and update its value directly.
A plain variable like `index = 0` would fail inside a function because
Python would treat it as a new local variable instead of modifying the original.

### The logic inside each function

Both functions follow the same three steps:
1. Update the index
2. Swap the image on the label
3. Enable or disable buttons at the boundaries

```python
def next_img():
    state["index"] = (state["index"] + 1) % len(image_list)
    image_label.configure(image=image_list[state["index"]])
    prev_btn.configure(state="normal" if state["index"] > 0 else "disabled")
    next_btn.configure(state="normal" if state["index"] < len(image_list) - 1 else "disabled")

def prev_img():
    state["index"] = (state["index"] - 1) % len(image_list)
    image_label.configure(image=image_list[state["index"]])
    prev_btn.configure(state="normal" if state["index"] > 0 else "disabled")
    next_btn.configure(state="normal" if state["index"] < len(image_list) - 1 else "disabled")
```

### Wrap-around with Modulo

The modulo operator `%` makes the viewer loop infinitely. Say you have 5 images:

| Current index | Calculation | New index |
|---|---|---|
| 0 | (0 + 1) % 5 | 1 |
| 1 | (1 + 1) % 5 | 2 |
| 3 | (3 + 1) % 5 | 4 |
| **4** | **(4 + 1) % 5 = 5 % 5** | **0 ← wraps** |

Without modulo, the index would go out of range and crash at the last image.

### Button enable/disable at boundaries

When on the first image, Prev is greyed out — there is nothing before it.
When on the last image, Next is greyed out — there is nothing after it:
```python
prev_btn.configure(state="normal" if state["index"] > 0 else "disabled")
next_btn.configure(state="normal" if state["index"] < len(image_list) - 1 else "disabled")
```

---

## 5. Mistakes Made & How They Were Fixed

| # | Mistake | Fix |
|---|---------|-----|
| 1 | Used backslashes in paths without raw strings — Python treated `\W` as an escape sequence | Switched to `pathlib` entirely — no backslashes needed |
| 2 | PIL Image objects appended directly — Tkinter cannot display them | Wrapped each image with `ImageTk.PhotoImage()` before appending |
| 3 | `image_number` started at `1` — first click skipped index `0` permanently | Initialised `state["index"]` to `0` |
| 4 | No filtering of non-image files — `os.listdir()` picks up hidden files | Added `valid_extensions` set and checked `file.suffix.lower()` |
| 5 | Used a `global` variable for the counter — bad practice | Replaced with a mutable dict `state = {"index": 0}` |
| 6 | `prev_img` and `next_img` logic was swapped — prev went forward, next went backward | Fixed: `next_img` uses `+ 1`, `prev_img` uses `- 1` |
| 7 | Wrong syntax `len%image_list` instead of `len(image_list)` | `len()` is a function call — the `%` goes between the two numbers, not inside `len` |
| 8 | Functions defined before `root = Tk()` — fragile ordering | Moved functions after `root`, `image_list` and `state` are set up, but before widgets |

---

## 6. Final Code Structure

```
load_images(folder)   →  reads, filters, resizes and converts all images into a list
state{"index"}        →  remembers which image is currently shown
next_img()            →  index + 1 with modulo, updates label and buttons
prev_img()            →  index - 1 with modulo, updates label and buttons
mainloop()            →  keeps the window open and listening for clicks
```

**Order of code matters:**
1. Imports and `valid_extensions`
2. `load_images()` function
3. `root = Tk()` and all window config
4. Paths, error checks
5. `image_list = load_images(images_path)`
6. `state = {"index": 0}`
7. `next_img()` and `prev_img()` functions
8. Widgets — label and buttons
9. `root.mainloop()`

---

## 7. Key Concepts Learned

- `Path(__file__).parent` — resolves paths relative to the script, not the working directory
- `folder.iterdir()` — pathlib way to loop through files in a folder
- `file.suffix.lower()` — gets the file extension in lowercase for safe comparison
- `Image.open()` + `.resize()` — opens and scales an image in one line
- `ImageTk.PhotoImage()` — mandatory conversion step for Tkinter compatibility
- `Label.configure(image=...)` — how to swap images in an existing label widget
- `state["index"] = (state["index"] + 1) % len(image_list)` — read, update, wrap, save back
- Mutable dict instead of `global` — functions can modify dict values without Python creating a local copy
- Extension filtering — prevents crashes from hidden or non-image files in the folder
- Button `state="disabled"` — greys out a button so the user knows they are at a boundary
```