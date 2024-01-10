#to day ima create a simple app for windows
#in app crating aim used in python some library
import tkinter as tk

windo = tk.Tk()
windo.title("Tk GUI")


def button_function():
    label.config(text="Hello ima a Button!", fg="white", bg="black")


label = tk.Label(windo, fg="red",bg="black", font=("Arial", 16),padx=100, pady= 5)
label.pack()

button = tk.Button(windo, text="Click Me", bg="white", fg="black", command=button_function)
button.pack()








windo.mainloop()










#all code write by Nerov Ahmead
#facebook/nerov13
#github/nerov103
#Thanks You!
#Power Of Python...

