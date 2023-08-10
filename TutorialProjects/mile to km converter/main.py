from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

#Labels
label_miles = Label(text="Miles")
label_miles.grid(column=2, row=0)

label_equal = Label(text="is equal to")
label_equal.grid(column=1, row=1)

label_km = Label(text="Km")
label_km.grid(column=2, row=2)

#Entry
miles_input = Entry(width=7)
print(miles_input.get())
miles_input.grid(column=1, row=0)

km_input = Entry(width=7)
print(km_input.get())
km_input.grid(column=1, row=2)

def calculate():
    if km_input.get():
        km = float(km_input.get())
        miles = km / 1.609
        miles_input.delete(0, END)
        miles_input.insert(END, round(miles, 2))

    elif miles_input.get():
        miles = float(miles_input.get())
        km = miles * 1.609
        km_input.delete(0, END)
        km_input.insert(END, round(km, 2))

#Button
button_calculate = Button(text="Calculate", command=calculate)
button_calculate.grid(column=1, row=3)



window.mainloop()