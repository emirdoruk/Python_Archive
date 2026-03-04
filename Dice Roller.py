import random
from tkinter import *

root = Tk()
root.title("Dice Roller")
root.geometry("100x200")

d4_possible_actions = ("1", "2", "3", "4")
d6_possible_actions = ("1", "2", "3", "4", "5", "6")
d8_possible_actions = ("1", "2", "3", "4", "5", "6", "7", "8")
d10_possible_actions = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10")
d12_possible_actions = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12")
d20_possible_actions = ("1", "2", "3", "4", "5", "6", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20")

def d4():
    d4_action = random.choice(d4_possible_actions)
    label4 = Label(root, text=d4_action).grid(row=3, column=2)

def d6():
    d6_action = random.choice(d6_possible_actions)
    label6 = Label(root, text=d6_action).grid(row=3, column=2)

def d8():
    d8_action = random.choice(d8_possible_actions)
    label8 = Label(root, text=d8_action).grid(row=3, column=2)

def d10():
    d10_action = random.choice(d10_possible_actions)
    label10 = Label(root, text=d10_action).grid(row=3, column=2)

def d12():
    d12_action = random.choice(d12_possible_actions)
    label12 = Label(root, text=d12_action).grid(row=3, column=2)

def d20():
    d20_action = random.choice(d20_possible_actions)
    label20 = Label(root, text=d20_action).grid(row=3, column=2)


d4button = Button(root, text="d4", command = d4)
d4button.grid(row=1, column=0)

d6button = Button(root, text="d6", command = d6)
d6button.grid(row=2, column=0)

d8button = Button(root, text="d8", command = d8)
d8button.grid(row=3, column=0)

d10button = Button(root, text="d10", command = d10)
d10button.grid(row=4, column=0)

d12button = Button(root, text="d12", command = d12)
d12button.grid(row=5, column=0)

d20button = Button(root, text="d20", command = d20)
d20button.grid(row=6, column=0)

root.mainloop()

