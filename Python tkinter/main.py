from tkinter import *                       # for GUIs
from pathlib import Path                    # for image path problem
from PIL import ImageTk, Image              # to display image on screen

root = Tk()

# title
root.title("Title")

# manipualting the size of GUI 
root.minsize(width="",height="")
root.geometry("width x height")

# creating a variable for path of image 
icon_path = Path(__file__).parent/"star.ico"
root.iconbitmap(icon_path)

# changing background color
root.configure(background="color")

# resizing the image 
original_image = Image.open(icon_path)
resized_image = original_image.resize((x,y))

# displaying image on screen
# img = ImageTk.PhotoImage(Image.open(icon_path))
img = ImageTk.PhotoImage(resized_image)
image_label = Label(root, image=img)
image_label.pack(pady=(50,20))                          # changing the positiion of image 

# adding text to screen
text_label = Label(root, text="text", fg="font-colour", bg="color", font=("font-style", size))
text_label.pack()

# adding input box for email address
input_box = Entry(root, width="")
input_box.pack(ipady="height")

# adding a button
button = Button(root, text="text", fg="font-color", bg="color",)
button.pack()

root.mainloop()
