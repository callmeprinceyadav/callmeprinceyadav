
from tkinter import *
from tkcalendar import Calendar

root = Tk()


root.geometry("400x300")

cal = Calendar(root, selectmode = 'day',
			year = 2023, month = 8,
			day = 9)

cal.pack(pady = 1)

def grad_date():
	date.config(text = "Selected Date is: " + cal.get_date())


Button(root, text = "Get Date",
	command = grad_date).pack(pady = 20)

date = Label(root, text = "")
date.pack(pady = 20)

# Execute Tkinter
root.mainloop()
