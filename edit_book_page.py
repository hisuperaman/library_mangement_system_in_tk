from tkinter import *
from tkinter import messagebox
import backend
from btn_hover import *


def main(root):
# def main():
  fontUsed = "Segoe UI"
  def editBtnClick():
    if isbn.get()!='' and book_title.get()!='' and author.get()!='' and publisher.get()!='' and edition.get()!='':
      try:
        backend.edit_book(bookID.get(), isbn.get(), book_title.get(), author.get(), publisher.get(), edition.get())
        messagebox.showinfo("Done", "Book edited successfully!", parent=win)
        win.destroy()
      except Exception as e:
        if not (isbn.get().isnumeric()):
          messagebox.showinfo("ISBN", "ISBN must be a number!", parent=win)
        else:
          messagebox.showerror("Error", "Something went wrong!", parent=win)
    else:
      messagebox.showinfo("Search", "Search the book first!", parent=win)

  def searchBtnClick():
    if bookID.get()!='':
      if bookID.get().isnumeric():
        entries = backend.search_book(bookID.get())
        if entries!=None:
          bookID.config(state='disabled')

          bookID.config(state='disabled')
          isbn.config(state='normal')
          book_title.config(state='normal')
          author.config(state='normal')
          publisher.config(state='normal')
          edition.config(state='normal')

          i = 0
          for key in strEntries.keys():
            strEntries[key].set(entries[i])
            i+=1
        else:
          isbn.config(state='disabled')
          book_title.config(state='disabled')
          author.config(state='disabled')
          publisher.config(state='disabled')
          edition.config(state='disabled')

          messagebox.showerror("Not found", "Specified BookID not found!", parent=win)
          for key in strEntries.keys():
            strEntries[key].set('')
      else:
        messagebox.showinfo("BookID", "BookID must be a number!", parent=win)
    else:
      messagebox.showinfo("BookID", "Enter bookID first!", parent=win)

  def resetBtnClick():
    sbookID.set("")
    bookID.config(state='normal')
    isbn.config(state='disabled')
    book_title.config(state='disabled')
    author.config(state='disabled')
    publisher.config(state='disabled')
    edition.config(state='disabled')
    bookID.config(state='normal')
    for key in strEntries.keys():
      strEntries[key].set("")
    win.focus()


  win = Toplevel(root)
  # win = Tk()
  strEntries={"sisbn": StringVar(), "stitle": StringVar(), "sauthor": StringVar(), "spublisher": StringVar(), "sedition": StringVar()}

  win.grab_set()
  win.focus()
  win.title("Edit Existing Book")
  width = 700
  height = 550
  x = ((win.winfo_screenwidth() - width)//2)-30
  y = ((win.winfo_screenheight() - height)//2)-30
  win.geometry(f"{width}x{height}+{x}+{y}")
  win.resizable(0, 0)
  bgimage=PhotoImage(file="images/edit_book.png") 
  bg=Label(win, image=bgimage)
  bg.place(x=0,y=0)

  sbookID = StringVar()
  bookID = Entry(win, font=(fontUsed, 14), width=8, textvariable=sbookID)
  bookID.place(x=395,y=42)

  searchBtn = Button(win, text="Search", bg='#655bd6', fg='white', font=(fontUsed, 11), borderwidth=0, width=8, command=searchBtnClick)
  searchBtn.place(x=500, y=42)

  searchBtn.bind("<Enter>", lambda e: btnMouseEnter(searchBtn))
  searchBtn.bind("<Leave>", lambda e: btnMouseLeave(searchBtn))

  isbn = Entry(win, font=(fontUsed, 14), width=24, textvariable=strEntries["sisbn"], state='disabled')
  isbn.place(x=373,y=130)

  book_title = Entry(win, font=(fontUsed, 13), width=23, textvariable=strEntries["stitle"], state='disabled')
  book_title.place(x=408,y=172)

  author = Entry(win, font=(fontUsed, 13), width=26, textvariable=strEntries["sauthor"], state='disabled')
  author.place(x=381,y=212)

  publisher = Entry(win, font=(fontUsed, 13), width=24, textvariable=strEntries["spublisher"], state='disabled')
  publisher.place(x=400,y=252)

  edition = Entry(win, font=(fontUsed, 13),width=26, textvariable=strEntries["sedition"], state='disabled')
  edition.place(x=383,y=294)


  editBtn = Button(win, text="Edit Book", bg='#655bd6', fg='white', font=(fontUsed, 14), borderwidth=0, width=12, command=editBtnClick)
  editBtn.place(x=545,y=350)

  editBtn.bind("<Enter>", lambda e: btnMouseEnter(editBtn))
  editBtn.bind("<Leave>", lambda e: btnMouseLeave(editBtn))


  resetBtn = Button(win, text="Reset", bg='#655bd6', fg='white', font=(fontUsed, 11), borderwidth=0, width=8, command=resetBtnClick)
  resetBtn.place(x=580, y=42)

  resetBtn.bind("<Enter>", lambda e: btnMouseEnter(resetBtn))
  resetBtn.bind("<Leave>", lambda e: btnMouseLeave(resetBtn))


  win.mainloop()

# main()