from tkinter import *
from pathlib import Path
from PIL import ImageTk, Image

valid_extensions = {".jpg", ".jpeg", ".png", ".bmp", ".gif", ".webp"}

def load_images(folder: Path) -> list:
    image_list = []
    for file in sorted(folder.iterdir()):
        if file.suffix.lower() in valid_extensions:
            img = Image.open(file).resize((900, 500))
            image_list.append(ImageTk.PhotoImage(img))
    return image_list

root = Tk()
root.title("Wallpaper Viewer")
root.geometry("1000x600")
root.minsize(1000, 600)
root.maxsize(1000, 600)
root.configure(background="#818181")

favicon_path = Path(__file__).parent / "favicon.ico"
images_path = Path(__file__).parent / "Wallpapers"

if favicon_path.exists():
    root.iconbitmap(favicon_path)

if not images_path.exists() or not images_path.is_dir():
    raise FileNotFoundError(f"Wallpapers folder not found: {images_path}")

image_list = load_images(images_path)

if not image_list:
    raise ValueError("No valid images found in Wallpapers folder")

state = {"index": 0}

def prev_img():
    state["index"] = (state["index"] - 1) % len(image_list)
    image_label.configure(image=image_list[state["index"]])
    prev_btn.configure(state="normal" if state["index"] > 0 else "disabled")
    next_btn.configure(state="normal" if state["index"] < len(image_list) - 1 else "disabled")

def next_img():
    state["index"] = (state["index"] + 1) % len(image_list)
    image_label.configure(image=image_list[state["index"]])
    prev_btn.configure(state="normal" if state["index"] > 0 else "disabled")
    next_btn.configure(state="normal" if state["index"] < len(image_list) - 1 else "disabled")

image_label = Label(root, image=image_list[0], background="#818181")
image_label.pack(pady=(10, 10))

prev_btn = Button(root, text="PREV", command=prev_img, state="disabled")
prev_btn.pack(side="left", padx=(200, 5), pady=(0, 20))

next_btn = Button(root, text="NEXT", command=next_img)
next_btn.pack(side="left", padx=(5, 200), pady=(0, 20))

root.mainloop()