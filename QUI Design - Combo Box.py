from tkinter import *
from tkinter import ttk#combo box modülü

root = Tk()
root.title("Combo Box")
root.geometry("300x300")

def show():
    if(comboBox.get() == "Rei Ayanami"):
        lable = Label(root, text="You choose first child")
        lable.pack()
    elif(comboBox.get() == "Shinji İkari"):
        lable = Label(root, text="You choose third child")
        lable.pack()
    elif(comboBox.get() == "Asuka Langley Soryu"):
        lable = Label(root, text="You choose second child")
        lable.pack()
    elif(comboBox.get() == "Kaworu Nagisa"):
        lable = Label(root, text="You choose fourth child")
        lable.pack()
    elif(comboBox.get() == "Mari Illustrious Makinami"):
        lable = Label(root, text="You choose fifth child")
        lable.pack()
        
options = (
    "Rei Ayanami",
    "Shinji İkari",
    "Asuka Langley Soryu",
    "Kaworu Nagisa",
    "Mari Illustrious Makinami"
    )

comboBox = ttk.Combobox(root, value=options)
comboBox.pack()

button = Button(root, text="Choose EVA Pilot", command=show)
button.pack()

root.mainloop()
