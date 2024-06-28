from tkinter import *

window = Tk()
window.title("Mile to Kilometer Converter")
window.config(padx=50, pady=50)


def button_clicked():
    mile = float(input.get())
    kilometer = round(mile * 1.609)
    kms_ans.config(text=kilometer)


equalto = Label(text="is equal to")
equalto.grid(column=0, row=1)

miles = Label(text="Miles")
miles.grid(column=2, row=0)

km = Label(text="Km")
km.grid(column=2, row=1)

input = Entry(width=20)
input.grid(column=1, row=0)

kms_ans = Label(text="0")
kms_ans.grid(column=1, row=1)

button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

window.mainloop()
