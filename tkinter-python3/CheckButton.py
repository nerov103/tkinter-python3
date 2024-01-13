import tkinter as tk


window = tk.Tk()
window.title("GUI")

def my_fun():
    lebal.config(text=f"scelcted:  {cound.get()}")



cound = tk.IntVar()
checkboxbutton = tk.Checkbutton(window, text="click me", variable=cound, command=my_fun)
checkboxbutton.pack()



lebal = tk.Label(window)
lebal.pack()





# Run the Tkinter event loop
window.mainloop()
