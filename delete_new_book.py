from tkinter import *
from tkinter import messagebox
import backend
from btn_hover import *


def main(root):
# def main():
  fontUsed = "Segoe UI"
  def deleteBtnClick():
    if isbn.get()!='' and book_title.get()!='' and author.get()!='' and publisher.get()!='' and edition.get()!='':
      try:
        backend.delete_new_book(bookID.get())
        messagebox.showinfo("Done", "Book deleted successfully!", parent=win)
        win.destroy()
      except Exception as e:
        e = str(e)
        if "foreign key" in e:
          messagebox.showerror("Error", "Specified book is issued to a student\nBook must be returned first!", parent=win)
    else:
      messagebox.showinfo("Search", "Search the book first!", parent=win)

  def searchBtnClick():
    if bookID.get()!='':
      if bookID.get().isnumeric():
        entries = backend.search_book(bookID.get())
        if entries!=None:
          bookID.config(state='disabled')

          i = 0
          for key in strEntries.keys():
            strEntries[key].set(entries[i])
            i+=1
        else:
          messagebox.showerror("Not found", "Specified BookID not found!", parent=win)
          for key in strEntries.keys():
            strEntries[key].set('')
      else:
        messagebox.showinfo("BookID", "BookID must be a number!", parent=win)
    else:
      messagebox.showinfo("BookID", "Enter BookID first!", parent=win)

  def resetBtnClick():
    sbookID.set("")
    bookID.config(state="normal")
    for key in strEntries.keys():
      strEntries[key].set("")
    win.focus()


  win = Toplevel(root)
  # win = Tk()
  strEntries={"sisbn": StringVar(), "stitle": StringVar(), "sauthor": StringVar(), "spublisher": StringVar(), "sedition": StringVar(), "savail_copies": StringVar()}

  win.grab_set()
  win.focus_force()
  win.title("Delete Existing Book")
  width = 700
  height = 550
  x = ((win.winfo_screenwidth() - width)//2)-30
  y = ((win.winfo_screenheight() - height)//2)-30
  win.geometry(f"{width}x{height}+{x}+{y}")
  win.resizable(0, 0)
  bgimage=PhotoImage(file="images/delete_book.png") 
  bg=Label(win, image=bgimage)
  bg.place(x=0,y=0)

  sbookID = StringVar()
  bookID = Entry(win, font=(fontUsed, 14), width=8, textvariable=sbookID)
  bookID.place(x=395,y=42)

  searchBtn = Button(win, text="Search", bg='#655bd6', fg='white', font=(fontUsed, 11), borderwidth=0, width=8, command=searchBtnClick)
  searchBtn.place(x=500, y=42)

  searchBtn.bind("<Enter>", lambda e: btnMouseEnter(searchBtn))
  searchBtn.bind("<Leave>", lambda e: btnMouseLeave(searchBtn))

  isbn = Entry(win, font=(fontUsed, 14), width=24, state='disabled', textvariable=strEntries["sisbn"])
  isbn.place(x=373,y=130)

  book_title = Entry(win, font=(fontUsed, 13), width=23, state='disabled', textvariable=strEntries["stitle"])
  book_title.place(x=408,y=172)

  author = Entry(win, font=(fontUsed, 13), width=26, state='disabled', textvariable=strEntries["sauthor"])
  author.place(x=381,y=212)

  publisher = Entry(win, font=(fontUsed, 13), width=24, state='disabled', textvariable=strEntries["spublisher"])
  publisher.place(x=400,y=252)

  edition = Entry(win, font=(fontUsed, 13),width=26, state='disabled', textvariable=strEntries["sedition"])
  edition.place(x=383,y=295)


  deleteBtn = Button(win, text="Delete Book", bg='#655bd6', fg='white', font=(fontUsed, 14), borderwidth=0, width=12, command=deleteBtnClick)
  deleteBtn.place(x=545,y=350)

  deleteBtn.bind("<Enter>", lambda e: btnMouseEnter(deleteBtn))
  deleteBtn.bind("<Leave>", lambda e: btnMouseLeave(deleteBtn))


  resetBtn = Button(win, text="Reset", bg='#655bd6', fg='white', font=(fontUsed, 11), borderwidth=0, width=8, command=resetBtnClick)
  resetBtn.place(x=580, y=42)

  resetBtn.bind("<Enter>", lambda e: btnMouseEnter(resetBtn))
  resetBtn.bind("<Leave>", lambda e: btnMouseLeave(resetBtn))


  win.mainloop()

# main()