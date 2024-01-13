import tkinter as tk

def hello():
    print("Hello!")

def quit_app():
    root.quit()

# Create the main window
root = tk.Tk()
root.title("Menu Example")

# Create a Menu widget
menu_bar = tk.Menu(root)

# Create a File menu
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open")
file_menu.add_command(label="Save")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=quit_app)

# Create an Edit menu
edit_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Cut")
edit_menu.add_command(label="Copy")
edit_menu.add_command(label="Paste")

# Add the File and Edit menus to the menu bar
menu_bar.add_cascade(label="File", menu=file_menu)
menu_bar.add_cascade(label="Edit", menu=edit_menu)

# Add a Hello command to the root menu
menu_bar.add_command(label="Hello", command=hello)

# Set the menu bar for the root window
root.config(menu=menu_bar)

# Start the Tkinter event loop
root.mainloop()
