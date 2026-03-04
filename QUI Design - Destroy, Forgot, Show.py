from tkinter import *

root = Tk()

root.title("Destroy - Forget")
root.geometry("400x400")

def click():
    global label
    label = Label(root, text="Welcome " + entry.get() )
    label.pack()

def clear():
    label.pack_forget()
    
def destroy():
    label.destroy()
    
def show():
    label.pack()
    
entry = Entry(root, text="write your name")
entry.pack()

nameButton = Button(root, text="click me", command = click)
nameButton.pack()

clearButton = Button(root, text="clear me", command = clear)
clearButton.pack()

destroyButton = Button(root, text="destory me", command = destroy)
destroyButton.pack()

showButton = Button(root, text="show me", command = show)
root.mainloop()
