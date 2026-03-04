from tkinter import *

root = Tk()
root.title("Boy Kilo İndeksi")
root.geometry("400x400")

def  calculate ():
    bki= float(WeightEntry.get())/(float(HeightEntry.get())**2)

    if(bki <= 18.5): #Zayıf
        label = Label(ThinPen, text= "Zayıfsınız.")
        label.pack()

    elif(bki > 18.5 and bki <= 25): #Normal
        label = Label(NormalPen, text= "Normal kilodasınız.")
        label.pack()

    elif(bki > 25 and bki <= 30):  #Şişman
        label = Label(FatPen, text= "Şişmansınız.")
        label.pack()


    else: #Obez
        label = Label(ObesePen, text= "Obezsiniz")
        label.pack()

WeightLabel = Label(root, text = "Weight: ")
WeightLabel.grid(row=0, column=0)
WeightEntry = Entry(root)
WeightEntry.grid(row=0, column=1)

HeightLabel = Label(root, text = "Height: ")
HeightLabel.grid(row=1, column=0)
HeightEntry = Entry(root) 
HeightEntry.grid(row=1, column=1)

CalculateButton = Button(root, text = "Calculate: ", command = calculate)
CalculateButton.grid(row=0, column=2 )

root.mainloop()
