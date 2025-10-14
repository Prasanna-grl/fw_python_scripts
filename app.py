import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Simple Tkinter App")

# Add a label widget
label = tk.Label(root, text="Hello, Tkinter!")
label.pack(pady=10)

# Define a button callback function
def on_button_click():
    label.config(text="Button was clicked!")

# Add a button widget
button = tk.Button(root, text="Click Me", command=on_button_click)
button.pack(pady=10)

# Start the GUI event loop
root.mainloop()
