import tkinter as tk

# Liste für die letzten Umrechnungen
history = []


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
        else:
            raise ValueError("Ungültige Ausgangseinheit")

        # Von Meter in Ziel-Einheit
        if to_unit == "Meter":
            result = meters
        elif to_unit == "Kilometer":
            result = meters / 1000
        elif to_unit == "Zentimeter":
            result = meters * 100
        else:
            raise ValueError("Ungültige Zieleinheit")

        result_label.config(text=f"Ergebnis: {result:.4f}")

        # Umrechnung zur History hinzufügen
        history_entry = f"{value} {from_unit} -> {result:.4f} {to_unit}"
        history.append(history_entry)
        if len(history) > 10:
            history.pop(0)
        # Listbox aktualisieren
        listbox.delete(0, tk.END)
        for item in history:
            listbox.insert(tk.END, item)

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
root.geometry("600x200")  # Breite erhöht für Listbox

# Linker Frame für bestehende Widgets
left_frame = tk.Frame(root)
left_frame.pack(side=tk.LEFT, padx=10, pady=10)
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

# Rechter Frame für Listbox
right_frame = tk.Frame(root)
right_frame.pack(side=tk.RIGHT, padx=10, pady=10)

tk.Label(right_frame, text="Letzte Umrechnungen:").pack(pady=5)
listbox = tk.Listbox(right_frame, width=40, height=10)
listbox.pack()

# Formelanzeige im rechten Frame
formula_label = tk.Label(right_frame, text="Benutze Umrechnungssformel:", justify='left')
formula_label.pack()

root.mainloop()