from tkinter import *

root = Tk()

def leftClick(event):
    print("Click Left Click Button")
def middleClick(event):
    print("Middle Clicked")
def rightClick(event):
    print("Right Clicked button")

frame = Frame(root, width=300, height=250)
frame.bind("<Button-1>",leftClick)
frame.bind("<Button-3>",rightClick)
frame.bind("<Button-2>",middleClick)
frame.pack()
root.mainloop()
