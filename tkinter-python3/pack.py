from tkinter import *

windo = Tk()
windo.geometry("500x500")




top = Label(windo, text="Top", bg='red')
top.pack(pady=10, side=LEFT, ipady=10, ipadx=10)
left = Label(windo,bg="black", text="Top And left", fg="white")
left.pack(padx=10, side=LEFT)










windo.mainloop()