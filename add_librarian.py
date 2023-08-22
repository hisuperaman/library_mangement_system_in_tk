from tkinter import *
from tkcalendar import DateEntry
from tkinter import messagebox
import backend
from btn_hover import *
from PIL import Image, ImageTk
from tkinter import filedialog


def main(root):
# def main():
  fontUsed = "Segoe UI"
  pfp_path = None
  

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
    pfp_path = None
    pfp_label.pack_forget()
    pfp_frame.place_forget()


  def addBtnClick():
    if fname.get()!='' and lname.get()!='' and gender.get()!='' and dob.get()!='' and email.get()!='' and phno.get()!='' and address.get()!='' and usrname.get()!='' and temp_password.get()!='' and password.get()!='':
      if temp_password.get()==password.get():
        if phno.get().isnumeric():
          try:
            backend.add_librarian(fname.get(), lname.get(), gender.get(), dob.get(), email.get(), phno.get(), address.get(), usrname.get(), password.get(), pfp_path)
            libID = backend.get_recent_libid()

            messagebox.showinfo("Done", f"Librarian added successfully with LibID {libID}!", parent=win)
            win.destroy()
          except Exception as e:
            print(e)
            e = str(e).lower()
            if "unique" in e and "email" in e:
              messagebox.showinfo("Email", "Email already exists!", parent=win)
            elif "unique" in e and "lib_user" in e:
              messagebox.showinfo("Username", "Username already exists!", parent=win)
            else:
              messagebox.showerror("Error", "Something went wrong!", parent=win)
        else:
          messagebox.showinfo("Phone Number", "Phone number must be a number!", parent=win)
      else:
        messagebox.showinfo("Password", "Password does not match!", parent=win)
    else:
      messagebox.showinfo("Inputs", "Input fields must not be empty!", parent=win)

  def resetBtnClick():
    remove_pfp_btn_click()
    for key in strEntries.keys():
      strEntries[key].set("")
    gender.set("M")
    sdob.set(default_date)
    win.focus()

  win = Toplevel(root)
  # win = Tk()
  win.grab_set()
  win.focus()
  win.title("Add Librarian")
  width = 700
  height = 550
  x = ((win.winfo_screenwidth() - width)//2)-30
  y = ((win.winfo_screenheight() - height)//2)-30
  win.geometry(f"{width}x{height}+{x}+{y}")
  win.resizable(0, 0)
  bgimage=PhotoImage(file="images/add_librarian.png") 
  bg=Label(win, image=bgimage)
  bg.place(x=0,y=0)
  strEntries={"sfname": StringVar(), "slname": StringVar(), "semail": StringVar(), "sphno": StringVar(), "saddress": StringVar(), "susrname": StringVar(), "stemp_password": StringVar(), "spassword": StringVar()}
  
  fname = Entry(win, font=(fontUsed, 14), width=12, textvariable=strEntries["sfname"])
  fname.place(x=410,y=42)
  lname = Entry(win, font=(fontUsed, 14), width=12, textvariable=strEntries["slname"])
  lname.place(x=540,y=42)

  gender = StringVar(win, value='M')
  Radiobutton(win, variable=gender,value="M",text="Male", font=("Reem Kufi", 14), bg="#ebecff", activebackground="#ebecff", fg="#585858", activeforeground="#585858").place(x=400,y=92)
  Radiobutton(win, variable=gender,value="F", text="Female", font=("Reem Kufi", 14), bg="#ebecff", activebackground="#ebecff", fg="#585858", activeforeground="#585858").place(x=480,y=92)
  
  sdob = StringVar()
  dob = DateEntry(win, font=(fontUsed, 10), date_pattern="yyyy-mm-dd", textvariable=sdob)
  dob.place(x=435,y=142)
  default_date = dob.get()

  email = Entry(win, font=(fontUsed, 13), width=24, textvariable=strEntries["semail"])
  email.place(x=362,y=178)
  phno = Entry(win, font=(fontUsed, 13), width=20, textvariable=strEntries["sphno"])
  phno.place(x=400,y=216)
  address = Entry(win, font=(fontUsed, 13), width=21, textvariable=strEntries["saddress"])
  address.place(x=390,y=252)
  
  usrname = Entry(win, font=(fontUsed, 13), width=20, textvariable=strEntries["susrname"])
  usrname.place(x=405,y=330)
  temp_password = Entry(win, font=(fontUsed, 13), width=20, show='*', textvariable=strEntries["stemp_password"])
  temp_password.place(x=405,y=363)
  password = Entry(win, font=(fontUsed, 13), width=18, show='*', textvariable=strEntries["spassword"])
  password.place(x=475,y=399)


  addBtn = Button(win, text="Add Librarian", bg='#655bd6', fg='white', font=(fontUsed, 14), borderwidth=0, width=12, command=addBtnClick)
  addBtn.place(x=550,y=450)

  addBtn.bind("<Enter>", lambda e: btnMouseEnter(addBtn))
  addBtn.bind("<Leave>", lambda e: btnMouseLeave(addBtn))


  upload_pfp_btn = Button(win, text="Upload", bg='white', fg='#655bd6', font=(fontUsed, 12), borderwidth=0, width=8, command=upload_pfp_btn_click)
  upload_pfp_btn.place(x=45, y=275)
  remove_pfp_btn = Button(win, text="Remove", bg='white', fg='#655bd6', font=(fontUsed, 12), borderwidth=0, width=8, command=remove_pfp_btn_click)
  remove_pfp_btn.place(x=135, y=275)

  upload_pfp_btn.bind("<Enter>", lambda e: pfpbtnMouseEnter(upload_pfp_btn))
  upload_pfp_btn.bind("<Leave>", lambda e: pfpbtnMouseLeave(upload_pfp_btn))
  remove_pfp_btn.bind("<Enter>", lambda e: pfpbtnMouseEnter(remove_pfp_btn))
  remove_pfp_btn.bind("<Leave>", lambda e: pfpbtnMouseLeave(remove_pfp_btn))

  pfp_frame = Frame(win, bg="#655bd6")
  
  
  pfp_label = Label(pfp_frame)


  resetBtn = Button(win, text="Reset", bg='#655bd6', fg='white', font=(fontUsed, 11), borderwidth=0, width=8, command=resetBtnClick)
  resetBtn.place(x=300, y=455)

  resetBtn.bind("<Enter>", lambda e: btnMouseEnter(resetBtn))
  resetBtn.bind("<Leave>", lambda e: btnMouseLeave(resetBtn))


  win.mainloop()

# main()