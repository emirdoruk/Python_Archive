from tkinter import *

root = Tk()

root.title("Songs Duration")
root.geometry("400x400")

#Pink Floyd
def WishYouWereHere():
    wywh = Label(root, text="5:34")
    wywh.pack()

def BrainDamage():
    bd = Label(root, text="3:46")
    bd.pack()

def Money():
    m = Label(root, text="6:23")
    m.pack()
    
#The Beatles
def LetItBe():
    lib = Label(root, text="4:03")
    lib.pack()

def HeyJude():
    hj = Label(root, text="7:05")
    hj.pack()

def Yesterday():
    y = Label(root, text="2:05")
    y.pack()
    
#Led Zeppelin
def StairwaytoHeaven():
    sth = Label(root, text="8:02")
    sth.pack()

def Kashmir():
    k = Label(root, text="8:28")
    k.pack()

def RockandRoll():
    rar = Label(root, text="3:40")
    rar.pack()
    
#Red Hot Chili Peppers
def Californication():
    c = Label(root, text="5:29")
    c.pack()

def TheZephyrSong():
    bd = Label(root, text="3:51")
    bd.pack()

def ThisIsthePalace():
    titp = Label(root, text="4:17")
    titp.pack()
    
#Guns N' Roses
def KnockinOnHeavensDoors():
    kothd = Label(root, text="5:36")
    kothd.pack()

def SweetChildOMine():
    scom = Label(root, text="5:54")
    scom.pack()

def ParadiseCity():
    pc = Label(root, text="6:45")
    pc.pack()
    
#AC/DC
def BackInBlack():
    bib = Label(root, text="4:15")
    bib.pack()

def HighwaytoHell():
    hth = Label(root, text="3:28")
    hth.pack()

def Thunderstruck():
    t = Label(root, text="4:52")
    t.pack()

myMenu = Menu(root)
root.config(menu = myMenu)

PinkFloyd = Menu(myMenu)
TheBeatles = Menu(myMenu)
LedZeppelin = Menu(myMenu)
RedHotChiliPeppers = Menu(myMenu)
GunsNRoses = Menu(myMenu)
ACDC = Menu(myMenu)

myMenu.add_cascade(label="Pink Floyd", menu=PinkFloyd)
myMenu.add_cascade(label="The Beatles", menu=TheBeatles)
myMenu.add_cascade(label="Led Zeppelin", menu=LedZeppelin)
myMenu.add_cascade(label="Red Hot Chili Peppers", menu=RedHotChiliPeppers)
myMenu.add_cascade(label="Guns N' Roses", menu=GunsNRoses)
myMenu.add_cascade(label="AC/DC", menu=ACDC)

PinkFloyd.add_command(label="Wish You Were Here", command= WishYouWereHere)
PinkFloyd.add_command(label="Brain Damage", command= BrainDamage)
PinkFloyd.add_command(label="Money", command= Money)

TheBeatles.add_command(label="Let It Be", command= LetItBe)
TheBeatles.add_command(label="Hey Jude", command= HeyJude)
TheBeatles.add_command(label="Yesterday", command= Yesterday)

LedZeppelin.add_command(label="Stairway to Heaven", command= StairwaytoHeaven)
LedZeppelin.add_command(label="Kashmir", command= Kashmir)
LedZeppelin.add_command(label="Rock and Roll", command= RockandRoll)

RedHotChiliPeppers.add_command(label="Californication", command= Californication)
RedHotChiliPeppers.add_command(label="The Zephyr Song", command= TheZephyrSong )
RedHotChiliPeppers.add_command(label="This Is the Palace ", command= ThisIsthePalace )

GunsNRoses.add_command(label="Knockin' On Heaven's Doors", command= KnockinOnHeavensDoors)
GunsNRoses.add_command(label="Sweet Child O' Mine", command= SweetChildOMine)
GunsNRoses.add_command(label="Paradis City", command= ParadiseCity)

ACDC.add_command(label="Back In Black", command= BackInBlack)
ACDC.add_command(label="Highway to Hell", command= HighwaytoHell)
ACDC.add_command(label="Thunderstruck", command= Thunderstruck)

root.mainloop()
