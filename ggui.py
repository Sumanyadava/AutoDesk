from tkinter import *
import tkinter.messagebox as msg

window = Tk()
window.title("welcome reflx")
window.minsize(width=400,height=300)
# window.maxsize(width=500,height=500)

def getOPT():

    msg.showinfo(var.get())




var = IntVar()

var.set(1)

Label(window,text="Which enviroment you want ",font="lucida 19 bold").pack()

radio = Radiobutton(window,text="Programming",variable=var,value=1,padx=34).pack(anchor="w")

radio = Radiobutton(window,text="Gaming",variable=var,value=2,padx=34).pack(anchor="w")

radio = Radiobutton(window,text="Content",variable=var,value=3,padx=34).pack(anchor="w")

radio = Radiobutton(window,text="Research",variable=var,value=4,padx=34).pack(anchor="w")

Button(window,text="click Here",pady=10,command=getOPT).pack()



window.mainloop()