from tkinter import *
import add_librarian
import delete_librarian
import edit_librarian
import show_librarians
import change_admin_info
from btn_hover import *
from PIL import Image, ImageTk
import os


# def main():
def main(root):
    def closeWindowClick():
        if os.path.exists("currentlibid.txt"):
            os.remove("currentlibid.txt")
        if os.path.exists("currentadminusrname.txt"):
            os.remove("currentadminusrname.txt")
        root.destroy()

    def librarian_add():
        add_librarian.main(root)
    def librarian_delete():
        delete_librarian.main(root)
    def librarian_edit():
        edit_librarian.main(root)
    def librarians_show():
        show_librarians.main(root)
    def login_info_change():
        change_admin_info.main(root)
    def logoutBtnClick():
        win.destroy()
        root.deiconify()

    win = Toplevel(root)
    # win = Tk()
    win.grab_set()
    win.focus_force()
    
    win.title("Admin Dashboard")
    width = 1150
    height = 600
    x = (root.winfo_screenwidth() - width)//2
    y = ((root.winfo_screenheight() - height)//2)-30
    win.geometry(f"{width}x{height}+{x}+{y}")
    # win.geometry(f"{width}x{height}")
    win.resizable(0, 0)

    bg_image = PhotoImage(file='images/dashboard_admin.png')
    bg = Label(win, image=bg_image).place(x=0, y=0)

    add_lib = Button(win, text="Add Librarian", bg='#655bd6', fg='white', font=('Segoe UI', 12), borderwidth=0, width=14, command=librarian_add)
    add_lib.place(x=394, y=265)
    edit_lib = Button(win, text="Edit Librarian", bg='#655bd6', fg='white', font=('Segoe UI', 12), borderwidth=0, width=14, command=librarian_edit)
    edit_lib.place(x=578, y=265)
    show_lib = Button(win, text="Show Librarians", bg='#655bd6', fg='white', font=('Segoe UI', 12), borderwidth=0, width=14, command=librarians_show)
    show_lib.place(x=396, y=433)
    del_lib = Button(win, text="Delete Librarian", bg='#655bd6', fg='white', font=('Segoe UI', 12), borderwidth=0, width=14, command=librarian_delete)
    del_lib.place(x=577, y=433)
    login_info_lib = Button(win, text="Login Info", bg='#655bd6', fg='white', font=('Segoe UI', 12), borderwidth=0, width=14, command=login_info_change)
    login_info_lib.place(x=765, y=265)

    logout_iconImg = Image.open('images/icons/logout_icon.png').resize((40, 40))
    logout_icon = ImageTk.PhotoImage(logout_iconImg)

    logoutBtn = Button(win, text="Logout       ", image=logout_icon, compound=RIGHT, bg='#655bd6', fg='white', font=('Segoe UI', 15), borderwidth=0, width=158, command=logoutBtnClick)
    logoutBtn.place(x=977, y=476)

    add_lib.bind("<Enter>", lambda e: btnMouseEnter(add_lib))
    add_lib.bind("<Leave>", lambda e: btnMouseLeave(add_lib))
    del_lib.bind("<Enter>", lambda e: btnMouseEnter(del_lib))
    del_lib.bind("<Leave>", lambda e: btnMouseLeave(del_lib))
    edit_lib.bind("<Enter>", lambda e: btnMouseEnter(edit_lib))
    edit_lib.bind("<Leave>", lambda e: btnMouseLeave(edit_lib))
    show_lib.bind("<Enter>", lambda e: btnMouseEnter(show_lib))
    show_lib.bind("<Leave>", lambda e: btnMouseLeave(show_lib))
    login_info_lib.bind("<Enter>", lambda e: btnMouseEnter(login_info_lib))
    login_info_lib.bind("<Leave>", lambda e: btnMouseLeave(login_info_lib))
    logoutBtn.bind("<Enter>", lambda e: btnMouseEnter(logoutBtn))
    logoutBtn.bind("<Leave>", lambda e: btnMouseLeave(logoutBtn))
    
    # destroying main window when this toplevel closes
    win.protocol("WM_DELETE_WINDOW", closeWindowClick)
    win.mainloop()


# main()