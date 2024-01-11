import tkinter
import customtkinter

# main windo
windo = tkinter.Tk()
windo.title("GUI")

#create a function for button
def x():
    print("ima button")

    
#create a button in tkinter
button = tkinter.Button(windo, text="show", command=x)
button.pack(pady=20)


def button_callback():
    print("button clicked")

app = customtkinter.CTk()
app.geometry("400x150")

button = customtkinter.CTkButton(app, text="my button", command=button_callback)
button.pack(padx=20, pady=20)








app.mainloop()
windo.mainloop()

