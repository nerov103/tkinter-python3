import tkinter

windo = tkinter.Tk()
windo.title("GUI")

def my_function():
    tx = "Hello ima nerov \n ima from bangladesh \n i love python programming langush \n thank you"
    mess.config(text=tx)

mess = tkinter.Message(windo, text="")
mess.pack(padx=100,pady=100)

button = tkinter.Button(windo, text="click me", command=my_function)
button.pack()





windo.mainloop()