from tkinter import *
root = Tk()

one = Label(root, text="One", bg="red", fg="white" , height=20)
one.pack(fill=X)

two = Label(root, text="Two", bg="green", fg="white", width=40)
two.pack(side=RIGHT,fill=Y)

three = Label(root, text="Three", bg="blue", fg="white", width=40)
three.pack(side=LEFT,fill=Y)
root.mainloop()
