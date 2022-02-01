from cgitb import text
from tkinter import *
from tkinter import ttk
import calendar
import datetime
from datetime import date

def calc():
    year_of_birth = int(year.get())
    monthofbirth = int(months.index(month.get()) + 1)
    dayofbirth = int(date_stringvar.get())

    today = datetime.datetime.now()
    year_now = int(today.year)
    month_now = int(today.month)
    day_now = int(today.day)

    d0 = date(year_of_birth, monthofbirth , dayofbirth)
    d1 = date(year_now, month_now, day_now)

    delta = d1-d0
    totaldays = delta.days
    age_total = totaldays // 365

    age.config(text=f"{age_total} years old")



win = Tk()
win.title("Age calculator")
win.geometry("400x200")

frame = Frame(win)
frame.pack()

birth_date = Label(frame,text="Date of Birth:",font=("Times","17"))
birth_date.pack(side=LEFT)

month = StringVar()
months = list(calendar.month_abbr)[1:]
monthchoosen = ttk.Combobox(frame,font=("Times","17"),width=5,textvariable=month)
monthchoosen.pack(side=LEFT,padx=5)
monthchoosen['values'] = months
monthchoosen.current(0)

date_stringvar = StringVar()
datechoosen = ttk.Combobox(frame,font=("Times","17"),width=5,textvariable=date_stringvar)
datechoosen.pack(side=LEFT,padx=5)
datechoosen['values'] = [num for num in range(1,32)]
datechoosen.current(0)

year = StringVar()
year.set("2002")
yearchoosen = Entry(frame,width=7,font=("Times","17"),relief='groove',border=2,textvariable=year)
yearchoosen.pack(side=LEFT, padx=5)

calculate = ttk.Button(win,text="Calculate",command=calc)
calculate.pack(pady=10)

age = Label(win ,font=("Times","17"),width=9)
age.pack()

win.mainloop()