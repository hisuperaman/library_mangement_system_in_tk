from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk


def get_frames(gif):
    """generates each frame of a gif"""
    try:
        while True:
            gif.seek(gif.tell()+1)
            yield gif.copy()
    except:
        return


def update_animation():
    """updates the animation of gif by changing the image of label to current frame"""
    global current_idx
    
    running_label.config(image=gif_frames[current_idx])
    current_idx = (current_idx+1) % len(gif_frames)
    if pb['value']<98:
        # win.after(100, update_animation)
        win.after(running_gif.info['duration'], update_animation)


def update_pb():
    """update the value of progress bar"""
    if pb['value']<100:
        pb['value'] += 1
        pb_frame.after(40, update_pb)
    else:
        win.destroy()
        main.main_func()


# configuring window
win = Tk()
win.title("Starting")
width = 600
height = 350
x = (win.winfo_screenwidth()-width) // 2
y = ((win.winfo_screenheight()-height) // 2)-30
win.geometry(f"{width}x{height}+{x}+{y}")
# removing the window buttons of root window
win.overrideredirect(1)

# displaying background image
bg_img = Image.open('images/splash_screen/bg.png')
bg = ImageTk.PhotoImage(bg_img)
bg_label = Label(win, image=bg)
bg_label.pack()

# changing style of progress bar
style = ttk.Style()
style.theme_use('default')
style.configure("TProgressbar", background='blue', troughcolor="#655bd6", thickness=5)

# displaying progress bar
pb_frame = Frame(win)
pb = ttk.Progressbar(pb_frame, orient='horizontal', mode='determinate', length=400, style="TProgressbar")
pb.pack()
pb_frame.place(x=110, y=270)
# calling update function for progress bar
update_pb()


# storing each frame of gif into a list
running_gif = Image.open("images/splash_screen/running.gif")
gif_frames = [ImageTk.PhotoImage(img) for img in get_frames(running_gif)]
current_idx = 0

# displaying current frame of gif
running_label = Label(bg_label, image=gif_frames[current_idx], bg="#4e61da")
running_label.place(x=50, y=30)

# updating the gif frame
update_animation()

import main

win.mainloop()