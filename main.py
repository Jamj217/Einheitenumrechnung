import tkinter as tk


# Formeln Dictionary
formulas = {
    ("Meter", "Meter"): ("Meter = Meter", "=", 1),
    ("Meter", "Kilometer"): ("Kilometer = Meter / 1000", "/", 1000),
    ("Meter", "Zentimeter"): ("Zentimeter = Meter * 100", "*", 100),
    ("Kilometer", "Meter"): ("Meter = Kilometer * 1000", "*", 1000),
    ("Kilometer", "Kilometer"): ("Kilometer = Kilometer", "=", 1),
    ("Kilometer", "Zentimeter"): ("Zentimeter = Kilometer * 100000", "*", 100000),
    ("Zentimeter", "Meter"): ("Meter = Zentimeter * 0.01", "*", 0.01),
    ("Zentimeter", "Kilometer"): ("Kilometer = Zentimeter / 100000", "/", 100000),
    ("Zentimeter", "Zentimeter"): ("Zentimeter = Zentimeter", "=", 1),
}


def convert():
    try:
        value = float(entry_value.get())
        from_unit = from_var.get()
        to_unit = to_var.get()

        # Umrechnung zuerst in Meter
        if from_unit == "Meter":
            meters = value
        elif from_unit == "Kilometer":
            meters = value * 1000
        elif from_unit == "Zentimeter":
            meters = value / 100

        # Von Meter in Ziel-Einheit
        if to_unit == "Meter":
            result = meters
        elif to_unit == "Kilometer":
            result = meters / 1000
        elif to_unit == "Zentimeter":
            result = meters * 100

        result_label.config(text=f"Ergebnis: {result:.4f}")

        # Formel anzeigen
        key = (from_unit, to_unit)
        if key in formulas:
            formula_text, op, factor = formulas[key]
            if op == "=":
                eingesetzt = f"{value} = {result:.4f}"
            elif op == "*":
                eingesetzt = f"{value} * {factor} = {result:.4f}"
            elif op == "/":
                eingesetzt = f"{value} / {factor} = {result:.4f}"
            formula_label.config(text=f"Benutze Umrechnungssformel\n({from_unit} -> {to_unit}):\n{formula_text}\n\nEingesetzt:\n{eingesetzt}")

    except ValueError:
        result_label.config(text="Bitte eine gültige Zahl eingeben")
        formula_label.config(text="Benutze Umrechnungssformel:")


root = tk.Tk()
root.title("Einheitenumrechner")
root.geometry("500x300")  # Höhe erhöht für mehrzeiligen Text

# Frames für Layout
left_frame = tk.Frame(root)
left_frame.pack(side='left', padx=10, pady=10)

right_frame = tk.Frame(root)
right_frame.pack(side='right', padx=10, pady=10)

# Eingabe
tk.Label(left_frame, text="Wert eingeben:").pack(pady=5)
entry_value = tk.Entry(left_frame)
entry_value.pack()

# Auswahl Ausgangseinheit
tk.Label(left_frame, text="Von Einheit:").pack(pady=5)
from_var = tk.StringVar(value="Meter")
from_menu = tk.OptionMenu(left_frame, from_var, "Meter", "Kilometer", "Zentimeter")
from_menu.pack()

# Auswahl Zieleinheit
tk.Label(left_frame, text="In Einheit:").pack(pady=5)
to_var = tk.StringVar(value="Kilometer")
to_menu = tk.OptionMenu(left_frame, to_var, "Meter", "Kilometer", "Zentimeter")
to_menu.pack()

# Button
convert_button = tk.Button(left_frame, text="Umrechnen", command=convert)
convert_button.pack(pady=10)

# Ergebnisanzeige
result_label = tk.Label(left_frame, text="Ergebnis:")
result_label.pack()

# Formelanzeige im rechten Frame
formula_label = tk.Label(right_frame, text="Benutze Umrechnungssformel:", justify='left')
formula_label.pack()

root.mainloop()