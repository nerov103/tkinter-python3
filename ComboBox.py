import tkinter
from tkinter import ttk

windo = tkinter.Tk()
windo.title("GUI")

def show_item(s):
    get_item = conboBox.get()
    disply_text.config(text=f"Selected {get_item}")



comboBox_item = ['item1', 'item2', 'item3', 'item4', 'item5', 'item6']
conboBox = ttk.Combobox(windo, values=comboBox_item)
conboBox.set('select option one')
conboBox.pack()




disply_text = tkinter.Label(windo, fg="black")
disply_text.pack()



# Bind the event handler to the <<ComboboxSelected>> event
conboBox.bind("<<ComboboxSelected>>", show_item)



windo.mainloop()

