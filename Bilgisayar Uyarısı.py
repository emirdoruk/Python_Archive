from tkinter import *
from tkinter import messagebox
import time

root = Tk()
root.title("Warning")
root.geometry("250x100")

def warning():
    local_time = float(entry2.get())
    local_time = local_time * 60
    time.sleep(local_time)
    messagebox.showinfo("Warning", str(entry1.get()))

label1 = Label(root, text="Object: ")
label1.grid(row=0, column=0)
label2 = Label(root, text="Time: ")
label2.grid(row=1, column=0)

entry1 = Entry(root)
entry1.grid(row=0, column=1)
entry2 = Entry(root)
entry2.grid(row=1, column=1)

button = Button(root, text="Start", command = warning)
button.grid(row=0, column=2)

root.mainloop()
