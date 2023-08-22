from tkinter import *
from btn_hover import *
import show_issued_books
import show_returned_books


def main(root):
# def main():
  def issuedBtnClick():
    win.destroy()
    show_issued_books.main(root)

  def returnedBtnClick():
    win.destroy()
    show_returned_books.main(root)

  fontUsed = "Segoe UI"

  win = Toplevel(root)
#   win = Tk()
  win.grab_set()
  win.focus()
  win.title("Show Issued/Returned Books")
  width = 500
  height = 250
  x = ((win.winfo_screenwidth() - width)//2)
  y = ((win.winfo_screenheight() - height)//2)-60
  win.geometry(f"{width}x{height}+{x}+{y}")
  win.resizable(0, 0)
  bgimage=PhotoImage(file="images/show_issue_ret_books.png") 
  bg=Label(win, image=bgimage)
  bg.place(x=0,y=0)

  
  issuedBtn = Button(win, text="Show Issued Books", bg='#655bd6', fg='white', font=(fontUsed, 16), borderwidth=0, width=16, command=issuedBtnClick)
  issuedBtn.place(x=30,y=172)

  returnedBtn = Button(win, text="Show Returned Books", bg='#655bd6', fg='white', font=(fontUsed, 15), borderwidth=0, width=18, command=returnedBtnClick)
  returnedBtn.place(x=270,y=175)

  issuedBtn.bind("<Enter>", lambda e: btnMouseEnter(issuedBtn))
  issuedBtn.bind("<Leave>", lambda e: btnMouseLeave(issuedBtn))
  returnedBtn.bind("<Enter>", lambda e: btnMouseEnter(returnedBtn))
  returnedBtn.bind("<Leave>", lambda e: btnMouseLeave(returnedBtn))

  win.mainloop()

# main()