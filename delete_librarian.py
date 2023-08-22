from tkinter import *
from tkcalendar import DateEntry
from tkinter import messagebox
import backend
from btn_hover import *
from PIL import Image, ImageTk
import os


def main(root):
# def main():
  fontUsed = "Segoe UI"

  def deleteBtnClick():
    delete = True
    if libID.get()!='':
      for value in strEntries.values():
        if value.get()=='':
          delete = False
      if delete:
        backend.delete_librarian(libID.get())
        messagebox.showinfo("Done", "Librarian deleted successfully!", parent=win)
        win.destroy()
      else:
        messagebox.showinfo("Search", "Press the search button!", parent=win)

    else:
      messagebox.showinfo("Search", "Search librarian first!", parent=win)

  def searchBtnClick():
    if libID.get()!="":
      if libID.get().isnumeric():
        entries = backend.search_librarian(libID.get())
        if entries!=None:
          libID.config(state='disabled')

          i = 1
          for key in strEntries.keys():
            strEntries[key].set(entries[i])
            i+=1

          pfp_path = backend.get_librarian_pfp(libID.get())
          pfp_path = pfp_path[0]
          if pfp_path!=None and os.path.exists(pfp_path):
            pfp_frame.place(x=50, y=105)
            img = Image.open(pfp_path).resize((150, 150), Image.Resampling.LANCZOS)
            img = ImageTk.PhotoImage(img)
            pfp_label.config(image=img)
            pfp_label.image = img
            pfp_label.pack()

        else:
          messagebox.showerror("Not found", "Specified LibID not found!", parent=win)
          for key in strEntries.keys():
            strEntries[key].set('')
      else:
        messagebox.showinfo("LibID", "LibID must be a number!", parent=win)
    else:
      messagebox.showinfo("LibID", "Enter LibID first!", parent=win)

  def resetBtnClick():
    slibID.set("")
    libID.config(state="normal")
    for key in strEntries.keys():
      strEntries[key].set("")
    strEntries["sgender"].set("M")
    strEntries["sdob"].set(default_date)
    pfp_label.pack_forget()
    pfp_frame.place_forget()
    win.focus()


  win = Toplevel(root)
  # win = Tk()
  strEntries={"sfname": StringVar(), "slname": StringVar(), "sgender": StringVar(value='M'), "sdob": StringVar(), "semail": StringVar(), "sphno": StringVar(), "saddress": StringVar(), "susrname": StringVar(), "spassword": StringVar()}
  win.grab_set()
  win.focus()
  win.title("Delete Librarian")
  width = 700
  height = 550
  x = ((win.winfo_screenwidth() - width)//2)-30
  y = ((win.winfo_screenheight() - height)//2)-30
  win.geometry(f"{width}x{height}+{x}+{y}")
  win.resizable(0, 0)
  bgimage=PhotoImage(file="images/delete_librarian.png") 
  bg=Label(win, image=bgimage)
  bg.place(x=0,y=0)

  slibID = StringVar()
  libID = Entry(win, font=(fontUsed, 14), width=8, textvariable=slibID)
  libID.place(x=380, y=20)

  searchBtn = Button(win, text="Search", bg='#655bd6', fg='white', font=(fontUsed, 11), borderwidth=0, width=8, command=searchBtnClick)
  searchBtn.place(x=485, y=19)

  searchBtn.bind("<Enter>", lambda e: btnMouseEnter(searchBtn))
  searchBtn.bind("<Leave>", lambda e: btnMouseLeave(searchBtn))

  fname = Entry(win, font=(fontUsed, 14), width=12, textvariable=strEntries["sfname"], state='disabled')
  fname.place(x=410,y=90)
  lname = Entry(win, font=(fontUsed, 14), width=12, textvariable=strEntries["slname"], state='disabled')
  lname.place(x=540,y=90)

  # gender = StringVar(win, value='M')
  Radiobutton(win, variable=strEntries['sgender'],value="M",text="Male", font=("Reem Kufi", 14), bg="#ebecff", activebackground="#ebecff", fg="#585858", activeforeground="#585858", state='disabled').place(x=400,y=138)
  Radiobutton(win, variable=strEntries['sgender'],value="F", text="Female", font=("Reem Kufi", 14), bg="#ebecff", activebackground="#ebecff", fg="#585858", activeforeground="#585858", state='disabled').place(x=480,y=138)
  
  dob = DateEntry(win, font=(fontUsed, 10), textvariable=strEntries["sdob"], date_pattern="yyyy-mm-dd", state='disabled')
  dob.place(x=435,y=188)
  default_date = dob.get()

  email = Entry(win, font=(fontUsed, 13), width=25, textvariable=strEntries["semail"], state='disabled')
  email.place(x=380,y=222)
  phno = Entry(win, font=(fontUsed, 13), width=23, textvariable=strEntries["sphno"], state='disabled')
  phno.place(x=400,y=260)
  address = Entry(win, font=(fontUsed, 13), textvariable=strEntries["saddress"], width=24, state='disabled')
  address.place(x=393,y=297)
  
  usrname = Entry(win, font=(fontUsed, 13), width=18, textvariable=strEntries["susrname"], state='disabled')
  usrname.place(x=405,y=375)
  password = Entry(win, font=(fontUsed, 13), width=18, textvariable=strEntries["spassword"], state='disabled')
  password.place(x=405,y=408)


  deleteBtn = Button(win, text="Delete Librarian", bg='#655bd6', fg='white', font=(fontUsed, 14), borderwidth=0, width=13, command=deleteBtnClick)
  deleteBtn.place(x=540,y=450)

  deleteBtn.bind("<Enter>", lambda e: btnMouseEnter(deleteBtn))
  deleteBtn.bind("<Leave>", lambda e: btnMouseLeave(deleteBtn))


  pfp_frame = Frame(win, bg="#655bd6")
  
  pfp_label = Label(pfp_frame)


  resetBtn = Button(win, text="Reset", bg='#655bd6', fg='white', font=(fontUsed, 11), borderwidth=0, width=8, command=resetBtnClick)
  resetBtn.place(x=565, y=19)

  resetBtn.bind("<Enter>", lambda e: btnMouseEnter(resetBtn))
  resetBtn.bind("<Leave>", lambda e: btnMouseLeave(resetBtn))


  win.mainloop()

# main()