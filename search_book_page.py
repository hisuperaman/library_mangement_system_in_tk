from tkinter import *
from tkinter import messagebox
import backend
from btn_hover import *


def main(root):
# def main():
  fontUsed = "Segoe UI"

  def searchBtnClick():
    if bookID.get()!='':
      if bookID.get().isnumeric():
        entries = backend.search_book_full(bookID.get())
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
    bookID.config(state='normal')
    for key in strEntries.keys():
      strEntries[key].set("")
    win.focus()  
  

  win = Toplevel(root)
  # win = Tk()
  strEntries={"sisbn": StringVar(), "stitle": StringVar(), "sauthor": StringVar(), "spublisher": StringVar(), "sedition": StringVar(), "stotal_copies": StringVar(), "sissued_copies": StringVar(), "savail_copies": StringVar()}
  
  win.grab_set()
  win.focus()
  win.title("Search Book")
  width = 700
  height = 550
  x = ((win.winfo_screenwidth() - width)//2)-30
  y = ((win.winfo_screenheight() - height)//2)-30
  win.geometry(f"{width}x{height}+{x}+{y}")
  win.resizable(0, 0)
  bgimage=PhotoImage(file="images/search_book.png") 
  bg=Label(win, image=bgimage)
  bg.place(x=0,y=0)

  sbookID = StringVar()
  bookID = Entry(win, font=(fontUsed, 14), width=8, textvariable=sbookID)
  bookID.place(x=395,y=44)

  searchBtn = Button(win, text="Search", bg='#655bd6', fg='white', font=(fontUsed, 11), borderwidth=0, width=8, command=searchBtnClick)
  searchBtn.place(x=500, y=43)

  searchBtn.bind("<Enter>", lambda e: btnMouseEnter(searchBtn))
  searchBtn.bind("<Leave>", lambda e: btnMouseLeave(searchBtn))

  isbn = Entry(win, font=(fontUsed, 14), width=21, state='disabled', textvariable=strEntries["sisbn"])
  isbn.place(x=371,y=130)

  book_title = Entry(win, font=(fontUsed, 13), width=19, state='disabled', textvariable=strEntries["stitle"])
  book_title.place(x=410,y=172)

  author = Entry(win, font=(fontUsed, 13), width=22, state='disabled', textvariable=strEntries["sauthor"])
  author.place(x=383,y=212)

  publisher = Entry(win, font=(fontUsed, 13), width=20, state='disabled', textvariable=strEntries["spublisher"])
  publisher.place(x=402,y=252)

  edition = Entry(win, font=(fontUsed, 13),width=22, state='disabled', textvariable=strEntries["sedition"])
  edition.place(x=385,y=295)

  total_copies = Entry(win, font=(fontUsed, 13),width=14, state='disabled', textvariable=strEntries["stotal_copies"])
  total_copies.place(x=432,y=371)

  issued_copies = Entry(win, font=(fontUsed, 13),width=12, state='disabled', textvariable=strEntries["sissued_copies"])
  issued_copies.place(x=451,y=410)

  avail_copies = Entry(win, font=(fontUsed, 13),width=9, state='disabled', textvariable=strEntries["savail_copies"])
  avail_copies.place(x=479,y=452)


  resetBtn = Button(win, text="Reset", bg='#655bd6', fg='white', font=(fontUsed, 11), borderwidth=0, width=8, command=resetBtnClick)
  resetBtn.place(x=580, y=43)

  resetBtn.bind("<Enter>", lambda e: btnMouseEnter(resetBtn))
  resetBtn.bind("<Leave>", lambda e: btnMouseLeave(resetBtn))


  win.mainloop()

# main()