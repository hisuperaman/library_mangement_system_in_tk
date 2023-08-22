from tkinter import *
import login_admin
import login_librarian
from btn_hover import *
import check_availability
from PIL import Image, ImageTk
import os


def main_func():
    def closeWindowClick():
        if os.path.exists("currentlibid.txt"):
            os.remove("currentlibid.txt")
        if os.path.exists("currentadminusrname.txt"):
            os.remove("currentadminusrname.txt")
        root.destroy()

    def admin_login():
        """handling admin login event"""
        login_admin.main(root)


    def librarian_login():
        """handling librarian login event"""
        login_librarian.main(root)

    def avail_btnClick():
        check_availability.main(root)


    root = Tk()

    root.title("Library Management System")
    root.wm_iconbitmap(True, "library_icon.ico")
    width = 1150
    height = 600
    x = (root.winfo_screenwidth() - width)//2
    y = ((root.winfo_screenheight() - height)//2)-30
    root.geometry(f"{width}x{height}+{x}+{y}")
    root.resizable(0, 0)
    root.focus_force()

    bg_image = PhotoImage(file='images/home_page.png')
    bg = Label(root, image=bg_image).place(x=0, y=0)
    available_icon_img = Image.open('images/icons/available_icon.png').resize((30, 30))
    available_icon = ImageTk.PhotoImage(available_icon_img)

    admin_login_btn = Button(root, text="Admin Login", bg='#655bd6', fg='white', font=('Segoe UI', 13), borderwidth=0, width=18, command=admin_login)
    admin_login_btn.place(x=529, y=364)
    librarian_login_btn = Button(root, text="Librarian Login", bg='#655bd6', fg='white', font=('Segoe UI', 13), borderwidth=0, width=18, command=librarian_login)
    librarian_login_btn.place(x=783, y=364)
    avail_btn = Button(root, text=" Availability ", image=available_icon, compound='left', bg='#655bd6', fg='white', font=('Segoe UI', 18), borderwidth=0, width=170, command=avail_btnClick)
    avail_btn.place(x=972, y=481)

    admin_login_btn.bind('<Enter>', lambda e: btnMouseEnter(admin_login_btn))

    admin_login_btn.bind('<Leave>', lambda e: btnMouseLeave(admin_login_btn))
    librarian_login_btn.bind('<Enter>', lambda e: btnMouseEnter(librarian_login_btn))
    librarian_login_btn.bind('<Leave>', lambda e: btnMouseLeave(librarian_login_btn))
    avail_btn.bind('<Enter>', lambda e: btnMouseEnter(avail_btn))
    avail_btn.bind('<Leave>', lambda e: btnMouseLeave(avail_btn))


    root.protocol("WM_DELETE_WINDOW", closeWindowClick)

    root.mainloop()

if __name__=='__main__':
    main_func()