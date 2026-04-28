# Build GUIs Using Python | Tkinter

## How to Initialize the GUI

- Import tkinter
- Create a variable as an object of the `Tk` class
- Call `mainloop()` to keep the window visible

```python
from tkinter import *
root = Tk()
root.mainloop()
```

> `root.mainloop()` is important — without it the window appears for a split second and disappears.

After these three steps your outpput should  look somethinng like this basically it is a basic GUI
<img width="253" height="291" alt="image" src="https://github.com/user-attachments/assets/cf499c10-6c30-4ebe-9d85-35eb96c527e1" />


---

## GUI Manipulation

### Window Settings

- Change title: `root.title("your-title")`
- Set minimum size: `root.minsize(width, height)`
- Open in a specific size: `root.geometry("widthxheight")` — no spaces around `x`
- Change background color: `root.configure(background="color")`

### Favicon (Window Icon)

- Change favicon: `root.iconbitmap("your-favicon-path")`
  - Must be a `.ico` file, not `.png` or anything else
  - Use the correct relative path
  - If still facing issues, use `pathlib`:

```python
from pathlib import Path
icon_path = Path(__file__).parent / "icon.ico"
root.iconbitmap(icon_path)
```

---

## Widgets

### Displaying an Image

- Install Pillow if not already installed:

```bash
pip install pillow
```

- Import and display:

```python
from PIL import ImageTk, Image

img = ImageTk.PhotoImage(Image.open("image-path"))
image_label = Label(root, image=img)
image_label.pack()
```

- Adjust position using `pady=(top, bottom)` or `padx=(left, right)` inside `pack()`

### Resizing an Image

```python
img = Image.open("image-path")
img = img.resize((width, height))
```

---

### Displaying Text

```python
Label(root, text="your text", fg="text-color", bg="bg-color", font=("FontStyle", size)).pack()
```

---

### Input Box (Entry)

```python
entry = Entry(root, width=30)
entry.pack(ipady=8)
```

- `width` controls horizontal size
- `ipady` inside `pack()` controls height

---

### Button

- Your notes got cut off here — add how to make a button once you learn it:

```python
btn = Button(root, text="Click Me", command=your_function)
btn.pack()
```

---

## Mistakes to Avoid

- Using `root.geometry("width x height")` with spaces around `x` — it won't work
- Using `.png` for favicon instead of `.ico`
- Forgetting `root.mainloop()` at the end
- Not storing the image in a variable before passing to `Label` — Tkinter's garbage collector will delete it and the image won't show
