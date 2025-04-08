import tkinter as tk
from tkinter import *
import playsound as p

window = tk.Tk()
window.geometry("450x475")
window.attributes("-topmost", True)
window.title("Soundboard")
window.resizable(False,False)
window.configure(bg="#fff")

row1=Frame()
row2=Frame()
row3=Frame()


sound1=tk.Button(row1, text="Sound1 Name",width=20,height=10)
sound2=tk.Button(row1, text="Sound2 Name",width=20,height=10)
sound3=tk.Button(row1, text="Sound3 Name",width=20,height=10)
sound4=tk.Button(row2, text="Sound4 Name",width=20,height=10)
sound5=tk.Button(row2, text="Sound5 Name",width=20,height=10)
sound6=tk.Button(row2, text="Sound6 Name",width=20,height=10)
sound7=tk.Button(row3, text="Sound7 Name",width=20,height=10)
sound8=tk.Button(row3, text="Sound8 Name",width=20,height=10)
sound9=tk.Button(row3, text="Sound9 Name",width=20,height=10)


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