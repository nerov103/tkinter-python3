import tkinter

windo = tkinter.Tk()
windo.title("GUI")



def my_function():
    lebel.config(text=f"CheckBox stats {get_intger_valu.set()}")


get_intger_valu = tkinter.IntVar()
checkbutton = tkinter.Checkbutton(windo, text="click me", variable=get_intger_valu, command=my_function)
checkbutton.pack()





#Create a Lebal 
lebel = tkinter.Label(windo, text="")
lebel.pack()



windo.mainloop()