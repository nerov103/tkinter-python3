#import module
import tkinter
from tkinter import *

#title and windo create
root_windo = Tk()
root_windo.title("Youtube")

#screensize 
root_windo.geometry("700x300")


#add icon in my appliction
phot = PhotoImage(file="icon.png")
root_windo.iconphoto(False, phot)


#create a label 
label1 = Label(root_windo, text="😊JAST FOR YOU😊", font=('Helvetica 15 underline'), fg="Olive")
label1.pack(pady=10)












root_windo.mainloop()