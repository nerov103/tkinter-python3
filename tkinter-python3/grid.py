import tkinter
windo = tkinter.Tk()
windo.geometry("500x500")


# label1 = tkinter.Label(windo, text="Label One")
# label1.grid(row=0, column=0)

# label2 = tkinter.Label(windo, text="Label Tow")
# label2.grid(row=1, column=1)

# label3 = tkinter.Label(windo, text="Label Three")
# label3.grid(row=2, column=3)

count = 5

for i in range(count):
    for c in range(count):
        labeln = tkinter.Label(windo, text=f"i'ma {i+1}",bg="black", fg="white")
        labeln.grid(row=i, column=c, padx=3, pady=2)






windo.mainloop()