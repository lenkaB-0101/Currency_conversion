from tkinter import *

# Okno
window = Tk()
window.title("Currency conversion")
window.minsize(width=300, height=300)
window.resizable(False, False)
window.iconbitmap("ICON.ico")
window.config(background="#f621d2")

# 1 EUR = 24,58 Kč

def count_currency():
    amount_eur = float(amount_input.get()) / 24.58
    result_l["text"] = round(amount_eur, 2)

# vstup od uživatele
amount_input = Entry(width=10, font=("Helvetica", 15))
amount_input.grid(row=0, column=0, padx=10, pady=10)


# Label
czk_label = Label(text="CZK", bg="#f621d2", fg="black", font=("Helvetica", 15), borderwidth=5, relief="sunken")
czk_label.grid(row=0, column=1)

result_l = Label(text="0", font=("Helvetica", 15), bg="#f621d2", fg="black")
result_l.grid(row=1, column=0)

eur_l= Label(text="EUR", font=("Helvetica", 15), bg="#f621d2", fg="black", borderwidth=5, relief="sunken")
eur_l.grid(row=1, column=1)


# tlačítko
count_button = Button(text="Conversion ", font=("Helvetica", 15), command=count_currency)
count_button.grid(row=0, column=2, padx=10, pady=10)







# Hlavní cyklus
window.mainloop()

