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
  win.focus()
  win.title("Show Students")
  width = root.winfo_width()
  height = root.winfo_height()
  x = ((win.winfo_screenwidth() - width)//2)
  y = ((win.winfo_screenheight() - height)//2)-30
  win.geometry(f"{width}x{height}+{x}+{y}")
  win.resizable(0, 0)
  # win.config(bg="white")

  tv = ttk.Treeview(win)

  # specify columns, where each element in tuple is treeViewID
  tv['columns'] = ('sid', 'fname', 'lname', 'gen', 'dob', 'father_name', 'email', 'phno', 'address')

  # format columns using treeViewID
  # column with #0ID is a ghost column
  tv.column('#0', width=-30, minwidth=0)
  tv.column('sid', width=10, minwidth=5)
  tv.column('fname', width=40, minwidth=20)
  tv.column('lname', width=40, minwidth=20)
  tv.column('gen', width=14, minwidth=10)
  tv.column('dob', width=40, minwidth=20)
  tv.column('father_name', width=40, minwidth=20)
  tv.column('email', width=40, minwidth=20)
  tv.column('phno', width=40, minwidth=20)
  tv.column('address', width=40, minwidth=20)

  # specify headings to columns
  tv.heading('sid', text="SID")
  tv.heading('fname', text="fname")
  tv.heading('lname', text="lname")
  tv.heading('gen', text="Gender")
  tv.heading('dob', text="DOB")
  tv.heading('father_name', text="father_name")
  tv.heading('email', text="Email")
  tv.heading('phno', text="PhNo")
  tv.heading('address', text="Address")

  # inserting data into treeView
  rows = backend.show_students()
  for row in rows:
    tv.insert(parent='', index='end', values=row)

  sb = ttk.Scrollbar(tv, orient='vertical')
  sb.config(command=tv.yview)
  tv.config(yscrollcommand=sb.set)
  sb.pack(side='right', fill='y')

  tv.place(x=0, y=0, width=width, height=height-40)


  headingRow = ['sid', 'fname', 'lname', 'gen', 'dob', 'father_name', 'email', 'phno', 'address']
  saveBtn = Button(win, text="Save", bg='#655bd6', fg='white', font=(fontUsed, 13), borderwidth=0, width=8, command=lambda: saveBtnClick(win, headingRow, rows, "students"))
  saveBtn.place(x=(width/2)-25, y=height-40)

  saveBtn.bind("<Enter>", lambda e: btnMouseEnter(saveBtn))
  saveBtn.bind("<Leave>", lambda e: btnMouseLeave(saveBtn))
  


  win.mainloop()

# main()