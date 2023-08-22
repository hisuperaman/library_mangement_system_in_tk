from tkinter import *
from tkinter import ttk
import backend
from treeview_functions import *
from btn_hover import *


def main(root):
# def main():
  fontUsed = "Segoe UI"
  
  win = Toplevel(root)
#   win = Tk()
  win.grab_set()
  win.focus()
  win.title("Show Books")
  width = root.winfo_width()
  height = root.winfo_height()
  x = ((win.winfo_screenwidth() - width)//2)
  y = ((win.winfo_screenheight() - height)//2)-30
  win.geometry(f"{width}x{height}+{x}+{y}")
  win.resizable(0, 0)
  # win.config(bg="#655bd6")

  tv = ttk.Treeview(win)

  # specify columns, where each element in tuple is treeViewID
  tv['columns'] = ('book_id', 'isbn', 'title', 'author', 'publisher', 'edition', 'avail_copies', 'issued_copies', 'total_copies')

  # format columns using treeViewID
  # column with #0ID is a ghost column
  tv.column('#0', width=-30, minwidth=0)
  tv.column('book_id', width=10, minwidth=5)
  tv.column('isbn', width=40, minwidth=20)
  tv.column('title', width=40, minwidth=20)
  tv.column('author', width=40, minwidth=20)
  tv.column('publisher', width=40, minwidth=40)
  tv.column('edition', width=40, minwidth=20)
  tv.column('avail_copies', width=40, minwidth=20)
  tv.column('issued_copies', width=40, minwidth=20)
  tv.column('total_copies', width=40, minwidth=20)

  # specify headings to columns
  tv.heading('book_id', text="BookID")
  tv.heading('isbn', text="ISBN")
  tv.heading('title', text="Title")
  tv.heading('author', text="Author")
  tv.heading('publisher', text="Publisher")
  tv.heading('edition', text="Edition")
  tv.heading('avail_copies', text="AvailCopies")
  tv.heading('issued_copies', text="IssuedCopies")
  tv.heading('total_copies', text="TotalCopies")

  # inserting data into treeView
  rows = backend.show_books()
  for row in rows:
    tv.insert(parent='', index='end', values=row)

  sb = ttk.Scrollbar(tv, orient='vertical')
  sb.config(command=tv.yview)
  tv.config(yscrollcommand=sb.set)
  sb.pack(side='right', fill='y')

  tv.place(x=0, y=0, width=width, height=height-40)

  headingRow = ['BookID', 'ISBN', 'Title', 'Author', 'Publisher', 'Edition', 'AvailCopies', 'IssuedCopies', 'TotalCopies']
  saveBtn = Button(win, text="Save", bg='#655bd6', fg='white', font=(fontUsed, 13), borderwidth=0, width=8, command=lambda: saveBtnClick(win, headingRow, rows, "books"))
  saveBtn.place(x=(width/2)-25, y=height-40)

  saveBtn.bind("<Enter>", lambda e: btnMouseEnter(saveBtn))
  saveBtn.bind("<Leave>", lambda e: btnMouseLeave(saveBtn))


  win.mainloop()

# main()