import tkinter as tk

window = tk.Tk()


def on_button_click():
    label.config(text="Button Clicked!")


frame = tk.Frame(window, padx=20, pady=20)
frame.pack(padx=10, pady=10)


# Add widgets (buttons, labels, etc.) to the frame
button = tk.Button(frame, text="Click Me", command=on_button_click)
button.pack()

label = tk.Label(frame, text="Hello, Tkinter!")
label.pack()









window.mainloop()