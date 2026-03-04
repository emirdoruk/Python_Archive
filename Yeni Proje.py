from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root = Tk()
root.title("a")
root.geometry("200x100")

def combobox():
    if(comboBox.get() == "1"):
        pass

    elif(comboBox.get() == "2"):
        pass

    elif(comboBox.get() == "3"):
        pass

options = (
    "1",
    "2",
    "3"
    )

comboBox = ttk.Combobox(root, value=options)
comboBox.grid(row=0, column=0)

root.mainloop()
