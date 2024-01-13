import tkinter as tk

windo = tk.Tk()
windo.title("GUI")



#Create a function
def my_function(valu):
    label.config(text=f"text label: {valu}")



scale = tk.Scale(windo, from_=0, to=100, orient=tk.HORIZONTAL, command=my_function)
scale.pack(pady=10)



#create a lavel 
label = tk.Label(windo, text="text label 0")
label.pack(pady=10)





windo.mainloop()