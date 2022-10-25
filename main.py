from tkinter import *

# Okno
window = Tk()
window.title("Currency conversion")
window.minsize(width=500, height=500)
window.resizable(False, False)
window.iconbitmap("ICON.ico")
window.config(background="#f621d2")

#window2 = tkinter.Tk()
#window2.title("Second window")
#window2.geometry("300x400+800+100")
#window2.resizable(False, False)
#window2.iconbitmap("ICON.ico")
#window2.config(bg="#20ff0d")


# Label
currency = Label(text="EUR", bg="#f621d2", fg="black", font=("Helvetica", 24, "bold"), borderwidth=5, relief="sunken")
currency.pack(ipadx=20)

#currency2 = Label(window, text="CZK", font=("Cambira", 24, "bold"), bg="#f621d2", fg="black", borderwidth=5, relief="sunken")
#currency2.pack(ipadx=20)


#změna textu
#currency["text"] = "New"
#currency.config(text="New2")

# tlačítko
def change_text():
    currency["text"] = input_1.get()


button_1 = Button(text="Click", command=change_text)
button_1.pack()

# Input
input_1 = Entry(width=20)
input_1.pack()


# Hlavní cyklus
window.mainloop()

