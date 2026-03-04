from tkinter import *

root = Tk()

def  new():
    New = Tk()
    New.title ("New")
    New.geometry("400x400")
        
    cikis = Button (New, text="Close", command = new.quit) # "pencere adı" + . + quit --> pencere kapatma
root.title("Menu")
root.geometry("400x400")

myMenu = Menu(root)
root.config(menu = myMenu)

newmenu = Menu(myMenu)
myMenu.add_cascade(label="File", menu = newmenu)
newmenu.add_command(label="New", command = new)

root.mainloop()
