from tkinter import *
import time
def digital():
    d=time.strftime("%H:%M:%S:%p")
    clock.config(text=d)
    clock.after(100,digital)
root=Tk()
root.title("Digital Clock-suvetha")
clock=Label(root,font=("calibri",100,"italic"),bg="blue")
clock.grid(row=6,column=1)
digital()
root.mainloop()
