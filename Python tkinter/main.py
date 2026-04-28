from tkinter import *                       # for GUIs
from pathlib import Path                    # for image path problem
from PIL import ImageTk, Image              # to display image on screen

root = Tk()

# title
root.title("Login Window")

# manipualting the size of GUI 
root.minsize(300,300)
root.geometry("400x500")

# creating a variable for path of image 
icon_path = Path(__file__).parent/"star.ico"
root.iconbitmap(icon_path)

# changing background color
root.configure(background="black")

# resizing the image 
original_image = Image.open(icon_path)
resized_image = original_image.resize((100,100))

# displaying image on screen
# img = ImageTk.PhotoImage(Image.open(icon_path))
img = ImageTk.PhotoImage(resized_image)
image_label = Label(root, image=img)
# changing the positiion of image 
image_label.pack(pady=(50,20))

# adding text to screen
text_label = Label(root, text="Hello", fg="white", bg="black", font=("verdana", 18))
text_label.pack()

# adding input box for email address
email_label = Label(root, text="enter email", fg="white", bg="black", font=("verdana", 9))
email_label.pack(pady=(50,10))
email_input = Entry(root, width="30")
email_input.pack(ipady="4")

# adding input box for password
password_label = Label(root, text="enter password", fg="white", bg="black", font=("verdana", 9))
password_label.pack(pady=(10,10))
password_input = Entry(root, width="30")
password_input.pack(ipady=4)

root.mainloop()
