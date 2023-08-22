from tkinter import *
from tkcalendar import DateEntry
from tkinter import messagebox
import datetime
import backend
from btn_hover import *


def main(root):
# def main():
  fontUsed = "Segoe UI"

  def issueBtnClick():
    issue = True
    for value in bookstrEntries.values():
      if value.get()=='':
        issue = False
    for value in stdstrEntries.values():
      if value.get()=='':
        issue = False
    if issue:
      if int(avail_copies.get())>0:
        try:
          backend.issue_book(bookID.get(), sid.get(), issueDate.get(), dueDate.get())
          messagebox.showinfo("Done", "Book issued successfully!", parent=win)
          win.destroy()
        except Exception as e:
          if "unique" in str(e).lower():
            messagebox.showinfo("Issued", "Specified Book is already issued to the specified student!", parent=win)
      else:
        messagebox.showinfo("Copies", "Not enough copies available!", parent=win)
    else:
      messagebox.showinfo("Search", "Search first!", parent=win)

  def booksearchBtnClick():
    if bookID.get()!='':
      if bookID.get().isnumeric():
        entries = backend.search_book_issue(bookID.get())
        if entries!=None:
          bookID.config(state='disabled')

          i = 0
          for key in bookstrEntries.keys():
            bookstrEntries[key].set(entries[i])
            i+=1
        else:
          messagebox.showerror("Not found", "Specified BookID not found!", parent=win)
          for key in bookstrEntries.keys():
            bookstrEntries[key].set('')
      else:
        messagebox.showinfo("BookID", "BookID must be a number!", parent=win)
    else:
      messagebox.showinfo("BookID", "Enter bookID first!", parent=win)

  def stdsearchBtnClick():
    if sid.get()!='':
      if sid.get().isnumeric():
        entries = backend.search_student_issue(sid.get())
        if entries!=None:
          sid.config(state='disabled')

          i = 0
          for key in stdstrEntries.keys():
            stdstrEntries[key].set(entries[i])
            i+=1
        else:
          messagebox.showerror("Not found", "Specified SID not found!", parent=win)
          for key in stdstrEntries.keys():
            stdstrEntries[key].set('')
      else:
        messagebox.showinfo("SID", "SID must be a number!", parent=win)
    else:
      messagebox.showinfo("SID", "Enter SID first!", parent=win)

  def bookresetBtnClick():
    sbookID.set("")
    bookID.config(state='normal')
    for key in bookstrEntries.keys():
      bookstrEntries[key].set("")
    win.focus()

  def stdresetBtnClick():
    ssid.set("")
    sid.config(state='normal')
    for key in stdstrEntries.keys():
      stdstrEntries[key].set("")
    win.focus()  


  win = Toplevel(root)
  # win = Tk()
  bookstrEntries={"sisbn": StringVar(), "stitle": StringVar(), "sauthor": StringVar(), "spublisher": StringVar(), "sedition": StringVar(), "savail_copies": StringVar()}
  stdstrEntries={"sfname": StringVar(), "slname": StringVar(), "semail": StringVar(), "sphno": StringVar()}

  win.grab_set()
  win.focus()
  win.title("Issue Book")
  width = 700
  height = 550
  x = ((win.winfo_screenwidth() - width)//2)-30
  y = ((win.winfo_screenheight() - height)//2)-30
  win.geometry(f"{width}x{height}+{x}+{y}")
  win.resizable(0, 0)
  bgimage=PhotoImage(file="images/issue_book.png") 
  bg=Label(win, image=bgimage)
  bg.place(x=0,y=0)

  sbookID = StringVar()
  bookID = Entry(win, font=(fontUsed, 14), width=8, textvariable=sbookID)
  bookID.place(x=380,y=14)

  booksearchBtn = Button(win, text="Search", bg='#655bd6', fg='white', font=(fontUsed, 11), borderwidth=0, width=8, command=booksearchBtnClick)
  booksearchBtn.place(x=475, y=13)

  booksearchBtn.bind("<Enter>", lambda e: btnMouseEnter(booksearchBtn))
  booksearchBtn.bind("<Leave>", lambda e: btnMouseLeave(booksearchBtn))

  isbn = Entry(win, font=(fontUsed, 11), width=23, textvariable=bookstrEntries["sisbn"], state='disabled')
  isbn.place(x=350,y=66)

  book_title = Entry(win, font=(fontUsed, 11), width=19, textvariable=bookstrEntries["stitle"], state='disabled')
  book_title.place(x=382,y=95)

  author = Entry(win, font=(fontUsed, 11), width=22, textvariable=bookstrEntries["sauthor"], state='disabled')
  author.place(x=358,y=123)

  publisher = Entry(win, font=(fontUsed, 11), width=20, textvariable=bookstrEntries["spublisher"], state='disabled')
  publisher.place(x=375,y=150)

  edition = Entry(win, font=(fontUsed, 11),width=22, textvariable=bookstrEntries["sedition"], state='disabled')
  edition.place(x=360,y=178)

  avail_copies = Entry(win, font=(fontUsed, 11),width=12, textvariable=bookstrEntries["savail_copies"], state='disabled')
  avail_copies.place(x=440,y=206)

  ssid = StringVar()
  sid = Entry(win, font=(fontUsed, 14), width=8, textvariable=ssid)
  sid.place(x=345,y=240)

  stdsearchBtn = Button(win, text="Search", bg='#655bd6', fg='white', font=(fontUsed, 11), borderwidth=0, width=8, command=stdsearchBtnClick)
  stdsearchBtn.place(x=440, y=239)

  stdsearchBtn.bind("<Enter>", lambda e: btnMouseEnter(stdsearchBtn))
  stdsearchBtn.bind("<Leave>", lambda e: btnMouseLeave(stdsearchBtn))

  fname = Entry(win, font=(fontUsed, 11), width=12, state='disabled', textvariable=stdstrEntries["sfname"])
  fname.place(x=392,y=292)
  lname = Entry(win, font=(fontUsed, 11), width=12, state='disabled', textvariable=stdstrEntries["slname"])
  lname.place(x=508,y=292)

  email = Entry(win, font=(fontUsed, 11), width=24, state='disabled', textvariable=stdstrEntries["semail"])
  email.place(x=352,y=346)
  phno = Entry(win, font=(fontUsed, 11), width=20, state='disabled', textvariable=stdstrEntries["sphno"])
  phno.place(x=384,y=375)

  strIssuedate = StringVar(value=datetime.date.today())
  issueDate = DateEntry(win, font=(fontUsed, 10), date_pattern="yyyy-mm-dd", state='disabled', textvariable=strIssuedate)
  issueDate.place(x=410,y=428)



  def change_cal_position(e):
    cal = dueDate._top_cal
    if cal.winfo_ismapped():
      cal.withdraw()
    else:
      x, y, _, _ = dueDate.bbox("insert")
      x += dueDate.winfo_rootx() - 50
      y += dueDate.winfo_rooty() - 206

      cal.geometry(f"+{x}+{y}")
      cal.deiconify()

  dueDate = DateEntry(win, font=(fontUsed, 10), date_pattern="yyyy-mm-dd", mindate=datetime.date.today()+datetime.timedelta(days=1))
  dueDate.place(x=410,y=460)
  dueDate.bind("<Button-1>", change_cal_position)



  issueBtn = Button(win, text="Issue Book", bg='#655bd6', fg='white', font=(fontUsed, 14), borderwidth=0, width=12, command=issueBtnClick)
  issueBtn.place(x=545,y=440)

  issueBtn.bind("<Enter>", lambda e: btnMouseEnter(issueBtn))
  issueBtn.bind("<Leave>", lambda e: btnMouseLeave(issueBtn))


  bookresetBtn = Button(win, text="Reset", bg='#655bd6', fg='white', font=(fontUsed, 11), borderwidth=0, width=8, command=bookresetBtnClick)
  bookresetBtn.place(x=555, y=13)

  bookresetBtn.bind("<Enter>", lambda e: btnMouseEnter(bookresetBtn))
  bookresetBtn.bind("<Leave>", lambda e: btnMouseLeave(bookresetBtn))


  stdresetBtn = Button(win, text="Reset", bg='#655bd6', fg='white', font=(fontUsed, 11), borderwidth=0, width=8, command=stdresetBtnClick)
  stdresetBtn.place(x=520, y=239)

  stdresetBtn.bind("<Enter>", lambda e: btnMouseEnter(stdresetBtn))
  stdresetBtn.bind("<Leave>", lambda e: btnMouseLeave(stdresetBtn))


  win.mainloop()

# main()