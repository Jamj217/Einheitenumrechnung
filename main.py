import tkinter as tk


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

    except ValueError:
        result_label.config(text="Bitte eine gültige Zahl eingeben")


root = tk.Tk()
root.title("Einheitenumrechner")
root.geometry("350x200")

# Eingabe
tk.Label(root, text="Wert eingeben:").pack(pady=5)
entry_value = tk.Entry(root)
entry_value.pack()

# Auswahl Ausgangseinheit
tk.Label(root, text="Von Einheit:").pack(pady=5)
from_var = tk.StringVar(value="Meter")
from_menu = tk.OptionMenu(root, from_var, "Meter", "Kilometer", "Zentimeter")
from_menu.pack()

# Auswahl Zieleinheit
tk.Label(root, text="In Einheit:").pack(pady=5)
to_var = tk.StringVar(value="Kilometer")
to_menu = tk.OptionMenu(root, to_var, "Meter", "Kilometer", "Zentimeter")
to_menu.pack()

# Button
convert_button = tk.Button(root, text="Umrechnen", command=convert)
convert_button.pack(pady=10)

# Ergebnisanzeige
result_label = tk.Label(root, text="Ergebnis:")
result_label.pack()

root.mainloop()