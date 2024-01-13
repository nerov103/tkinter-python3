import tkinter

windo = tkinter.Tk()

def my_function():
    g = text.get("1.0", tkinter.END)
    label.config(text=g)

text = tkinter.Text(windo, width=60, height=30)
text.pack(pady=10)

button = tkinter.Button(windo, text="click me", command=my_function)
button.pack()


label = tkinter.Label(windo, text="")
label.pack()




windo.mainloop()

