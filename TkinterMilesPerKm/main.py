from tkinter import *


def mile_to_km():
    miles = float(input_miles.get())
    km = round(miles * 1.60934, 2)
    km_value_label.config(text=f"{km}")


screen = Tk()
screen.title("Miles to Km Converter")
screen.config(padx=20, pady=20)

input_miles = Entry(width=7)
input_miles.grid(row=0, column=1)

miles_label = Label(text="Miles", font=("Arial", 10, "bold"))
miles_label.grid(row=0, column=2)

equals_label = Label(text="is equal to", font=("Arial", 10, "bold"))
equals_label.grid(row=1, column=0)

km_value_label = Label(text="0", font=("Arial", 10, "bold"))
km_value_label.grid(row=1, column=1)

km_label = Label(text="Km", font=("Arial", 10, "bold"))
km_label.grid(row=1, column=2)

calculate_button = Button(text="Calculate", command=mile_to_km)
calculate_button.grid(row=2, column=1)

screen.mainloop()
