import tkinter as tk



# def on_scroll(*args):
#     text.yview(*args)


# Create the main window
root = tk.Tk()

# Create a Text widget
text = tk.Text(root, wrap=tk.WORD, width=10, height=10)

# Create a Scrollbar widget


# Configure the Text widget to use the scrollbar
scrollbar = tk.Scrollbar(root)
text.config(yscrollcommand=scrollbar.set)

# Pack the widgets into the window
text.pack(side=tk.LEFT, padx=10, pady=10)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Add some text to the Text widget
# for i in range(1, 101):
#     text.insert(tk.END, f"Line {i}\n")









# Start the Tkinter event loop
root.mainloop()
