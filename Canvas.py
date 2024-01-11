#to day ima create a simple app for windows
#in app crating aim used in python some library
import tkinter as tk

windo = tk.Tk()
windo.title("Tk GUI")


def ret_ang():
    canvas.create_rectangle(10, 10, 100, 100, fill="tomato")



# label = tk.Label(windo, text="Hello Wolrd!", fg="white", bg="black", padx=50)
# label.pack()
canvas = tk.Canvas(windo, height=200, width=200, background='green')
canvas.pack()

button = tk.Button(windo, text="click me", bg="red", fg="black", command=ret_ang)
button.pack()



















windo.mainloop()
#all code write by Nerov Ahmead
#facebook/nerov13
#github/nerov103
#Thanks You!
#Power Of Python...

