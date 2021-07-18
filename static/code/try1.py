'''
    Author: Aryan
    Date: 18 march 2021
    Purpose: Make calculater
'''
from tkinter import *
import Mytools
from functools import partial

def call(n):
    print(n)
    if n == "c":
        value.set("")
        var.set("")
        entry.update()
        l = Label(text=var.get(),font="lucida 13 bold")
        l.place(x=50,y=5)

    elif n == "=":
        ans = calculate()
        value.set(f"{ans}")
        var.set(var.get()+f" = {ans}")
        entry.update()
        l = Label(text=var.get(),font="lucida 13 bold")
        l.place(x=50,y=5)
    else:
        value.set(value.get()+str(n))
        entry.update()
        var.set(var.get()+str(n))
        l = Label(text=var.get(),font="lucida 13 bold")
        l.place(x=50,y=5)

def calculate():
    return eval(entry.get())
        
window = Mytools.GUI(52,325,"Calculater")
value = StringVar()
entry = Entry(window, textvariable=value,font="lucida 30 bold")
entry.pack(padx=10,ipadx=10,pady=40)
fo = "lucida 25 bold"
var = StringVar()

l = Label(text=var.get(),font="lucida 13 bold")
l.place(x=50,y=5)
f = Frame(window,bg="gray")
f.pack()

i = 9
while 1:
    # if i
    Button(f,text=i,font=fo,padx=18,pady=5,borderwidth=3,command=partial(call,i)).pack(side=LEFT)
    print(i)
    if i == 7:
        Button(f,text="+",font=fo,borderwidth=3,command=partial(call,"+"),padx=16,pady=5).pack(side=LEFT)
        f = Frame(window,bg="gray")
        f.pack()
    if i == 4:
        Button(f,text="-",font=fo,borderwidth=3,command=partial(call,"-"),padx=20,pady=5).pack(side=LEFT)
        f = Frame(window,bg="gray")
        f.pack()
    if i == 1:
        Button(f,text="x",font=fo,borderwidth=3,command=partial(call,"*"),padx=15,pady=5).pack(side=LEFT)
        f = Frame(window,bg="gray")
        f.pack()
    if i == 0:
        Button(f,text="00",font=fo,borderwidth=3,command=partial(call,"00"),padx=10,pady=5).pack(side=LEFT)
        Button(f,text="%",font=fo,borderwidth=3,command=partial(call,"%"),padx=15,pady=5).pack(side=LEFT)
        Button(f,text=".",font=fo,borderwidth=3,command=partial(call,"."),padx=15,pady=5).pack(side=LEFT)
        f = Frame(window,bg="gray")
        f.pack()
        Button(f,text="=",font=fo,borderwidth=3,command=partial(call,"="),padx=18,pady=5).pack(side=LEFT)
        Button(f,text="/",font=fo,borderwidth=3,command=partial(call,"/"),padx=18,pady=5).pack(side=LEFT)
        Button(f,text="c",font=fo,borderwidth=3,command=partial(call,"c"),padx=18,pady=5).pack(side=LEFT)
        Button(f,text="**",font=fo,borderwidth=3,command=partial(call,"**"),padx=18,pady=5).pack(side=LEFT)
        break
    i-=1

window.mainloop()