from future.moves.tkinter import *
from tkinter import messagebox
from PIL import ImageTk     # install Pillow


class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("User Login")
        self.root.geometry("1350x700+0+0")

        # **************** All Images **************** #
        self.bg_icon = ImageTk.PhotoImage(file="E:/dell/Python/Temp/login/bg4.jpg")
        self.user_icon = ImageTk.PhotoImage(file="E:/dell/Python/Temp/login/username.png")
        self.password_icon = ImageTk.PhotoImage(file="E:/dell/Python/Temp/login/password.png")
        self.logo_icon = ImageTk.PhotoImage(file="E:/dell/Python/Temp/login/logo1.jpg")

        # **************** All Variables **************** #
        self.username = StringVar()
        self.password = StringVar()

        # Background Image
        bg_image = Label(self.root, image=self.bg_icon)
        bg_image.pack()

        # Title
        title = Label(self.root, text="Login System", font=("impact", 30, "bold"), bg="#273746", fg="white", bd=10,
                      relief=GROOVE)
        title.place(x=0, y=0, relwidth=1)

        # Login Frame
        Login_Frame = Frame(self.root, bd=5, bg="white")
        Login_Frame.place(x=400, y=150, width=500, height=350)

        # Logo
        logo_lbl = Label(Login_Frame, image=self.logo_icon, bd=0)
        logo_lbl.grid(row=0, columnspan=2, pady=20)

        # User
        username_lbl = Label(Login_Frame, text="Username", image=self.user_icon, compound=LEFT,
                             font=("times new roman", 20, "bold"), bg="white")
        username_lbl.grid(row=1, column=0, padx=20, pady=10)
        username_txt = Entry(Login_Frame, textvariable=self.username, bd=5, relief=GROOVE, font=("", 15))
        username_txt.grid(row=1, column=1, padx=20, pady=10)

        # Password
        password_lbl = Label(Login_Frame, text=" Passsord", image=self.password_icon, compound=LEFT,
                             font=("times new roman", 20, "bold"), bg="white")
        password_lbl.grid(row=2, column=0, padx=20, pady=10)
        user_txt = Entry(Login_Frame, textvariable=self.password, bd=5, relief=GROOVE, show="*", font=("", 15))
        user_txt.grid(row=2, column=1, padx=20, pady=10)

        # Login Button
        btn = Button(Login_Frame, text="Login", width=15, command=self.login, font=("times new roman", 14, "bold"),
                     bg="#BFC9CA", fg="black")
        btn.grid(row=3, columnspan=2, padx=20, pady=10)

    def login(self):
        if self.username.get() == "" or self.password.get() == "":
            messagebox.showerror("Error !", "All fields are required!")
        elif self.username.get() == "imkevin12" and self.password.get() == "12345":
            messagebox.showinfo("Successfull !", f"Welcome to KEVIN WORLD !")
        else:
            messagebox.showerror("Oops !", "Invalid username or password!")


root = Tk()
obj = Login(root)
root.mainloop()
