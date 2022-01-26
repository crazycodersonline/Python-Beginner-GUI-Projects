from audioop import add
from cgitb import text
from tkinter import *

def cal(option):
    num1 = float(num1_e.get())
    num2 = float(num2_e.get())
    if(option == "+"):
        res = num1 + num2
    elif(option == "-"):
        res = num1 - num2

    elif(option == "*"):
        res = num1 * num2
    else:
        res = num1 / num2

    res_o.config(text=str(res))



win = Tk()
win.title("Calculator")
win.geometry("300x250")

num1_l = Label(win,text="Enter First Number:",font=("Helvatical" , 15))
num1_l.pack()
num1_e = Entry(win,font=("Helvatical" , 15))
num1_e.pack()

num2_l = Label(win,text="Enter Second Number:",font=("Helvatical" , 15))
num2_l.pack()
num2_e = Entry(win,font=("Helvatical" , 15))
num2_e.pack()

frame = Frame(win)
frame.pack(pady=10)

add_b = Button(frame,text="Add" ,command=lambda:cal("+"))
add_b.pack(side=LEFT,padx=10)

sub_b = Button(frame,text="Subtract",command=lambda:cal("-"))
sub_b.pack(side=LEFT,padx=10)

mul_b = Button(frame,text="Multiply",command=lambda:cal("*"))
mul_b.pack(side=LEFT,padx=10)

divide_b = Button(frame,text="Divide",command=lambda:cal("/"))
divide_b.pack(side=LEFT,padx=10)

res_l = Label(win,text="Result:",font=("Helvatical" , 15))
res_l.pack()

res_o = Label(win,bg="White",width=20,font=("Helvatical" , 15),relief="sunken")
res_o.pack()




win.mainloop()