from tkinter import *

root = Tk()

def click():
    label = Label(root, text = "Merhaba")
    label.grid(row=2, column=0)
    
button = Button(root, text = "Click Me",  command = click, padx = 50, pady = 50, bg= "yellow", fg = "black")
button.grid(row=1, column=0)

root.mainloop()
