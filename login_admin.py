from tkinter import *
from tkinter import messagebox
import dashboard_admin
import backend
from btn_hover import *


def main(root):
    def admin_dashboard():
        """opening dashboard when admin logs in"""
        if (username.get()!="" and password.get()!=""):
            admin_details = backend.admin_info(username.get())
            if admin_details!=None:
                if admin_details[0]==username.get() and admin_details[1]==password.get():
                        with open("currentadminusrname.txt", "w") as f:
                            f.write(str(admin_details[0]))
                        root.withdraw()
                        win.destroy()
                        dashboard_admin.main(root)
                else:
                    messagebox.showerror("Invalid info", "Incorrect password!", parent=win)
            else:
                messagebox.showerror("Invalid info", "Username does not exist!", parent=win)
        else:
            messagebox.showinfo("Inputs", "Input fields must not be empty!", parent=win)
    

    win = Toplevel(root)
    # win = Tk()
    win.grab_set()
    win.focus()
    win.title("Admin Login")
    width = 700
    height = 550
    x = ((win.winfo_screenwidth() - width)//2)-30
    y = ((win.winfo_screenheight() - height)//2)-30
    win.geometry(f"{width}x{height}+{x}+{y}")
    win.resizable(0, 0)

    bg_image = PhotoImage(file='images/login_admin.png')
    bg = Label(win, image=bg_image).place(x=0, y=0)

    username = Entry(win, width=20, font=('Segoe UI', 15), borderwidth=1)
    username.place(x=310, y=215)
    password = Entry(win, width=20, font=('Segoe UI', 15), borderwidth=1, show='*')
    password.place(x=310, y=305)

    login_btn = Button(win, text="Login", bg='#655bd6', fg='white', font=('Segoe UI', 13), borderwidth=0, width=9, command=admin_dashboard)
    login_btn.place(x=312, y=366)

    login_btn.bind("<Enter>", lambda e: btnMouseEnter(login_btn))
    login_btn.bind("<Leave>", lambda e: btnMouseLeave(login_btn))

    win.mainloop()

# main()
