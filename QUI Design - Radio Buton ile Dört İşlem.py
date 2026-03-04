from tkinter import *

root = Tk()
root.title("Radio Button ile Toplama ve Çıkarma")
root.geometry("200x100")

def click():
    
    if (a.get() == 1):
        sonuc1 = int(entry1.get()) + int(entry2.get())
        label = Label(root, text = str(sonuc1))

    elif (a.get() == 2):
        sonuc2 = int(entry1.get()) - int(entry2.get())
        label = Label(root, text = str(sonuc2))

    elif(a.get() == 3):
        sonuc3 = int(entry1.get()) * int(entry2.get())
        label = Label(root, text = str(sonuc3))

    elif(a.get() == 4):
        sonuc4 = int(entry1.get()) / int(entry2.get())
        label = Label(root, text = str(sonuc4))

    label.grid(row=2, column=1)
    
a = IntVar() 

radioButton1= Radiobutton(root, text = "+", variable = a, value = 1).grid(row=0, column=2)
radioButton2 = Radiobutton(root, text = "-", variable = a, value = 2).grid(row=1, column=2)
radioButton3= Radiobutton(root, text = "*", variable = a, value = 3).grid(row=2, column=2)
radioButton4 = Radiobutton(root, text = "/", variable = a, value = 4).grid(row=3, column=2)

label1 = Label(root, text = "1.")
label2 = Label(root, text = "2.")
label1.grid(row=0, column=0)
label2.grid(row=1, column=0)
entry1 = Entry(root)
entry2= Entry(root)
entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)

button1 = Button(root, text = "click", command = click).grid(row=2, column=0)

root.mainloop()
