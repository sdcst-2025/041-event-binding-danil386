import tkinter as tk
from tkinter import *
import playsound as p
from PIL import Image,ImageTk


def playtwister(event):
    print(event)
    p.playsound("The Twister.mp3", block=False)

def playbirds(event):
    print(event)
    p.playsound("Birds.mp3", block=False)

def playfireball(event):
    print(event)
    p.playsound("Fireball.mp3", block=False)

def playcow(event):
    print(event)
    p.playsound("Flying Cow.mp3", block=False)

def playmunchkinmayor(event):
    print(event)
    p.playsound("Munchkin Mayor.mp3", block=False)

def playthunder(event):
    print(event)
    p.playsound("Thunder.mp3", block=False)

def playbark(event):
    print(event)
    p.playsound("Toto Bark.mp3", block=False)

def playwhimper(event):
    print(event)
    p.playsound("Toto Whimper.mp3", block=False)

def playwind(event):
    print(event)
    p.playsound("Wind.mp3", block=False)


window = tk.Tk()
window.geometry("450x475")
window.attributes("-topmost", True)
window.title("WOZ SFX Soundboard")
window.resizable(False,False)

row1=Frame()
row2=Frame()
row3=Frame()

thunderimage = tk.PhotoImage(name="thunder",file="thunder.png")
twisterimage = tk.PhotoImage(name="twister",file="twister.png")
trumpetimage = tk.PhotoImage(name="trumpet",file="trumpet.png")
birdsimage = tk.PhotoImage(name="birds",file="birds.png")
fireballimage = tk.PhotoImage(name="fireball",file="fireball.png")
flyingcowimage = tk.PhotoImage(name="flyingcow",file="flyingcow.png")
totobarkimage = tk.PhotoImage(name="totobark",file="totobark.png")
totowhimperimage = tk.PhotoImage(name="totowhimper",file="totowhimper.png")
windimage = tk.PhotoImage(name="wind",file="wind.png")

sound1=tk.Button(row1,image="birds",text="Birds",width=144,height=155)
sound1.bind("<Button>",playbirds)
sound2=tk.Button(row1,image="fireball",text="Fireball",width=144,height=155)
sound2.bind("<Button>",playfireball)
sound3=tk.Button(row1,image="flyingcow",text="Flying Cow",width=144,height=155)
sound3.bind("<Button>",playcow)
sound4=tk.Button(row2,image="trumpet",text="Munchkin Mayor",width=144,height=155)
sound4.bind("<Button>",playmunchkinmayor)
sound5=tk.Button(row2,image="twister",text="Twister",width=144,height=155)
sound5.bind("<Button>",playtwister)
sound6=tk.Button(row2,image="thunder", text="Thunder",width=200,height=155)
sound6.bind("<Button>",playthunder)
sound7=tk.Button(row3,image="totobark",text="Toto Bark",width=144,height=155)
sound7.bind("<Button>",playbark)
sound8=tk.Button(row3,image="totowhimper",text="Toto Whimper",width=144,height=155)
sound8.bind("<Button>",playwhimper)
sound9=tk.Button(row3,image="wind",text="Wind",width=144,height=155)
sound9.bind("<Button>",playwind)


row1.pack()
sound1.pack(side=LEFT)
sound2.pack(side=LEFT)
sound3.pack(side=LEFT)

row2.pack()
sound4.pack(side=LEFT)
sound5.pack(side=LEFT)
sound6.pack(side=LEFT)

row3.pack()
sound7.pack(side=LEFT)
sound8.pack(side=LEFT)
sound9.pack(side=LEFT)

window.mainloop()