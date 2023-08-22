from tkinter import *
from tkinter import messagebox
import backend
from btn_hover import *


def main(root):
# def main():
  fontUsed = "Segoe UI"


  def editBtnClick():
    if new_fine.get()!="":
      if new_fine.get().isnumeric():
        try:
            backend.edit_fine(new_fine.get())
            messagebox.showinfo("Done", f"Fine rate changed to {new_fine.get()} successfully!", parent=win)
            win.destroy()
        except Exception as e:
            e = str(e).lower()
            if "out of range" in e:
                messagebox.showinfo("Fine", "Too big fine value!", parent=win)
            else:
                messagebox.showerror("Error", "Something went wrong!", parent=win)

      else:
        messagebox.showinfo("Fine", "Fine must be a number!", parent=win)
    else:
        messagebox.showinfo("Fine", "Fine field must not be empty!", parent=win)

  def resetBtnClick():
    snew_fine.set("")
    win.focus()
        

  win = Toplevel(root)
  # win = Tk()

  win.grab_set()
  win.focus()
  win.title("Edit Fine")
  width = 700
  height = 550
  x = ((win.winfo_screenwidth() - width)//2)-30
  y = ((win.winfo_screenheight() - height)//2)-30
  win.geometry(f"{width}x{height}+{x}+{y}")
  win.resizable(0, 0)
  bgimage=PhotoImage(file="images/edit_fine.png") 
  bg=Label(win, image=bgimage)
  bg.place(x=0,y=0)

  scurrent_fine = StringVar(value=backend.get_fine_val())
  current_fine = Entry(win, font=(fontUsed, 13), width=10, state='disabled', textvariable=scurrent_fine)
  current_fine.place(x=435,y=168)

  snew_fine = StringVar()
  new_fine = Entry(win, font=(fontUsed, 13), width=14, textvariable=snew_fine)
  new_fine.place(x=400,y=218)


  editBtn = Button(win, text="Save and Update", bg='#655bd6', fg='white', font=(fontUsed, 14), borderwidth=0, width=14, command=editBtnClick)
  editBtn.place(x=525,y=270)

  editBtn.bind("<Enter>", lambda e: btnMouseEnter(editBtn))
  editBtn.bind("<Leave>", lambda e: btnMouseLeave(editBtn))


  resetBtn = Button(win, text="Reset", bg='#655bd6', fg='white', font=(fontUsed, 11), borderwidth=0, width=8, command=resetBtnClick)
  resetBtn.place(x=300, y=275)

  resetBtn.bind("<Enter>", lambda e: btnMouseEnter(resetBtn))
  resetBtn.bind("<Leave>", lambda e: btnMouseLeave(resetBtn))



  win.mainloop()

# main()