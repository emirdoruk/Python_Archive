from tkinter import *

root = Tk()

root.title("CheckButton")
root.geometry("100x100")

def fiyat():
    if(v1.get() == "ONtavuk"):
        fiyatLabel = Label(root, text = "Tavuk 25 TL'dir.")
        fiyatLabel.pack()
    elif(v1.get() == "OFFtavuk"):
        fiyatLabel = Label(root, text = "Tavuk seçilmedi.")
        fiyatLabel.pack()
    elif(v2.get() == "ONpizza"):
        fiyatLabel = Label(root, text = "Pizza 35 TL'dir.")
        fiyatLabel.pack()
    elif(v2.get() == "OFFpizza"):
        fiyatLabel = Label(root, text = "Pizza seçilmedi.")
        fiyatLabel.pack()

v1 = StringVar()
v2 = StringVar()

checkButton1 = Checkbutton(root, text = "Tavuk", variable = v1, onvalue = "ONtavuk", offvalue = "OFFtavuk")
checkButton1.deselect()
checkButton1.pack()

checkButton2 = Checkbutton(root, text = "Pizza", variable = v2, onvalue = "ONpizza", offvalue = "OFFpizza")
checkButton2.deselect()
checkButton2.pack()

fiyatButton = Button(root, text = "Fiyat Göster", command = fiyat)
fiyatButton.pack()

root.mainloop()

