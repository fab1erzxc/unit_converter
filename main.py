import tkinter as tk

# Conversion factors
conversion_factors = {
    "lbs": {
        "kgs": 0.453592
    },
    "kgs": {
        "lbs": 2.20462
    },
    "m": {
        "in": 39.3701,
        "ft": 3.28084,
        "yd": 1.09361,
        "mi": 0.000621371
    },
    "in": {
        "m": 0.0254
    },
    "ft": {
        "m": 0.3048
    },
    "yd": {
        "m": 0.9144
    },
    "mi": {
        "m": 1609.34
    },
    "s": {
        "h": 0.000277778
    },
    "h": {
        "s": 3600
    },
    "A": {
        "A": 1
    },
    "K": {
        "°F": lambda x: x * 9 / 5 - 459.67,
        "°C": lambda x: x - 273.15
    },
    "°F": {
        "K": lambda x: (x + 459.67) * 5 / 9,
        "°C": lambda x: (x - 32) * 5 / 9
    },
    "°C": {
        "K": lambda x: x + 273.15,
        "°F": lambda x: x * 9 / 5 + 32
    }
}


def convert_units():
    from_unit = from_dropdown.get()
    to_unit = to_dropdown.get()
    input_value = float(input_entry.get())

    if from_unit == to_unit:
        result_label.config(text=f"Result: {input_value} {from_unit}")
    elif from_unit in conversion_factors and to_unit in conversion_factors[from_unit]:
        conversion_factor = conversion_factors[from_unit][to_unit]
        result = input_value * conversion_factor
        result_label.config(text=f"Result: {result} {to_unit}")
    elif from_unit in conversion_factors and to_unit in conversion_factors[from_unit].keys():
        conversion_function = conversion_factors[from_unit][to_unit]
        result = conversion_function(input_value)
        result_label.config(text=f"Result: {result} {to_unit}")
    else:
        result_label.config(text="Invalid conversion!")


# Create the GUI window
window = tk.Tk()
window.title("Unit Converter")

# Create input entry field
input_label = tk.Label(window, text="Value:")
input_label.pack()
input_entry = tk.Entry(window)
input_entry.pack()

# Create "From" unit dropdown
from_label = tk.Label(window, text="From:")
from_label.pack()
from_dropdown = tk.StringVar(window)
from_dropdown.set("lbs")  # Default value
from_menu = tk.OptionMenu(window, from_dropdown, *conversion_factors.keys())
from_menu.pack()

# Create "To" unit dropdown
to_label = tk.Label(window, text="To:")
to_label.pack()
to_dropdown = tk.StringVar(window)
to_dropdown.set("kgs")  # Default value
to_menu = tk.OptionMenu(window, to_dropdown, *conversion_factors.keys())
to_menu.pack()

# Create conversion button
convert_button = tk.Button(window, text="Convert", command=convert_units)
convert_button.pack()

# Create label for displaying the result
result_label = tk.Label(window, text="Result: ")
result_label.pack()

# Run the GUI loop
window.mainloop()
