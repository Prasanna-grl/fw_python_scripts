import tkinter as tk

root = tk.Tk()
root.title("Simple Tkinter App")

# set window size: WIDTHxHEIGHT, optionally +X+Y position
root.geometry("800x480+100+60")  # size 800x480 at position x=100, y=60

label = tk.Label(root, text="Hello, Tkinter!")
label.pack(pady=10)

def on_button_click():
    label.config(text="Button was clicked!")

button = tk.Button(root, text="Click Me", command=on_button_click)
button.pack(pady=10)

root.mainloop()
