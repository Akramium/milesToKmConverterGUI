from tkinter import *


def calculate():
    miles = input_miles.get()
    res = round(float(miles) * 1.6)
    label_result.config(text=res)


# window
window = Tk()
window.title("Mile to km converter")

# input
input_miles = Entry(width = 5)
input_miles.grid(row=0, column=1)

# label miles
label_miles = Label(text="Miles")
label_miles.grid(row=0, column=3)

# label is equal to
label_is_equal_to = Label(text="is equal to")
label_is_equal_to.grid(row=1, column=0)

# label result
label_result = Label(text="0")
label_result.grid(row=1, column=1)

# label km
label_km = Label(text="Km")
label_km.grid(row=1, column=2)

# button calculate
btn_calculate = Button(text="Calculate", command=calculate)
btn_calculate.grid(row=2, column=1)

window.mainloop()
