from tkinter import *
from tkcalendar import DateEntry
from tkinter import messagebox
import datetime
import backend
from btn_hover import *


def main(root):
# def main():

  fontUsed = "Segoe UI"

  def returnBtnClick():
    returnBookflag = True
    for value in bookstrEntries.values():
      if value.get()=='':
        returnBookflag = False
    for value in stdstrEntries.values():
      if value.get()=='':
        returnBookflag = False
    if returnBookflag:
      try:
        backend.return_book(bookID.get(), sid.get(), issueDate.get(), dueDate.get(), returnDate.get(), fine.get())
        messagebox.showinfo("Done", "Book returned successfully!", parent=win)
        win.destroy()
      except Exception as e:
        messagebox.showerror("Error", "Something went wrong!", parent=win)
        # print(e)
    else:
      messagebox.showinfo("Search", "Search first!", parent=win)

  def searchBtnClick():
    if bookID.get()!='' and sid.get()!='':
      if bookID.get().isnumeric() and sid.get().isnumeric():
        bookentries = None
        studententries = None
        if backend.search_book_std_return(bookID.get(), sid.get())==0:
          bookentries = backend.search_book_issue(bookID.get())
          studententries = backend.search_student_issue(sid.get())
        
        if bookentries!=None and studententries!=None:

          bookID.config(state='disabled')
          sid.config(state='disabled')

          # book entries
          i = 0
          for key in bookstrEntries.keys():
            bookstrEntries[key].set(bookentries[i])
            i+=1

          # student entries
          i = 0
          for key in stdstrEntries.keys():
            stdstrEntries[key].set(studententries[i])
            i+=1

          # date entries
          dateEntries = backend.search_dates(bookID.get(), sid.get())
          i = 0
          for key in datestrEntries.keys():
            datestrEntries[key].set(dateEntries[i])
            i+=1

          # fine entry
          fineVal = int(backend.get_fine_val()[0])
          date_due = datetime.datetime.strptime(dateEntries[1], "%Y-%m-%d").date()
          date_return = datetime.date.today()
          days = date_return-date_due
          total_fine = int(days.days) * fineVal
          if total_fine>0:
            sfine.set(total_fine)
          else:
            total_fine = 0
            sfine.set(total_fine)

        else:
          messagebox.showerror("Not found", "Specified book is not issued to specified student!", parent=win)
          for key in bookstrEntries.keys():
            bookstrEntries[key].set('')
          for key in stdstrEntries.keys():
            stdstrEntries[key].set('')
      else:
        messagebox.showinfo("IDs", "BookID and SID must be a number!", parent=win)
    else:
      messagebox.showinfo("IDs", "Enter IDs first!", parent=win)

  def resetBtnClick():
    sbookID.set("")
    ssid.set("")
    bookID.config(state='normal')
    sid.config(state='normal')
    for key in bookstrEntries.keys():
      bookstrEntries[key].set("")
    for key in stdstrEntries.keys():
      stdstrEntries[key].set("")
    for key in datestrEntries.keys():
      datestrEntries[key].set("")
    strReturndate.set(default_returnDate)
    sfine.set(default_fine)
    win.focus()


  win = Toplevel(root)
  # win = Tk()
  bookstrEntries={"sisbn": StringVar(), "stitle": StringVar(), "sauthor": StringVar(), "spublisher": StringVar(), "sedition": StringVar(), "savail_copies": StringVar()}
  stdstrEntries={"sfname": StringVar(), "slname": StringVar(), "semail": StringVar(), "sphno": StringVar()}
  datestrEntries={"sissue_date": StringVar(), "sdue_date": StringVar()}

  win.grab_set()
  win.focus()
  win.title("Return Book")
  width = 700
  height = 550
  x = ((win.winfo_screenwidth() - width)//2)-30
  y = ((win.winfo_screenheight() - height)//2)-30
  win.geometry(f"{width}x{height}+{x}+{y}")
  win.resizable(0, 0)
  bgimage=PhotoImage(file="images/return_book.png") 
  bg=Label(win, image=bgimage)
  bg.place(x=0,y=0)

  sbookID = StringVar()
  bookID = Entry(win, font=(fontUsed, 14), width=8, textvariable=sbookID)
  bookID.place(x=380,y=12)

  ssid = StringVar()
  sid = Entry(win, font=(fontUsed, 14), width=8, textvariable=ssid)
  sid.place(x=380,y=45)

  searchBtn = Button(win, text="Search", bg='#655bd6', fg='white', font=(fontUsed, 11), borderwidth=0, width=8, command=searchBtnClick)
  searchBtn.place(x=475, y=22)

  searchBtn.bind("<Enter>", lambda e: btnMouseEnter(searchBtn))
  searchBtn.bind("<Leave>", lambda e: btnMouseLeave(searchBtn))

  isbn = Entry(win, font=(fontUsed, 11), width=22, textvariable=bookstrEntries["sisbn"], state='disabled')
  isbn.place(x=352,y=104)

  book_title = Entry(win, font=(fontUsed, 11), width=18, textvariable=bookstrEntries["stitle"], state='disabled')
  book_title.place(x=384,y=132)

  author = Entry(win, font=(fontUsed, 11), width=21, textvariable=bookstrEntries["sauthor"], state='disabled')
  author.place(x=360,y=160)

  publisher = Entry(win, font=(fontUsed, 11), width=19, textvariable=bookstrEntries["spublisher"], state='disabled')
  publisher.place(x=377,y=188)

  edition = Entry(win, font=(fontUsed, 11),width=21, textvariable=bookstrEntries["sedition"], state='disabled')
  edition.place(x=361,y=215)

  avail_copies = Entry(win, font=(fontUsed, 11),width=11, textvariable=bookstrEntries["savail_copies"], state='disabled')
  avail_copies.place(x=441,y=243)


  fname = Entry(win, font=(fontUsed, 11), width=12, state='disabled', textvariable=stdstrEntries["sfname"])
  fname.place(x=392,y=292)
  lname = Entry(win, font=(fontUsed, 11), width=12, state='disabled', textvariable=stdstrEntries["slname"])
  lname.place(x=508,y=292)

  email = Entry(win, font=(fontUsed, 11), width=24, state='disabled', textvariable=stdstrEntries["semail"])
  email.place(x=352,y=346)
  phno = Entry(win, font=(fontUsed, 11), width=20, state='disabled', textvariable=stdstrEntries["sphno"])
  phno.place(x=384,y=375)

  issueDate = DateEntry(win, font=(fontUsed, 10), date_pattern="yyyy-mm-dd", state='disabled', textvariable=datestrEntries["sissue_date"])
  issueDate.place(x=405,y=411)

  dueDate = DateEntry(win, font=(fontUsed, 10), date_pattern="yyyy-mm-dd", mindate=datetime.date.today()+datetime.timedelta(days=1), state='disabled', textvariable=datestrEntries["sdue_date"])
  dueDate.place(x=405,y=440)

  strReturndate = StringVar(value=datetime.date.today())
  returnDate = DateEntry(win, font=(fontUsed, 10), date_pattern="yyyy-mm-dd", state='disabled', textvariable=strReturndate)
  returnDate.place(x=420,y=470)
  default_returnDate = returnDate.get()

  sfine = StringVar()
  fine = Entry(win, font=(fontUsed, 10), width=17, state='disabled', textvariable=sfine)
  fine.place(x=405,y=502)
  default_fine = fine.get()


  returnBtn = Button(win, text="Return Book", bg='#655bd6', fg='white', font=(fontUsed, 14), borderwidth=0, width=12, command=returnBtnClick)
  returnBtn.place(x=545,y=440)

  returnBtn.bind("<Enter>", lambda e: btnMouseEnter(returnBtn))
  returnBtn.bind("<Leave>", lambda e: btnMouseLeave(returnBtn))


  resetBtn = Button(win, text="Reset", bg='#655bd6', fg='white', font=(fontUsed, 11), borderwidth=0, width=8, command=resetBtnClick)
  resetBtn.place(x=555, y=22)

  resetBtn.bind("<Enter>", lambda e: btnMouseEnter(resetBtn))
  resetBtn.bind("<Leave>", lambda e: btnMouseLeave(resetBtn))


  win.mainloop()

# main()