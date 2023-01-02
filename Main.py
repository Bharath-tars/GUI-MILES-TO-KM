from tkinter import *

t = Tk()
t.title("Km Converter")
t.config(padx=20, pady=20)

e = Entry(width=5)
e.insert(END, string="")
e.grid(row=0, column=1)
l1 = Label(text="Miles", font=("Arial", 16, "normal"))
l1.grid(row=0, column=2)
l2 = Label(text="is equal to", font=("Arial", 16, "normal"))
l2.grid(row=1, column=0)
l3 = Label(text="KM", font=("Arial", 16, "normal"))
l3.grid(row=1, column=2)


def calculate():
    value = e.get()
    calculated_value = float(value) * 1.609
    l4.config(text=int(calculated_value))


l4 = Label(text="0", font=("Arial", 16, "normal"))
l4.grid(column=1, row=1)
b = Button(text="Calculate", command=calculate)
b.grid(column=1, row=2)

t.mainloop()
