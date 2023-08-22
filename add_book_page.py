from tkinter import *
import add_new_book
import add_book_copies
from btn_hover import *


def main(root):
# def main():
  def addBookBtnClick():
    win.destroy()
    add_new_book.main(root)

  def addCopyBtnClick():
    win.destroy()
    add_book_copies.main(root)

  fontUsed = "Segoe UI"

  win = Toplevel(root)
#   win = Tk()
  win.grab_set()
  win.focus()
  win.title("Add Book Page")
  width = 500
  height = 250
  x = ((win.winfo_screenwidth() - width)//2)
  y = ((win.winfo_screenheight() - height)//2)-60
  win.geometry(f"{width}x{height}+{x}+{y}")
  win.resizable(0, 0)
  bgimage=PhotoImage(file="images/add_book_page.png") 
  bg=Label(win, image=bgimage)
  bg.place(x=0,y=0)

  
  addBookBtn = Button(win, text="Add New Book", bg='#655bd6', fg='white', font=(fontUsed, 18), borderwidth=0, width=15, command=addBookBtnClick)
  addBookBtn.place(x=28,y=170)

  addCopyBtn = Button(win, text="Add Book Copies", bg='#655bd6', fg='white', font=(fontUsed, 18), borderwidth=0, width=15, command=addCopyBtnClick)
  addCopyBtn.place(x=272,y=171)

  addBookBtn.bind("<Enter>", lambda e: btnMouseEnter(addBookBtn))
  addBookBtn.bind("<Leave>", lambda e: btnMouseLeave(addBookBtn))
  addCopyBtn.bind("<Enter>", lambda e: btnMouseEnter(addCopyBtn))
  addCopyBtn.bind("<Leave>", lambda e: btnMouseLeave(addCopyBtn))

  win.mainloop()

# main()