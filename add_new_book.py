from tkinter import *
from tkinter import messagebox
import backend
from btn_hover import *


def main(root):
# def main():
  fontUsed = "Segoe UI"
  def addBtnClick():
    if isbn.get()!='' and book_title.get()!='' and author.get()!='' and publisher.get()!='' and edition.get()!='' and copies.get()!='':
      try:
        backend.add_new_book(isbn.get(), book_title.get(), author.get(), publisher.get(), edition.get(), copies.get())
        book_id = backend.get_recent_bookid()
        messagebox.showinfo("Done", f"Book added successfully with bookID {book_id}!", parent=win)
        win.destroy()
      except Exception as e:
          if "unique" in str(e).lower():
            messagebox.showinfo("Already exists", "A book already exists with same ISBN!", parent=win)
          elif not (copies.get().isnumeric()):
            messagebox.showinfo("Copies", "Copies must be a number!", parent=win)
          else:
            messagebox.showerror("Error", "Something went wrong", parent=win)
    else:
      messagebox.showinfo("Inputs", "Input fields must not be empty!", parent=win)

  def resetBtnClick():
    for key in strEntries.keys():
      strEntries[key].set("")
    win.focus()

  win = Toplevel(root)
  # win = Tk()
  win.grab_set()
  win.focus_force()
  win.title("Add New Book")
  width = 700
  height = 550
  x = ((win.winfo_screenwidth() - width)//2)-30
  y = ((win.winfo_screenheight() - height)//2)-30
  win.geometry(f"{width}x{height}+{x}+{y}")
  win.resizable(0, 0)
  bgimage=PhotoImage(file="images/add_book.png") 
  bg=Label(win, image=bgimage)
  bg.place(x=0,y=0)
  strEntries = {"sisbn": StringVar(), "sbook_title": StringVar(), "sauthor": StringVar(), "spublisher": StringVar(), "sedition": StringVar(), "scopies": StringVar()}

  isbn = Entry(win, font=(fontUsed, 14), width=24, textvariable=strEntries["sisbn"])
  isbn.place(x=373,y=80)

  book_title = Entry(win, font=(fontUsed, 13), width=23, textvariable=strEntries["sbook_title"])
  book_title.place(x=408,y=120)

  author = Entry(win, font=(fontUsed, 13), width=26, textvariable=strEntries["sauthor"])
  author.place(x=381,y=160)

  publisher = Entry(win, font=(fontUsed, 13), width=24, textvariable=strEntries["spublisher"])
  publisher.place(x=400,y=201)

  edition = Entry(win, font=(fontUsed, 13),width=26, textvariable=strEntries["sedition"])
  edition.place(x=383,y=243)

  copies = Entry(win, font=(fontUsed, 13),width=13, textvariable=strEntries["scopies"])
  copies.place(x=385,y=328)


  addBtn = Button(win, text="Add Book", bg='#655bd6', fg='white', font=(fontUsed, 14), borderwidth=0, width=12, command=addBtnClick)
  addBtn.place(x=545,y=380)

  addBtn.bind("<Enter>", lambda e: btnMouseEnter(addBtn))
  addBtn.bind("<Leave>", lambda e: btnMouseLeave(addBtn))

  resetBtn = Button(win, text="Reset", bg='#655bd6', fg='white', font=(fontUsed, 11), borderwidth=0, width=8, command=resetBtnClick)
  resetBtn.place(x=300, y=385)

  resetBtn.bind("<Enter>", lambda e: btnMouseEnter(resetBtn))
  resetBtn.bind("<Leave>", lambda e: btnMouseLeave(resetBtn))

  win.mainloop()

# main()