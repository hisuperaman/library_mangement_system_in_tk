from tkinter import *
from tkinter import ttk
import backend
from btn_hover import *
from treeview_functions import *


def main(root):
# def main():
  fontUsed = "Segoe UI"
  
  win = Toplevel(root)
#   win = Tk()
  win.grab_set()
  win.focus_force()
  win.title("Show Issued Books")
  width = root.winfo_width()
  height = root.winfo_height()
  x = ((win.winfo_screenwidth() - width)//2)
  y = ((win.winfo_screenheight() - height)//2)-30
  win.geometry(f"{width}x{height}+{x}+{y}")
  win.resizable(0, 0)
  # win.config(bg="#655bd6")

  tv = ttk.Treeview(win)

  # specify columns, where each element in tuple is treeViewID
  tv['columns'] = ('book_id', 'sid', 'issue_date', 'due_date')

  # format columns using treeViewID
  # column with #0ID is a ghost column
  tv.column('#0', width=-30, minwidth=0)
  tv.column('book_id', width=10, minwidth=5)
  tv.column('sid', width=40, minwidth=40)
  tv.column('issue_date', width=40, minwidth=20)
  tv.column('due_date', width=40, minwidth=20)

  # specify headings to columns
  tv.heading('book_id', text="BookID")
  tv.heading('sid', text="SID")
  tv.heading('issue_date', text="IssueDate")
  tv.heading('due_date', text="DueDate")

  # inserting data into treeView
  rows = backend.show_issued_books()
  for row in rows:
    tv.insert(parent='', index='end', values=row)

  sb = ttk.Scrollbar(tv, orient='vertical')
  sb.config(command=tv.yview)
  tv.config(yscrollcommand=sb.set)
  sb.pack(side='right', fill='y')


  tv.place(x=0, y=0, width=width, height=height-40)

  headingRow = ['BookID', 'SID', 'IssueDate', 'DueDate']
  saveBtn = Button(win, text="Save", bg='#655bd6', fg='white', font=(fontUsed, 13), borderwidth=0, width=8, command=lambda: saveBtnClick(win, headingRow, rows, "issued_books"))
  saveBtn.place(x=(width/2)-25, y=height-40)

  saveBtn.bind("<Enter>", lambda e: btnMouseEnter(saveBtn))
  saveBtn.bind("<Leave>", lambda e: btnMouseLeave(saveBtn))


  win.mainloop()

# main()