# digital_clock.py

import tkinter as tk
import time

def launch_clock():
    def update_time():
        current_time = time.strftime('%H:%M:%S')
        clock_label.config(text=current_time)
        root.after(1000, update_time)

    root = tk.Tk()
    root.title("Digital Clock")
    root.configure(bg="black")

    clock_label = tk.Label(root, text="", font=("Helvetica", 44), fg="mediumpurple2", bg="black")
    clock_label.pack(padx=20, pady=20)

    update_time()
    root.mainloop()

# Run directly
