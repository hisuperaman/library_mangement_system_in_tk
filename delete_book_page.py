from tkinter import *
import delete_new_book
import delete_book_copies
from btn_hover import *


def main(root):
# def main():
  def delBookBtnClick():
    win.destroy()
    delete_new_book.main(root)

  def delCopyBtnClick():
    win.destroy()
    delete_book_copies.main(root)

  fontUsed = "Segoe UI"

  win = Toplevel(root)
#   win = Tk()
  win.grab_set()
  win.focus()
  win.title("Delete Book Page")
  width = 500
  height = 250
  x = ((win.winfo_screenwidth() - width)//2)
  y = ((win.winfo_screenheight() - height)//2)-60
  win.geometry(f"{width}x{height}+{x}+{y}")
  win.resizable(0, 0)
  bgimage=PhotoImage(file="images/delete_book_page.png") 
  bg=Label(win, image=bgimage)
  bg.place(x=0,y=0)

  
  delBookBtn = Button(win, text="Del New Book", bg='#655bd6', fg='white', font=(fontUsed, 18), borderwidth=0, width=15, command=delBookBtnClick)
  delBookBtn.place(x=28,y=170)

  delCopyBtn = Button(win, text="Del Book Copies", bg='#655bd6', fg='white', font=(fontUsed, 18), borderwidth=0, width=15, command=delCopyBtnClick)
  delCopyBtn.place(x=272,y=171)

  delBookBtn.bind("<Enter>", lambda e: btnMouseEnter(delBookBtn))
  delBookBtn.bind("<Leave>", lambda e: btnMouseLeave(delBookBtn))
  delCopyBtn.bind("<Enter>", lambda e: btnMouseEnter(delCopyBtn))
  delCopyBtn.bind("<Leave>", lambda e: btnMouseLeave(delCopyBtn))

  win.mainloop()

# main()