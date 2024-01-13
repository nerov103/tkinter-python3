import tkinter

windo = tkinter.Tk()
windo.title("GUI")



def my_fun():
    dorlam = spnbox.get()
    label.config(text=f"Selected value: {dorlam}")



spnbox = tkinter.Spinbox(windo, from_=0, to=100, increment=1, command=my_fun)
spnbox.pack()



label = tkinter.Label(windo, text="Selected value: 0")
label.pack()





windo.mainloop()
