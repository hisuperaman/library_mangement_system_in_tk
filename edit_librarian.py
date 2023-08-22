from tkinter import *
from tkcalendar import DateEntry
from tkinter import messagebox
import backend
from btn_hover import *
from PIL import Image, ImageTk
from tkinter import filedialog
import os



def main(root):
# def main():
  fontUsed = "Segoe UI"
  pfp_path = None
  remove_btn_clicked = False

  def upload_pfp_btn_click():
    nonlocal pfp_path
    pfp_path = filedialog.askopenfilename(filetypes=[('Images Files', '.png .jpg')])
    if len(pfp_path)>0:
      # print(pfp_path)
      pfp_frame.place(x=50, y=105)
      img = Image.open(pfp_path).resize((150, 150), Image.Resampling.LANCZOS)
      img = ImageTk.PhotoImage(img)
      pfp_label.config(image=img)
      pfp_label.image = img
      pfp_label.pack()

  def remove_pfp_btn_click():
    nonlocal pfp_path
    nonlocal remove_btn_clicked
    pfp_path = None
    pfp_label.pack_forget()
    pfp_frame.place_forget()
    remove_btn_clicked = True


  def editBtnClick():
    nonlocal remove_btn_clicked
    nonlocal pfp_path
    if fname.get()!='' and lname.get()!='' and strEntries["sgender"].get()!='' and dob.get()!='' and email.get()!='' and phno.get()!='' and address.get()!='' and usrname.get()!='' and password.get()!='':
      if phno.get().isnumeric():
        try:
          if remove_btn_clicked==False:
            db_pfp_path = backend.get_librarian_pfp(libID.get())[0]
            if db_pfp_path!=None and pfp_path==None:
              pfp_path = db_pfp_path
          backend.edit_librarian(libID.get(), fname.get(), lname.get(), strEntries['sgender'].get(), dob.get(), email.get(), phno.get(), address.get(), usrname.get(), password.get(), pfp_path)
          messagebox.showinfo("Done", "Librarian edited successfully!", parent=win)
          win.destroy()
        except Exception as e:
            if "duplicate" in str(e).lower():
              messagebox.showinfo("Username", "Username already exists!", parent=win)
            else:
              messagebox.showerror("Error", "Something went wrong!", parent=win)
      else:
        messagebox.showinfo("Phone Number", "Phone number must be a number!", parent=win)
    else:
      messagebox.showinfo("Search", "Search librarian first!", parent=win)

  def searchBtnClick():
    if libID.get()!='':
      if libID.get().isnumeric():

        entries = backend.search_librarian(libID.get())
        if entries!=None:
          libID.config(state='disabled')

          fname.config(state='normal')
          lname.config(state='normal')
          r1.config(state='normal')
          r2.config(state='normal')
          dob.config(state='normal')
          email.config(state='normal')
          phno.config(state='normal')
          address.config(state='normal')
          usrname.config(state='normal')
          password.config(state='normal')

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

          upload_pfp_btn.place(x=45, y=275)
          remove_pfp_btn.place(x=135, y=275)

        else:
          fname.config(state='disabled')
          lname.config(state='disabled')
          r1.config(state='disabled')
          r2.config(state='disabled')
          dob.config(state='disabled')
          email.config(state='disabled')
          phno.config(state='disabled')
          address.config(state='disabled')
          usrname.config(state='disabled')
          password.config(state='disabled')
          
          messagebox.showerror("Not found", "Specified LibID not found!", parent=win)
          for key in strEntries.keys():
            strEntries[key].set('')
      else:
        messagebox.showinfo("LibID", "LibID must be a number!", parent=win)
    else:
      messagebox.showinfo("LibID", "Enter libID first!", parent=win)
  
  def resetBtnClick():
    slibID.set("")
    libID.config(state="normal")
    fname.config(state='disabled')
    lname.config(state='disabled')
    r1.config(state='disabled')
    r2.config(state='disabled')
    dob.config(state='disabled')
    email.config(state='disabled')
    phno.config(state='disabled')
    address.config(state='disabled')
    usrname.config(state='disabled')
    password.config(state='disabled')

    remove_pfp_btn_click()
    upload_pfp_btn.place_forget()
    remove_pfp_btn.place_forget()

    for key in strEntries.keys():
      strEntries[key].set("")
    strEntries["sgender"].set("M")
    strEntries["sdob"].set(default_date)
    win.focus()
        

  win = Toplevel(root)
  # win = Tk()
  strEntries={"sfname": StringVar(), "slname": StringVar(), "sgender": StringVar(value='M'), "sdob": StringVar(), "semail": StringVar(), "sphno": StringVar(), "saddress": StringVar(), "susrname": StringVar(), "spassword": StringVar()}
  
  win.grab_set()
  win.focus()
  win.title("Edit Librarian")
  width = 700
  height = 550
  x = ((win.winfo_screenwidth() - width)//2)-30
  y = ((win.winfo_screenheight() - height)//2)-30
  win.geometry(f"{width}x{height}+{x}+{y}")
  win.resizable(0, 0)
  bgimage=PhotoImage(file="images/edit_librarian.png") 
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
  r1 = Radiobutton(win, variable=strEntries['sgender'],value="M",text="Male", font=("Reem Kufi", 14), bg="#ebecff", activebackground="#ebecff", fg="#585858", activeforeground="#585858", state='disabled')
  r1.place(x=400,y=138)
  r2 = Radiobutton(win, variable=strEntries["sgender"],value="F", text="Female", font=("Reem Kufi", 14), bg="#ebecff", activebackground="#ebecff", fg="#585858", activeforeground="#585858", state='disabled')
  r2.place(x=480,y=138)
  
  dob = DateEntry(win, font=(fontUsed, 10), textvariable=strEntries["sdob"], date_pattern="yyyy-mm-dd", state='disabled')
  dob.place(x=435,y=188)
  default_date = dob.get()

  email = Entry(win, font=(fontUsed, 13), width=25, textvariable=strEntries["semail"], state='disabled')
  email.place(x=380,y=222)
  phno = Entry(win, font=(fontUsed, 13), width=23, textvariable=strEntries["sphno"], state='disabled')
  phno.place(x=399,y=260)
  address = Entry(win, font=(fontUsed, 13), textvariable=strEntries["saddress"], width=24, state='disabled')
  address.place(x=392,y=297)
  
  usrname = Entry(win, font=(fontUsed, 13), width=18, textvariable=strEntries["susrname"], state='disabled')
  usrname.place(x=405,y=375)
  password = Entry(win, font=(fontUsed, 13), width=18, textvariable=strEntries["spassword"], state='disabled')
  password.place(x=405,y=408)


  editBtn = Button(win, text="Save and Update", bg='#655bd6', fg='white', font=(fontUsed, 14), borderwidth=0, width=14, command=editBtnClick)
  editBtn.place(x=525,y=450)

  editBtn.bind("<Enter>", lambda e: btnMouseEnter(editBtn))
  editBtn.bind("<Leave>", lambda e: btnMouseLeave(editBtn))


  upload_pfp_btn = Button(win, text="Upload", bg='white', fg='#655bd6', font=(fontUsed, 12), borderwidth=0, width=8, command=upload_pfp_btn_click)
  remove_pfp_btn = Button(win, text="Remove", bg='white', fg='#655bd6', font=(fontUsed, 12), borderwidth=0, width=8, command=remove_pfp_btn_click)

  upload_pfp_btn.bind("<Enter>", lambda e: pfpbtnMouseEnter(upload_pfp_btn))
  upload_pfp_btn.bind("<Leave>", lambda e: pfpbtnMouseLeave(upload_pfp_btn))
  remove_pfp_btn.bind("<Enter>", lambda e: pfpbtnMouseEnter(remove_pfp_btn))
  remove_pfp_btn.bind("<Leave>", lambda e: pfpbtnMouseLeave(remove_pfp_btn))

  pfp_frame = Frame(win, bg="#655bd6")
  
  
  pfp_label = Label(pfp_frame)


  resetBtn = Button(win, text="Reset", bg='#655bd6', fg='white', font=(fontUsed, 11), borderwidth=0, width=8, command=resetBtnClick)
  resetBtn.place(x=565, y=19)

  resetBtn.bind("<Enter>", lambda e: btnMouseEnter(resetBtn))
  resetBtn.bind("<Leave>", lambda e: btnMouseLeave(resetBtn))


  win.mainloop()

# main()