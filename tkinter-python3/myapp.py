#import module
import tkinter
from tkinter import *
from pytube import YouTube
import pytube

#title and windo create
root_windo = Tk()
root_windo.title("Youtube")

#screensize 
root_windo.geometry("700x300")
root_windo.configure(bg="LightGray")

#add icon in my appliction
phot = PhotoImage(file="icon.png")
root_windo.iconphoto(False, phot)


#create a label 
label1 = Label(root_windo, text="😊JAST FOR YOU😊", font=('Helvetica 15 underline'), fg="Olive")
label1.pack(pady=10)


#youtube video downloads function in used to python pytube library
def my_video():
    user_deta = user_url.get()
    youtubeObject = YouTube(user_deta)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("An error has occurred")
    error_label.config(text="Download is completed...")


#create a function for entry box
def focas(event):
    if  user_url.get() == "enter your video url...":
        user_url.delete(0,'end')
        user_url.config(bg="white")


#a input label
user_url = Entry(root_windo, width=80, highlightcolor='green', highlightthickness=2,highlightbackground="white", font=("Aril", 13))
user_url.pack(pady=10)
user_url.insert(0, "enter your video url...")
user_url.bind("<FocusIn>", focas)


#download button
button = tkinter.Button(root_windo, text="Downloads", bg="Gray", fg="white", command=my_video)
button.pack(pady=20)


#add 3 label for about me
labelx = tkinter.Label(root_windo, text="Create by Nerov Ahmead",  font=("Times", 10), fg="LightYellow")
labely = tkinter.Label(root_windo, text="facebook/nerov13",  font=("Helvetica", 10), fg="LightCyan")
error_label = tkinter.Label(root_windo, text="", fg="green")
labelx.pack(side=BOTTOM)
labely.pack(side=BOTTOM)
error_label.pack(side=BOTTOM)


root_windo.mainloop()