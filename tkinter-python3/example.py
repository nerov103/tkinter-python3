import tkinter
# import customtkinter

# # main windo
windo = tkinter.Tk()
# windo.title("GUI")

# #create a function for button
# def x():
#     print("ima button")

    
# #create a button in tkinter
# button = tkinter.Button(windo, text="show", command=x)
# button.pack(pady=20)


# def button_callback():
#     print("button clicked")

# app = customtkinter.CTk()
# app.geometry("400x150")

# button = customtkinter.CTkButton(app, text="my button", command=button_callback)
# button.pack(padx=20, pady=20)

# import random
# len_input = int(input("enter your password len[+] "))
# all_key = "!, @ #  %, ^, &, *, (, ), _, +A, S,, ;, '8, 9, 0, -, 0-9, +, -, *, /, ~ =".replace(",","").replace(" ", "")
# all_deta = ""
# for a in range(len_input):
#     all_deta+=random.choice(all_key)

# print(all_deta)

windo.geometry("500x500")

label = tkinter.Label(windo, text="Hello World", fg="red", bg="PowderBlue")
label.pack()


label = tkinter.Label(windo, text="Hello World", fg="black", bg="PowderBlue")
label.pack(side=["left"])


label = tkinter.Label(windo, text="Hello World", fg="green", bg="PowderBlue")
label.pack(side=["bottom"])


label = tkinter.Label(windo, text="Hello World", fg="red", bg="PowderBlue")
label.pack(side=["right"])







# app.mainloop()
windo.mainloop()

