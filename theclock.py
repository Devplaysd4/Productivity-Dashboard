#!/usr/bin/env python3
import tkinter as tk
import time

root = tk.Tk()
root.title("Digital Clock")
root.configure(bg="black")

# Small window
root.geometry("240x80+650+20")   # width x height + x + y
root.resizable(False, False)

# Optional: always stay on top
root.attributes("-topmost", True)

clock_label = tk.Label(
    root,
    font=("Helvetica", 36, "bold"),
    fg="white",
    bg="black"
)
clock_label.pack(expand=True, fill="both")

def update_time():
    clock_label.config(text=time.strftime("%H:%M:%S"))
    root.after(1000, update_time)

update_time()
root.mainloop()