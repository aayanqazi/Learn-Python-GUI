from tkinter import *

root = Tk()
topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)
button1 = Button(topFrame, text="Click Me",fg="red")
button2 = Button(topFrame, text="Click Me",fg="green")
button4 = Button(topFrame, text="Click Me",fg="purple")
button3 = Button(bottomFrame, text="Click Me",fg="blue" , width=100)
button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack()

root.mainloop()