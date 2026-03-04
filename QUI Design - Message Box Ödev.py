from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("100x40")

def askYesNo():
    response = messagebox.askyesno ("Toplama İşlemi", "Toplama İşlemi Yapmak İstiyor musunuz?")

    if (response == 1):
        Yes =Tk()
        Yes.title("Toplama İşlemi")
        Yes.geometry("400x100")

        def topla():
            sonuc = float(e1.get()) + float(e2.get())
            sonucLabel = Label(Yes, text = sonuc)
            sonucLabel.grid(row=2, column=1)

        Label(Yes, text="Birinci Toplanan:").grid(row=0)
        Label(Yes, text="İkinci Toplanan:").grid(row=1)
        Label(Yes, text="Toplam:").grid(row=2)
        
        e1= Entry(Yes)
        e1.grid(row=0, column=1)
        e2= Entry(Yes)
        e2.grid(row=1, column=1)

        arti = Button(Yes,text="+", command=topla)
        arti.grid(row=0, column=2)

    elif (response == 0):
        pass

popButton = Button(root, text = "Ask Yes / No", command = askYesNo)
popButton.pack()

root.mainloop()

