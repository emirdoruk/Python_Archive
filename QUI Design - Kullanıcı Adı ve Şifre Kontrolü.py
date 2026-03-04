from tkinter import *

root = Tk()

#Entry
        
nameEntry = Entry(root)
nameEntry.grid(row=0, column=1)

passwordEntry = Entry(root)
passwordEntry.grid(row=1, column=1)

nameLabel = Label (root, text = "User Name")
nameLabel.grid(row=0, column=0)

passwordLabel = Label (root, text = "Password")
passwordLabel.grid(row=1, column=0)

enterButton = Button (root, text = "Login")
enterButton.grid (row=2, column=1)

controlLabel = Label (root, text = " ")
controlLabel.grid(row=3, column=1)

root.mainloop()
