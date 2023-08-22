from tkinter import *
from tkinter import ttk
import backend
from btn_hover import *
from treeview_functions import *


def main(root):
# def main():
  fontUsed = "Segoe UI"
  
  win = Toplevel(root)
  # win = Tk()
  win.grab_set()
  win.focus()
  win.title("Show Librarians")
  width = root.winfo_width()
  height = root.winfo_height()
  x = ((win.winfo_screenwidth() - width)//2)
  y = ((win.winfo_screenheight() - height)//2)-30
  win.geometry(f"{width}x{height}+{x}+{y}")
  win.resizable(0, 0)
  # win.config(bg="#655bd6")

  tv = ttk.Treeview(win)

  # specify columns, where each element in tuple is treeViewID
  tv['columns'] = ('lib_id', 'fname', 'lname', 'gen', 'dob', 'email', 'phno', 'lib_address', 'lib_user', 'lib_pass')

  # format columns using treeViewID
  # column with #0ID is a ghost column
  tv.column('#0', width=-30, minwidth=0)
  tv.column('lib_id', width=10, minwidth=5)
  tv.column('fname', width=40, minwidth=20)
  tv.column('lname', width=40, minwidth=20)
  tv.column('gen', width=14, minwidth=10)
  tv.column('dob', width=40, minwidth=20)
  tv.column('email', width=40, minwidth=20)
  tv.column('phno', width=40, minwidth=20)
  tv.column('lib_address', width=40, minwidth=20)
  tv.column('lib_user', width=40, minwidth=20)
  tv.column('lib_pass', width=40, minwidth=20)

  # specify headings to columns
  tv.heading('lib_id', text="LibID")
  tv.heading('fname', text="fname")
  tv.heading('lname', text="lname")
  tv.heading('gen', text="Gender")
  tv.heading('dob', text="DOB")
  tv.heading('email', text="Email")
  tv.heading('phno', text="PhNo")
  tv.heading('lib_address', text="Address")
  tv.heading('lib_user', text="Username")
  tv.heading('lib_pass', text="Password")

  # inserting data into treeView
  rows = backend.show_librarians()
  for row in rows:
    tv.insert(parent='', index='end', values=row)

  sb = ttk.Scrollbar(tv, orient='vertical')
  sb.config(command=tv.yview)
  tv.config(yscrollcommand=sb.set)
  sb.pack(side='right', fill='y')

  tv.place(x=0, y=0, width=width, height=height-40)

  headingRow = ['LibID', 'fname', 'lname', 'Gender', 'DOB', 'Email', 'PhNo', 'Address', 'Username', 'Password']
  saveBtn = Button(win, text="Save", bg='#655bd6', fg='white', font=(fontUsed, 13), borderwidth=0, width=8, command=lambda: saveBtnClick(win, headingRow, rows, "librarians"))
  saveBtn.place(x=(width/2)-25, y=height-40)

  saveBtn.bind("<Enter>", lambda e: btnMouseEnter(saveBtn))
  saveBtn.bind("<Leave>", lambda e: btnMouseLeave(saveBtn))


  win.mainloop()

# main()