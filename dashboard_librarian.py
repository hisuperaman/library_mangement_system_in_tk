from tkinter import *
import add_student
import delete_student
import edit_student
import add_book_page
import delete_book_page
import edit_book_page
import search_book_page
import issue_book_page
import return_book_page
import show_students
import show_books
import show_issued_ret_books
import edit_fine_page
from btn_hover import *
from PIL import Image, ImageTk
import backend
import os


# def main():
def main(root):
    fontUsed = "Reem Kufi"

    def closeWindowClick():
        if os.path.exists("currentlibid.txt"):
            os.remove("currentlibid.txt")
        if os.path.exists("currentadminusrname.txt"):
            os.remove("currentadminusrname.txt")
        root.destroy()


    def student_add():
        add_student.main(root)

    def student_delete():
        delete_student.main(root)

    def student_edit():
        edit_student.main(root)

    def book_add():
        add_book_page.main(root)

    def book_delete():
        delete_book_page.main(root)

    def book_edit():
        edit_book_page.main(root)

    def book_search():
        search_book_page.main(root)

    def book_issue():
        issue_book_page.main(root)

    def book_return():
        return_book_page.main(root)

    def book_issued_show():
        show_issued_ret_books.main(root)

    def students_show():
        show_students.main(root)

    def books_show():
        show_books.main(root)

    def fine_edit():
        edit_fine_page.main(root)

    def logoutBtnClick():
        win.destroy()
        root.deiconify()
        
    win = Toplevel(root)
    # win = Tk()
    win.grab_set()
    win.focus_force()
    
    win.title("Librarian Dashboard")
    width = 1150
    height = 600
    x = (win.winfo_screenwidth() - width)//2
    y = ((win.winfo_screenheight() - height)//2)-30
    win.geometry(f"{width}x{height}+{x}+{y}")
    win.resizable(0, 0)

    bg_image = PhotoImage(file='images/dashboard_librarian.png')
    bg = Label(win, image=bg_image).place(x=0, y=0)

    add_std = Button(win, text="Add Student", bg='#655bd6', fg='white', font=('Segoe UI', 14), borderwidth=0, width=10, command=student_add)
    add_std.place(x=372, y=200)
    del_std = Button(win, text="Delete Student", bg='#655bd6', fg='white', font=('Segoe UI', 13), borderwidth=0, width=12, command=student_delete)
    del_std.place(x=520, y=202)
    edit_std = Button(win, text="Edit Student", bg='#655bd6', fg='white', font=('Segoe UI', 14), borderwidth=0, width=10, command=student_edit)
    edit_std.place(x=680, y=202)
    show_std = Button(win, text="Show Students", bg='#655bd6', fg='white', font=('Segoe UI', 13), borderwidth=0, width=12, command=students_show)
    show_std.place(x=830, y=205)

    add_std.bind("<Enter>", lambda e: btnMouseEnter(add_std))
    add_std.bind("<Leave>", lambda e: btnMouseLeave(add_std))
    del_std.bind("<Enter>", lambda e: btnMouseEnter(del_std))
    del_std.bind("<Leave>", lambda e: btnMouseLeave(del_std))
    edit_std.bind("<Enter>", lambda e: btnMouseEnter(edit_std))
    edit_std.bind("<Leave>", lambda e: btnMouseLeave(edit_std))
    show_std.bind("<Enter>", lambda e: btnMouseEnter(show_std))
    show_std.bind("<Leave>", lambda e: btnMouseLeave(show_std))

    add_book = Button(win, text="Add Book", bg='#655bd6', fg='white', font=('Segoe UI', 14), borderwidth=0, width=11, command=book_add)
    add_book.place(x=367, y=338)
    del_book = Button(win, text="Delete Book", bg='#655bd6', fg='white', font=('Segoe UI', 13), borderwidth=0, width=12, command=book_delete)
    del_book.place(x=522, y=340)
    edit_book = Button(win, text="Edit Book", bg='#655bd6', fg='white', font=('Segoe UI', 14), borderwidth=0, width=10, command=book_edit)
    edit_book.place(x=682, y=338)
    show_book = Button(win, text="Show Books", bg='#655bd6', fg='white', font=('Segoe UI', 13), borderwidth=0, width=12, command=books_show)
    show_book.place(x=830, y=340)

    add_book.bind("<Enter>", lambda e: btnMouseEnter(add_book))
    add_book.bind("<Leave>", lambda e: btnMouseLeave(add_book))
    del_book.bind("<Enter>", lambda e: btnMouseEnter(del_book))
    del_book.bind("<Leave>", lambda e: btnMouseLeave(del_book))
    edit_book.bind("<Enter>", lambda e: btnMouseEnter(edit_book))
    edit_book.bind("<Leave>", lambda e: btnMouseLeave(edit_book))
    show_book.bind("<Enter>", lambda e: btnMouseEnter(show_book))
    show_book.bind("<Leave>", lambda e: btnMouseLeave(show_book))

    issue_book = Button(win, text="Issue Book", bg='#655bd6', fg='white', font=('Segoe UI', 14), borderwidth=0, width=11, command=book_issue)
    issue_book.place(x=366, y=475)
    return_book = Button(win, text="Return Book", bg='#655bd6', fg='white', font=('Segoe UI', 13), borderwidth=0, width=12, command=book_return)
    return_book.place(x=524, y=475)
    search_book = Button(win, text="Search Book", bg='#655bd6', fg='white', font=('Segoe UI', 14), borderwidth=0, width=10, command=book_search)
    search_book.place(x=682, y=475)
    issued_books = Button(win, text="Issued Books", bg='#655bd6', fg='white', font=('Segoe UI', 13), borderwidth=0, width=12, command=book_issued_show)
    issued_books.place(x=831, y=476)
    edit_fine = Button(win, text="Edit Fine   ",  bg='#655bd6', fg='white', font=('Segoe UI', 15), borderwidth=0, width=11, command=fine_edit)
    edit_fine.place(x=1010, y=398)

    issue_book.bind("<Enter>", lambda e: btnMouseEnter(issue_book))
    issue_book.bind("<Leave>", lambda e: btnMouseLeave(issue_book))
    return_book.bind("<Enter>", lambda e: btnMouseEnter(return_book))
    return_book.bind("<Leave>", lambda e: btnMouseLeave(return_book))
    search_book.bind("<Enter>", lambda e: btnMouseEnter(search_book))
    search_book.bind("<Leave>", lambda e: btnMouseLeave(search_book))
    issued_books.bind("<Enter>", lambda e: btnMouseEnter(issued_books))
    issued_books.bind("<Leave>", lambda e: btnMouseLeave(issued_books))
    edit_fine.bind("<Enter>", lambda e: btnMouseEnter(edit_fine))
    edit_fine.bind("<Leave>", lambda e: btnMouseLeave(edit_fine))

    logout_iconImg = Image.open('images/icons/logout_icon.png').resize((40, 40))
    logout_icon = ImageTk.PhotoImage(logout_iconImg)

    logoutBtn = Button(win, text="Logout       ", image=logout_icon, compound=RIGHT, bg='#655bd6', fg='white', font=('Segoe UI', 15), borderwidth=0, width=158, command=logoutBtnClick)
    logoutBtn.place(x=977, y=476)

    logoutBtn.bind("<Enter>", lambda e: btnMouseEnter(logoutBtn))
    logoutBtn.bind("<Leave>", lambda e: btnMouseLeave(logoutBtn))


    pfp_frame = Frame(win, bg="#655bd6")
  
    pfp_label = Label(pfp_frame)


    with open("currentlibid.txt", "r") as f:
        libID = f.read()

    # print(libID) 
    
    pfp_path = backend.get_librarian_pfp(libID)
    pfp_path = pfp_path[0]
    if pfp_path!=None:
        pfp_frame.place(x=96, y=148)
        img = Image.open(pfp_path).resize((150, 150), Image.Resampling.LANCZOS)
        img = ImageTk.PhotoImage(img)
        pfp_label.config(image=img)
        pfp_label.image = img
        pfp_label.pack()

    librarian_info = backend.search_librarian(libID)
    lib_name = librarian_info[1]+" "+librarian_info[2]
    lib_name_label = Label(win, text=lib_name, bg="#a8b9ff", fg="#3f48cc" ,font=(fontUsed, 22, 'underline'))
    lib_name_label.place(x=18, y=302)        

    lib_username = librarian_info[8]
    lib_username_label = Label(win, text=lib_username, bg="#a8b9ff", fg="#3f48cc" ,font=("Segoe UI", 18, 'underline'))
    lib_username_label.place(x=152, y=358)    

    lib_email = librarian_info[5]
    lib_email_label = Label(win, text=lib_email, bg="#a8b9ff", fg="#3f48cc" ,font=("Segoe UI", 14, 'underline'))    
    lib_email_label.place(x=20, y=430)        

    # destroying main window when this toplevel closes
    win.protocol("WM_DELETE_WINDOW", closeWindowClick)
    
    win.mainloop()


# main()