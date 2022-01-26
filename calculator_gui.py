from tkinter import *
from tkinter import font

win = Tk()
win.title("Calculator")

def number(selected):
    e.insert("end",str(selected))

def clear_one():
    val = e.get()
    e.delete(len(val)-1,"end")

def clear_f():
    e.delete(0,"end")

def equal_f():
    exp = e.get()
    e.delete(0,"end")
    try:
        e.insert(0,eval(exp))
    except Exception as error:
        e.insert(0,"Invalid Expression")
    
e = Entry(win,font=("lcd 20"),width=15,justify="right")
e.grid(row=1,column=1,columnspan=4,ipadx=0,ipady=10)

clear = Button(win,text="x",command=clear_one)
clear.grid(row=2,column=1,ipadx=20,ipady=20,padx=0,pady=0)

clear_2 = Button(win,text="C",command=clear_f)
clear_2.grid(row=2,column=2,ipadx=20,ipady=20)

equal = Button(win,text="=",command=equal_f)
equal.grid(row=2,column=3,ipadx=20,ipady=20)


div = Button(win,text="/",command=lambda:number("/"))
div.grid(row=2,column=4,ipadx=20,ipady=20)





one = Button(win,text=1,command=lambda:number(1))
one.grid(row=3,column=1,ipadx=20,ipady=20)

two= Button(win,text=2,command=lambda:number(2))
two.grid(row=3,column=2,ipadx=20,ipady=20)

three = Button(win,text=3,command=lambda:number(3))
three.grid(row=3,column=3,ipadx=20,ipady=20)

mul = Button(win,text="*",command=lambda:number("*"))
mul.grid(row=3,column=4,ipadx=19,ipady=20)

four = Button(win,text=4,command=lambda:number(4))
four.grid(row=4,column=1,ipadx=20,ipady=20)

five= Button(win,text=5,command=lambda:number(5))
five.grid(row=4,column=2,ipadx=20,ipady=20)

six = Button(win,text=6,command=lambda:number(6))
six.grid(row=4,column=3,ipadx=20,ipady=20)

minus = Button(win,text="-",command=lambda:number("-"))
minus.grid(row=4,column=4,ipadx=20,ipady=20)

seven = Button(win,text=7,command=lambda:number(7))
seven.grid(row=5,column=1,ipadx=20,ipady=20)

eight= Button(win,text=8,command=lambda:number(8))
eight.grid(row=5,column=2,ipadx=20,ipady=20)

nine = Button(win,text=9,command=lambda:number(9))
nine.grid(row=5,column=3,ipadx=20,ipady=20)

add = Button(win,text="+",command=lambda:number("+"))
add.grid(row=5,column=4,ipadx=20,ipady=60,rowspan=2)


zero= Button(win,text=0,command=lambda:number(0))
zero.grid(row=6,column=1,ipadx=20,ipady=20)


zero_2 = Button(win,text="00",command=lambda:number("00"))
zero_2.grid(row=6,column=2,ipadx=18,ipady=20)

point = Button(win,text=".",command=lambda:number("."))
point.grid(row=6,column=3,ipadx=20,ipady=20)



win.mainloop()