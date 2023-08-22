from tkinter import *
from tkinter import ttk
import backend
from treeview_functions import *
from btn_hover import *
from tkinter import messagebox

def main(root):
# def main():

  def queryClick(e):
    if squery.get()==default_squery:
      squery.set("")
      query.config(font=(fontUsed, 14, 'normal'), fg='black')

  def searchBtnClick():
    query_str = query.get()
    if query_str!="" and query_str!=default_squery:
      if len(query_str)>2:
        books_info = backend.get_books_by_query(query.get())
        current_rows = tv.get_children()
        for row in current_rows:
          tv.delete(row)
        for row in books_info:
          tv.insert(parent='', index='end', values=row)
      else:
        messagebox.showinfo("Query", "Enter at most 3 characters!", parent=win)
    else:
      messagebox.showinfo("Query", "Enter query first!", parent=win)

  def resetBtnClick():
    query.config(font=(fontUsed, 14, 'italic'), fg='grey')
    squery.set("search by book title, author, publisher")

    current_rows = tv.get_children()
    for row in current_rows:
      tv.delete(row)
    for row in rows:
      tv.insert(parent='', index='end', values=row)
    win.focus()

  fontUsed = "Segoe UI"
  
  win = Toplevel(root)
#   win = Tk()
  win.grab_set()
  win.focus()
  win.title("Check Available Books")
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
  rows = backend.show_avail_books()
  for row in rows:
    tv.insert(parent='', index='end', values=row)

  sb = ttk.Scrollbar(tv, orient='vertical')
  sb.config(command=tv.yview)
  tv.config(yscrollcommand=sb.set)
  sb.pack(side='right', fill='y')

  tv.place(x=0, y=60, width=width, height=height-60)


  squery = StringVar(value="search by book title, author, publisher")
  default_squery = squery.get()
  query = Entry(win, font=(fontUsed, 14, 'italic'), width=38, fg="grey", textvariable=squery)
  query.place(x=width/2-200,y=14)
  query.bind("<FocusIn>", queryClick)

  searchBtn = Button(win, text="Search", bg='#655bd6', fg='white', font=(fontUsed, 12), borderwidth=0, width=9, command=searchBtnClick)
  searchBtn.place(x=width/2+200,y=12)

  searchBtn.bind("<Enter>", lambda e: btnMouseEnter(searchBtn))
  searchBtn.bind("<Leave>", lambda e: btnMouseLeave(searchBtn))

  resetBtn = Button(win, text="Reset", bg='#655bd6', fg='white', font=(fontUsed, 11), borderwidth=0, width=8, command=resetBtnClick)
  resetBtn.place(x=width/2+300, y=13)

  resetBtn.bind("<Enter>", lambda e: btnMouseEnter(resetBtn))
  resetBtn.bind("<Leave>", lambda e: btnMouseLeave(resetBtn))
  


  win.mainloop()

# main()