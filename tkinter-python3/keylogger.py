import tkinter
from tkinter import *

#for main windo
root = tkinter.Tk()
root.title("keylogger")
x = 600
y = 300
root.geometry(f"{x}x{y}")
root.maxsize(x, y)
root.minsize(x, y)




background_image = PhotoImage(file="/home/backbox/Pictures/img.gif")

# Create a Label and set the image as its background
label = Label(root, image=background_image)
label.place(x=0, y=0)


# Create the button
button = Button(root, text="Click Me",fg="white", bg="blue",font=('Georgia', 15))
button.pack(side=BOTTOM, pady=70)

# #label3

root.mainloop()