from tkinter import *
from tkinter import messagebox
from pathlib import Path
from PIL import ImageTk, Image

def handle_login():
    email = email_input.get().strip()
    password = password_input.get().strip()
    
    if not email or not password:
        return
    
    if "@gmail.com" in email:
        messagebox.showinfo("Success", "Login Successful")
    
    else:
        messagebox.showerror("Error", "Login Denied")

def setup_ui():

    global email_input, password_input


    text_label = Label(root, text="SIGN IN", font=("verdana", 15), fg="white", bg="#121212")
    text_label.pack(pady=(20, 20))

    email_label = Label(root, text="Username or Email", font=("verdana", 9), fg="white", bg="#121212")
    email_label.pack()
    email_input = Entry(root, width=33)
    email_input.pack(ipady=2, pady=(0,10))

    password_label = Label(root, text="Password", font=("verdana", 9), fg="white", bg="#121212", )
    password_label.pack()
    password_input = Entry(root, width=33, show="•")
    password_input.pack(ipady=2)

    login_btn = Button(root, text="LogIn", borderwidth=2, font=("verdana", 10), width=10, height=1, fg="#000000", command=handle_login)
    login_btn.pack(pady=(18,18))




root = Tk()

image_path = Path(__file__).parent / "login-image.png"
favicon_path = Path(__file__).parent / "favicon.ico"

root.title("Login Page")
root.iconbitmap(favicon_path)
root.configure(background="#121212")

root.geometry("350x500")
root.minsize(width=350, height=500)
root.maxsize(width=350, height=500)

original_image = Image.open(image_path)
img = ImageTk.PhotoImage(original_image.resize((100,100)))
img_label = Label(root, image=img)
img_label.pack(pady=(50,20))


setup_ui()
root.mainloop()