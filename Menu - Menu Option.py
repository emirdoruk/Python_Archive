from tkinter import *

root = Tk()

root.title("Menu Options")
root.geometry("400x400")

def sumNumber():
    sumLabel = Label(root, text="You clicked the sum button")
    sumLabel.pack()

def divNumber():
    divLabel = Label(root, text="You clicked the div button")
    divLabel.pack()

def copyNumber():
    copyLabel = Label(root, text="You clicked the copy button")
    copyLabel.pack()

def pasteNumber():
    pasteLabel = Label(root, text="You clicked the paste button")
    pasteLabel.pack()
    
myMenu = Menu(root) #"Menu" adını isteğin şey yapar

root.config(menu = myMenu) #"Menu"yu kendi oluşturduğumuz "menu"ye bağlar

myFile = Menu(myMenu)
myEdit = Menu(myMenu)
mySearch = Menu(myMenu)

myMenu.add_cascade(label="File", menu=myFile)
myMenu.add_cascade(label="Edit", menu=myEdit)
myMenu.add_cascade(label="Search", menu=mySearch)

myFile.add_command(label="Sum", command= sumNumber)
myFile.add_command(label="Div", command= divNumber)

myEdit.add_command(label="Copy", command= copyNumber)
myEdit.add_command(label="Paste", command= pasteNumber)
root.mainloop()
