from tkinter import *

root = Tk()
root.title("Menü")
root.geometry("200x100")

def click():
    
    if (a.get() == 1):
        label = Label(root, text = "30.00")

    elif (a.get() == 2):
        label = Label(root, text = "38.00")

    elif(a.get() == 3):
        label = Label(root, text = "30.00")

    label.grid(row=1, column=2)
    
a = IntVar() 

radioButton1= Radiobutton(root, text = "Tavuk Sote", variable = a, value = 1).grid(row=0, column=0)
radioButton2 = Radiobutton(root, text = "Et Sote", variable = a, value = 2).grid(row=1, column=0)
radioButton3= Radiobutton(root, text = "Balık Sote", variable = a, value = 3).grid(row=2, column=0)

button1 = Button(root, text = "fiyat", command = click).grid(row=0, column=1)

root.mainloop()
