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
    if sid.get()!='':
      for value in strEntries.values():
        if value.get()=='':
          delete = False
      if delete:
        try:
          backend.delete_student(sid.get())
          messagebox.showinfo("Done", "Student deleted successfully!", parent=win)
          win.destroy()
        except Exception as e:
          e = str(e)
          if "foreign key" in e:
            messagebox.showerror("Error", "A book is issued to the specified student\nBook must be returned first!", parent=win)
      else:
        messagebox.showinfo("Search", "Press the search button!", parent=win)
    else:
      messagebox.showinfo("Search", "Search student first!", parent=win)

  def searchBtnClick():
    if sid.get()!="":
      if sid.get().isnumeric():
        entries = backend.search_student(sid.get())
        if entries!=None:
          sid.config(state='disabled')

          i = 1
          for key in strEntries.keys():
            strEntries[key].set(entries[i])
            i+=1

          pfp_path = backend.get_student_pfp(sid.get())
          pfp_path = pfp_path[0]
          if pfp_path!=None and os.path.exists(pfp_path):
            pfp_frame.place(x=50, y=105)
            img = Image.open(pfp_path).resize((150, 150), Image.Resampling.LANCZOS)
            img = ImageTk.PhotoImage(img)
            pfp_label.config(image=img)
            pfp_label.image = img
            pfp_label.pack()

        else:
          messagebox.showerror("Not found", "Specified SID not found!", parent=win)
          for key in strEntries.keys():
            strEntries[key].set('')
      else:
        messagebox.showinfo("SID", "SID must be a number!", parent=win)
    else:
      messagebox.showinfo("SID", "Enter SID first!", parent=win)

  def resetBtnClick():
    ssid.set("")
    sid.config(state="normal")
    for key in strEntries.keys():
      strEntries[key].set("")
    strEntries["sgender"].set("M")
    strEntries["sdob"].set(default_date)
    pfp_label.pack_forget()
    pfp_frame.place_forget()
    win.focus()
        


  win = Toplevel(root)
  # win = Tk()
  strEntries={"sfname": StringVar(), "slname": StringVar(), "sgender": StringVar(value='M'), "sdob": StringVar(), "sfathername": StringVar(), "semail": StringVar(), "sphno": StringVar(), "saddress": StringVar()}
  win.grab_set()
  win.focus()
  win.title("Delete Existing Student")
  width = 700
  height = 550
  x = ((win.winfo_screenwidth() - width)//2)-30
  y = ((win.winfo_screenheight() - height)//2)-30
  win.geometry(f"{width}x{height}+{x}+{y}")
  win.resizable(0, 0)
  bgimage=PhotoImage(file="images/delete_student.png") 
  bg=Label(win, image=bgimage)
  bg.place(x=0,y=0)

  ssid = StringVar()
  sid = Entry(win, font=(fontUsed, 14), width=8, textvariable=ssid)
  sid.place(x=360, y=50)

  searchBtn = Button(win, text="Search", bg='#655bd6', fg='white', font=(fontUsed, 11), borderwidth=0, width=8, command=searchBtnClick)
  searchBtn.place(x=465, y=50)

  searchBtn.bind("<Enter>", lambda e: btnMouseEnter(searchBtn))
  searchBtn.bind("<Leave>", lambda e: btnMouseLeave(searchBtn))

  fname = Entry(win, font=(fontUsed, 14), width=12, textvariable=strEntries["sfname"], state='disabled')
  fname.place(x=410,y=110)
  lname = Entry(win, font=(fontUsed, 14), width=12, textvariable=strEntries["slname"], state='disabled')
  lname.place(x=540,y=110)

  # gender = StringVar(win, value='M')
  Radiobutton(win, variable=strEntries['sgender'],value="M",text="Male", font=("Reem Kufi", 14), bg="#ebecff", activebackground="#ebecff", fg="#585858", activeforeground="#585858", state='disabled').place(x=400,y=160)
  Radiobutton(win, variable=strEntries['sgender'],value="F", text="Female", font=("Reem Kufi", 14), bg="#ebecff", activebackground="#ebecff", fg="#585858", activeforeground="#585858", state='disabled').place(x=480,y=160)
  
  dob = DateEntry(win, font=(fontUsed, 10), textvariable=strEntries["sdob"], date_pattern="yyyy-mm-dd", state='disabled')
  dob.place(x=435,y=210)
  default_date = dob.get()

  fathername = Entry(win, font=(fontUsed, 13), width=18, textvariable=strEntries["sfathername"], state='disabled')
  fathername.place(x=445,y=247)

  email = Entry(win, font=(fontUsed, 13), width=25, textvariable=strEntries["semail"], state='disabled')
  email.place(x=380,y=285)
  phno = Entry(win, font=(fontUsed, 13), width=23, textvariable=strEntries["sphno"], state='disabled')
  phno.place(x=400,y=324)
  address = Entry(win, font=(fontUsed, 13), textvariable=strEntries["saddress"], width=24, state='disabled')
  address.place(x=393,y=360)


  deleteBtn = Button(win, text="Delete Student", bg='#655bd6', fg='white', font=(fontUsed, 14), borderwidth=0, width=12, command=deleteBtnClick)
  deleteBtn.place(x=550,y=400)

  deleteBtn.bind("<Enter>", lambda e: btnMouseEnter(deleteBtn))
  deleteBtn.bind("<Leave>", lambda e: btnMouseLeave(deleteBtn))


  pfp_frame = Frame(win, bg="#655bd6")
  
  pfp_label = Label(pfp_frame)

  resetBtn = Button(win, text="Reset", bg='#655bd6', fg='white', font=(fontUsed, 11), borderwidth=0, width=8, command=resetBtnClick)
  resetBtn.place(x=545, y=50)

  resetBtn.bind("<Enter>", lambda e: btnMouseEnter(resetBtn))
  resetBtn.bind("<Leave>", lambda e: btnMouseLeave(resetBtn))


  win.mainloop()

# main()