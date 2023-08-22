from tkinter import *
from tkinter import messagebox
import backend
from btn_hover import *



def main(root):
# def main():
  fontUsed = "Segoe UI"


  def editBtnClick():
    if usrname.get()!="" and current_password.get()!="" and temp_new_password.get()!="" and new_password.get()!="":
      admin_info = backend.admin_info(usrname.get())
      if admin_info!=None:
        if current_password.get()==admin_info[1]:
            if temp_new_password.get()==new_password.get():
                backend.change_admin_info(usrname.get(), new_usrname.get(), new_password.get())
                messagebox.showinfo("Done", "Login info changed successfully!", parent=win)
                win.destroy()
            else:
                messagebox.showinfo("Password", "New password does not match!", parent=win)
        else:
            messagebox.showinfo("Password", "Incorrect password!", parent=win)
      else:
        messagebox.showerror("Error", "Incorrect username!", parent=win)
    else:
        messagebox.showinfo("Inputs", "Input fields must not be empty!", parent=win)

  def resetBtnClick():
    scurrent_password.set("")
    snew_usrname.set("")
    stemp_new_password.set("")
    snew_password.set("")
    win.focus()
        

  win = Toplevel(root)
  # win = Tk()

  win.grab_set()
  win.focus()
  win.title("Change Login Info")
  width = 700
  height = 550
  x = ((win.winfo_screenwidth() - width)//2)-30
  y = ((win.winfo_screenheight() - height)//2)-30
  win.geometry(f"{width}x{height}+{x}+{y}")
  win.resizable(0, 0)
  bgimage=PhotoImage(file="images/change_admin_info.png") 
  bg=Label(win, image=bgimage)
  bg.place(x=0,y=0)

  with open("currentadminusrname.txt", "r") as f:
    susrname = StringVar(value=str(f.read()))

  usrname = Entry(win, font=(fontUsed, 13), width=18, state='disabled', textvariable=susrname)
  usrname.place(x=420,y=125)
  scurrent_password = StringVar()
  current_password = Entry(win, font=(fontUsed, 13), width=18, show="*", textvariable=scurrent_password)
  current_password.place(x=486,y=160)

  snew_usrname = StringVar()
  new_usrname = Entry(win, font=(fontUsed, 13), width=20, textvariable=snew_usrname)
  new_usrname.place(x=468,y=215)
  stemp_new_password = StringVar()
  temp_new_password = Entry(win, font=(fontUsed, 13), width=21, show="*", textvariable=stemp_new_password)
  temp_new_password.place(x=460,y=247)
  snew_password = StringVar()
  new_password = Entry(win, font=(fontUsed, 13), width=18, show="*", textvariable=snew_password)
  new_password.place(x=488,y=280)


  editBtn = Button(win, text="Save and Update", bg='#655bd6', fg='white', font=(fontUsed, 14), borderwidth=0, width=14, command=editBtnClick)
  editBtn.place(x=525,y=340)

  editBtn.bind("<Enter>", lambda e: btnMouseEnter(editBtn))
  editBtn.bind("<Leave>", lambda e: btnMouseLeave(editBtn))


  resetBtn = Button(win, text="Reset", bg='#655bd6', fg='white', font=(fontUsed, 11), borderwidth=0, width=8, command=resetBtnClick)
  resetBtn.place(x=300, y=345)

  resetBtn.bind("<Enter>", lambda e: btnMouseEnter(resetBtn))
  resetBtn.bind("<Leave>", lambda e: btnMouseLeave(resetBtn))


  win.mainloop()

# main()