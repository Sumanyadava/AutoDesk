import tkinter

import pyautogui as pg
import time
import webbrowser as wbs

from tkinter import *
import tkinter.messagebox as msg




# chrome defined here
chrome = wbs.get('C:/Program Files/Google/Chrome/Application/chrome.exe %s')


# all sites defined here
sites = [["youtube","https://youtube.com"],["wiki","https://wiki.com"]]

app_env = 0;

def openApp(App_name):
    pg.press('win')
    pg.write(App_name)
    pg.press('enter')
    pg.sleep(2)

def allignApp(position):
    pg.hotkey('win',position)


def getOPT():
    app_env = var.get()
    # pyauto start here


    if (app_env == 1):

        # programming vscode chrome youtube music

        openApp('vscode')
        allignApp('left')

        wbs.open(sites[0][1])
        allignApp('right')

        openApp('music')
        pg.sleep(3)
        pg.press('space')

        chrome.open("https://google.com")

        openApp('task')

        window.destroy()


    elif (app_env == 2):
        # gaming counterstrike music

        openApp('counter')

        openApp('music')
        pg.sleep(2)
        pg.press('space')

        window.destroy()

    elif (app_env == 3):
        # content creation primer photoshp aftereffect

        openApp('premiere')
        pg.sleep(3)
        openApp('photoshop')

        window.destroy()

    elif (app_env == 4):
        # research obsidian word youtube

        openApp('obsid')
        openApp('word')
        allignApp('left')
        wbs.open(sites[0][1])
        allignApp('right')

        window.destroy()

    elif(app_env == 5):
        e = Entry(window, width=50)

        def open_cus():
            openApp(e.get())
            window.destroy()

        b2 = Button(window, text="click here", command=open_cus)

        e.pack()
        b2.pack()


    elif(app_env == 6):
        window.destroy()



    else:
        print("over")




    # window.destroy()


def update_time():
    my_label.config(text="times up ")
    b1.invoke()







# main start from here


window = Tk()
window.title("welcome reflx")
window.minsize(width=400,height=600)
# window.maxsize(width=500,height=500)



var = IntVar()

var.set(4)

Label(window,text="Which enviroment you want ",font="lucida 19 bold").pack()

Label(window,text="Vs code ,Chrome Youtube Music",pady=20).pack()
radio = Radiobutton(window,text="Programming",variable=var,value=1,padx=34).pack(anchor="w")


Label(window,text="CounterStrike, Music",pady=20).pack()
radio = Radiobutton(window,text="Gaming",variable=var,value=2,padx=34).pack(anchor="w")

Label(window,text="photoshop,primere pro, Music").pack()
radio = Radiobutton(window,text="Content",variable=var,value=3,padx=34).pack(anchor="w")

Label(window,text="obsidian word Youtube").pack()
radio = Radiobutton(window,text="Research",variable=var,value=4,padx=34).pack(anchor="w")

radio = Radiobutton(window,text="Custom",variable=var,value=5,padx=34).pack(anchor="w")

radio = Radiobutton(window,text="Exit",variable=var,value=6,padx=34).pack(anchor="w")

# b1 = Button(window,text="click Here",pady=10,command=getOPT).pack()

b1 = Button(window,text="Click Here",pady=10,   command=getOPT)


my_label = Label(window,text="you have 10 sec to choose")

my_label.pack(pady=20)

my_label.after(5000, update_time)

b1.pack()

window.mainloop()



'''
code logic 

from pyautogui open app and aligment
open_app function and aligment function 

both tak input as a string 

there are 6 options accordingly 
chosse time 5 sec 

afte that a button in called which is in update time event  

option 5 have custom which you write your app 

option 6 exit the app
'''







# app_env = int(pg.prompt("which enviroment you want from 1-3"))
