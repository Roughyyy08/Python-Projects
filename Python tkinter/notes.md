# Build GUIs Using Python | Python Tkinter

##  how to initialize the GUI

- first we have to import tkinter
- then create a variable which will be an object of tk class
- now we want our interface to be visible when we run our code

we can do this by following below steps:

- `from tkinter import *`
- `root = Tk()`
- `root.mainloop()` this line is important so that gui stays on the screen if we dont add it the gui will be visible for few secs and disappear 

## GUI Manipulation

- to change the title `tk` to your custom title use `root.title("your-title")`
- to change the favicn use `root.iconbitmap("your-favicon-path")`
    1. the favicon should be in .ico not .png or anything else
    2. give the proper relative path of the favion
    3. if you are still facing the issue import Path from pathlib `from pathlib import Path`
    4. then make a variable and give the path as shown here : icon_path = Path(__file__).parent/
    5. now use this icon_path instead of using favicon path directly
- to set a minimum size of your GUI use this `root.minsize(width,height)`
- to open it in a specific size use `root.geometry("width x height")`
- to change the background color use `root.configure(background="your-color")`
- to display a image on the GUI you need to import it using `from PIL import ImageTk, Image`
    - if not already installed, install a library using this command in terminal `pip install pillow`
    - then make a variable and store it like this `ImageTk.PhotoImage(Image.open(image-path))`
    - make a lablel for this using `Label(root, image=your-variable)`
    - open it using a geometry manager `image_label.pack()`
    - you can also change the position of image using `pady=(a,b)` or `padx=(a,b)` inside the `pack()`
- to resize your image first make a variable and open it using `Image.open(img-path)` then use `resize((width, height))`
- to write a texxt on the screen use label as shown for image but instead of `image=` use `text=`
- you can change the background and text colour also the font style and size `text="demo", fg="colour", bg="color", font=("style", size)` after 
- to add a input box make a variable and use `Entry(root, width="")` to customize height use `ipady=""` inside `pack()`
- to make a button