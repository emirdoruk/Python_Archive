from tkinter import *
from PIL import Image, ImageTk # Resim Modülü

root = Tk()
root.title("Open New Page With A Image")
root.geometry("400x400")

def showImage():
    newPen = Toplevel() # Yeni pencere açar, alttaki pencereyi etkisiz kılar
    newPen.title("aPPa")
    newPen.geometry("346x346")

    myImage = ImageTk.PhotoImage(Image.open("C:/Users/doruk/Desktop/Yeni klasör/Shit Post/aPPa.jpg"))
    label = Label(newPen, image = myImage)
    label.pack()

    newPen.mainloop()
    
button = Button(root, text="Show Image", command = showImage)
button.pack()

root.mainloop()

