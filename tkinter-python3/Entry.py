import tkinter

windo = tkinter.Tk()
windo.title('GUI')

windo.geometry("1080x720")

def how_box():
    sev = input_box.get()
    x = tkinter.Label(windo, text=sev, fg="red", bg="black")
    x.pack()

input_box = tkinter.Entry(windo,width=30)
input_box.pack(pady=20)


button = tkinter.Button(windo, text="click me", command=how_box)
button.pack(pady=5)












windo.mainloop()