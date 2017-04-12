from tkinter import *

root = Tk()
photo = PhotoImage(file="01.png")
label = Label(root, image=photo)
label.pack()

root.mainloop()