from tkinter import *
 
master = Tk()
 
var = IntVar()
 
c = Checkbutton(master, text="我是帅锅", variable=var)
c.pack()
 
mainloop()