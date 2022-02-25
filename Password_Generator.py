import random
from tkinter import *


root = Tk()
root.geometry("500x400")
root.title("Password Generator")


def exit():
    root.destroy()
    #l2.config(text= "        ")
def generate():
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    special = "[]():*/-_#"
    all = lower + upper + numbers + special
    lenght = 8
    password = "".join(random.sample(all,lenght))
    l2.config(text = password)
def ngenerate():
    generate()
    

l = Label(
    root,text = "Password Generator",font="Normal 30 bold",    
    ).pack(pady= 10)
f = Frame(root)
f.pack()
l1 = Label(f,text = "Password: ", font="Normal 20 italic",    )
l1.pack()
l2 = Label(f,text = "             ",font = "normal 20 bold",bg = "grey",width = 15 ,borderwidth = 2,relief = "solid")
l2.pack()
b = Button(f,text= "Generate", font= "normal 20 bold",
            bg = 'green',width=10,borderwidth=2,command=generate,relief='sunken'
            ).pack(padx =10 ,pady=20)
b1 = Button(f,text="New Password",font= "normal 10 bold",bg = 'blue',command = ngenerate,relief= 'groove').pack(side=LEFT,padx=6,pady=20)
b2 = Button(f,text = "Exit", font = "Normal 10 bold", width=5,bg = 'red',command=exit).pack(side=RIGHT)

root.mainloop()
