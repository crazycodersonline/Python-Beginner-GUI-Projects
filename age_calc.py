from tkinter import *
from tkinter import ttk
import calendar



win = Tk()
win.title("Age Calculator")
win.geometry("400x200")

frame = Frame(win)
frame.pack()


birth_date = Label(frame,text="Date of Birth:",font=("Times" , "17"))
birth_date.pack(side=LEFT)

month = StringVar()
months = list(calendar.month_abbr)[1:]
monthchoosen = ttk.Combobox(frame, width = 5, textvariable = month,font=("Times" , "17"))
monthchoosen.pack(side=LEFT,padx=4)
monthchoosen['values'] = months
monthchoosen.current(0)


dates = StringVar()
datechoosen = ttk.Combobox(frame,background="White", width = 5, textvariable = dates,font=("Times" , "17"))
datechoosen.pack(side=LEFT,padx=4)
datechoosen['values'] = [num for num in range(1,32)]
datechoosen.current(0)


year = StringVar()
year.set("2021")
yearchoosen = Entry(frame, background="White", width = 7, textvariable = year, font=("Times" , "17"),relief= "groove",borderwidth=0 ,border=2)
yearchoosen.pack(side=LEFT,padx=4)

s = ttk.Style()
s.configure('TButton', font=("Times" , "17"))
ok = ttk.Button(win, text='Calculate')
ok.pack(pady=10)


win.mainloop()
