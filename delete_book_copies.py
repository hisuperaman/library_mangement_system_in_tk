from tkinter import *
from tkinter import messagebox
import backend
from btn_hover import *


def main(root):
# def main():
  fontUsed = "Segoe UI"
  def deleteBtnClick():
    if isbn.get()!='' and book_title.get()!='' and author.get()!='' and publisher.get()!='' and edition.get()!='' and avail_copies.get()!='':
      if copies.get()=='':
        messagebox.showinfo("Copies", "Enter number of copies first!", parent=win)
      elif not (copies.get().isnumeric()):
        messagebox.showinfo("Copies", "Copies must be a number!", parent=win)
      else:
        if int(copies.get()) > int(avail_copies.get()):
          messagebox.showinfo("Copies", "Not enough copies to delete!", parent=win)
        else:
          try:
            backend.delete_book_copies(bookID.get(), copies.get())
            messagebox.showinfo("Done", "Book copies deleted successfully!", parent=win)
            win.destroy()
          except Exception as e:
            messagebox.showerror("Error", "Something went wrong!", parent=win)
    else:
      messagebox.showinfo("Search", "Search the book first!", parent=win)

  def searchBtnClick():
    if bookID.get()!='':
      if bookID.get().isnumeric():
        entries = backend.search_book_for_copies(bookID.get())
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
    scopies.set("")
    win.focus()
    

  win = Toplevel(root)
  # win = Tk()
  strEntries={"sisbn": StringVar(), "stitle": StringVar(), "sauthor": StringVar(), "spublisher": StringVar(), "sedition": StringVar(), "savail_copies": StringVar()}
  
  win.grab_set()
  win.focus_force()
  win.title("Delete Book Copies")
  width = 700
  height = 550
  x = ((win.winfo_screenwidth() - width)//2)-30
  y = ((win.winfo_screenheight() - height)//2)-30
  win.geometry(f"{width}x{height}+{x}+{y}")
  win.resizable(0, 0)
  bgimage=PhotoImage(file="images/delete_book_copies.png") 
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
  edition.place(x=383,y=294)

  avail_copies = Entry(win, font=(fontUsed, 13),width=13, state='disabled', textvariable=strEntries["savail_copies"])
  avail_copies.place(x=475,y=332)

  scopies = StringVar()
  copies = Entry(win, font=(fontUsed, 13),width=13, textvariable=scopies)
  copies.place(x=385,y=405)


  deleteBtn = Button(win, text="Delete Copies", bg='#655bd6', fg='white', font=(fontUsed, 14), borderwidth=0, width=12, command=deleteBtnClick)
  deleteBtn.place(x=545,y=445)

  deleteBtn.bind("<Enter>", lambda e: btnMouseEnter(deleteBtn))
  deleteBtn.bind("<Leave>", lambda e: btnMouseLeave(deleteBtn))


  resetBtn = Button(win, text="Reset", bg='#655bd6', fg='white', font=(fontUsed, 11), borderwidth=0, width=8, command=resetBtnClick)
  resetBtn.place(x=580, y=42)

  resetBtn.bind("<Enter>", lambda e: btnMouseEnter(resetBtn))
  resetBtn.bind("<Leave>", lambda e: btnMouseLeave(resetBtn))


  win.mainloop()

# main()