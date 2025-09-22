from tkinter import *
from tkinter import messagebox  # tkinter k tools use krne k liye 
import numpy as np
import math
import winsound
import pygame
import os

# import pyttsx3  # Import text-to-speech library

# # Initialize Text-to-Speech Engine
# engine = pyttsx3.init()
# engine.setProperty('rate', 150)  # Adjust speech speed
root = Tk()  # initializing
root.title("Calculator")  # name
root.geometry("330x530+550+230")  # dabbe ka size
root.resizable(FALSE,FALSE)
root.configure(bg="gray25")  # background
history_label = Label(root, text="", font=("Arial", 14), bg= "black", fg="gray", anchor="e")
history_label.pack( fill=BOTH,expand=TRUE)
history_label.config(font=("Arial", 12))
history_list=[]

userentryvar = StringVar()
userentry = Entry(root, textvariable=userentryvar, font=("Arial", 20), bg="black", fg="white",  relief=FLAT, justify="right")
userentry.pack( fill=BOTH, expand=TRUE)


def open_standard():
    root.deiconify()  # Ensures main awindow is visible

def open_scientific():
    sci = Toplevel(root)
    sci.title("Scientific Mode")
    sci.geometry("330x530+820+300")
    sci.configure(bg="black")

    # Menu for Switching Modes
    menu = Menu(sci)
    item = Menu(menu, tearoff=0)
    item.add_command(label='Standard Mode', command=lambda: (open_standard(), sci.destroy()))
    item.add_command(label='Scientific Mode', command=open_scientific)
    item.add_command(label='Conversions', command=open_conversion)
    item.add_command(label='Graphs', command=open_graph)
    item.add_command(label='Interest(sciulator', command=open_interest)
    menu.add_cascade(label='Modes', menu=item)
    sci.config(menu=menu)
    sqrt_button = Button(sci, text="√", command=lambda: on_click("sqrt("), font=("Arial", 18))
    sqrt_button.grid(row=4, column=0, padx=5, pady=5, sticky="nsew")

    openbracket_button = Button(sci, text="(", command=lambda: on_click("("), font=("Arial", 18))
    openbracket_button.grid(row=4, column=1, padx=5, pady=5, sticky="nsew")

    closebracket_button = Button(sci, text=")", command=lambda: on_click(")"), font=("Arial", 18))
    closebracket_button.grid(row=4, column=2, padx=5, pady=5, sticky="nsew")

    power_button = Button(sci, text="xʸ", command=lambda: on_click("**"), font=("Arial", 18))
    power_button.grid(row=4, column=3, padx=5, pady=5, sticky="nsew")

    log_button = Button(sci, text="log", command=lambda: on_click("log10("), font=("Arial", 18))
    log_button.grid(row=5, column=0, padx=5, pady=5, sticky="nsew")

    ln_button = Button(sci, text="ln", command=lambda: on_click("log("), font=("Arial", 18))
    ln_button.grid(row=5, column=1, padx=5, pady=5, sticky="nsew")

    factorial_button = Button(sci, text="n!", command=lambda: on_click("factorial("), font=("Arial", 18))
    factorial_button.grid(row=5, column=2, padx=5, pady=5, sticky="nsew")

    mod_button = Button(sci, text="%", command=lambda: on_click("%"), font=("Arial", 18))
    mod_button.grid(row=5, column=3, padx=5, pady=5, sticky="nsew")

    sin_button = Button(sci, text="sin", command=lambda: on_click("sin("), font=("Arial", 18))
    sin_button.grid(row=6, column=0, padx=5, pady=5, sticky="nsew")

    cos_button = Button(sci, text="cos", command=lambda: on_click("cos("), font=("Arial", 18))
    cos_button.grid(row=6, column=1, padx=5, pady=5, sticky="nsew")

    tan_button = Button(sci, text="tan", command=lambda: on_click("tan("), font=("Arial", 18))
    tan_button.grid(row=6, column=2, padx=5, pady=5, sticky="nsew")

    sin_inv_button = Button(sci, text="sin⁻¹", command=lambda: on_click("asin("), font=("Arial", 18))
    sin_inv_button.grid(row=6, column=3, padx=5, pady=5, sticky="nsew")

    cos_inv_button = Button(sci, text="cos⁻¹", command=lambda: on_click("acos("), font=("Arial", 18))
    cos_inv_button.grid(row=7, column=0, padx=5, pady=5, sticky="nsew")

    tan_inv_button = Button(sci, text="tan⁻¹", command=lambda: on_click("atan("), font=("Arial", 18))
    tan_inv_button.grid(row=7, column=1, padx=5, pady=5, sticky="nsew")

    pi_button = Button(sci, text="π", command=lambda: on_click("pi"), font=("Arial", 18))
    pi_button.grid(row=7, column=2, padx=5, pady=5, sticky="nsew")

    e_button = Button(sci, text="e", command=lambda: on_click("e"), font=("Arial", 18))
    e_button.grid(row=7, column=3, padx=5, pady=5, sticky="nsew")
   
 
    
    theme_menu = Menu(menu, tearoff=0)
    theme_menu.add_command(label="Light Mode", command=lambda: change_theme("light"))
    theme_menu.add_command(label="Dark Mode", command=lambda: change_theme("Dark"))
    theme_menu.add_command(label="Retro Mode", command=lambda: change_theme("Retro"))
    theme_menu.add_command(label="Default Mode", command=lambda: change_theme("Default"))
    menu.add_cascade(label="Themes", menu=theme_menu)
    sci.config(menu=menu)
    


def open_conversion():
    new_win = Toplevel(root)
    new_win.title("Unit Converter")
    new_win.geometry("400x300")

    Label(new_win, text="Unit Converter", font=("Arial", 20)).pack(pady=10)

    options = ["Celsius to Fahrenheit", "Fahrenheit to Celsius", 
               "Kilometers to Miles", "Miles to Kilometers",
               "Kilograms to Pounds", "Pounds to Kilograms"]

    selected = StringVar()
    selected.set(options[0])

    OptionMenu(new_win, selected, *options).pack(pady=10)

    entry = Entry(new_win, font=("Arial", 14))
    entry.pack(pady=5)

    result_label = Label(new_win, text="", font=("Arial", 14))
    result_label.pack(pady=10)

    def convert():
        try:
            val = float(entry.get())
            choice = selected.get()
            if choice == "Celsius to Fahrenheit":
                res = (val * 9/5) + 32
            elif choice == "Fahrenheit to Celsius":
                res = (val - 32) * 5/9
            elif choice == "Kilometers to Miles":
                res = val * 0.621371
            elif choice == "Miles to Kilometers":
                res = val / 0.621371
            elif choice == "Kilograms to Pounds":
                res = val * 2.20462
            elif choice == "Pounds to Kilograms":
                res = val / 2.20462
            else:
                res = "Unknown"
            result_label.config(text=f"Result: {res:.2f}")
        except Exception as e:
            result_label.config(text="Invalid input")

    Button(new_win, text="Convert", command=convert, font=("Arial", 12)).pack(pady=10)

import matplotlib.pyplot as plt
import numpy as np

def open_graph():
    new_win = Toplevel(root)
    new_win.title("Graphing Calculator")
    new_win.geometry("400x200")

    Label(new_win, text="Graphing Calculator", font=("Arial", 20)).pack(pady=10)
    Label(new_win, text="Enter function in terms of x (e.g., sin(x), x**2 + 3):").pack()

    entry = Entry(new_win, font=("Arial", 14), width=30)
    entry.pack(pady=5)

    def plot_graph():
        expr = entry.get()
        x = np.linspace(-10, 10, 400)
        try:
            y = eval(expr, {"x": x, "np": np, "sin": np.sin, "cos": np.cos, "tan": np.tan,
                            "log": np.log, "sqrt": np.sqrt, "exp": np.exp})
            plt.plot(x, y)
            plt.title(f"y = {expr}")
            plt.grid(True)
            plt.xlabel("x")
            plt.ylabel("y")
            plt.show()
        except Exception as e:
            messagebox.showerror("Error", f"Invalid expression:\n{e}")

    Button(new_win, text="Plot", command=plot_graph, font=("Arial", 12)).pack(pady=10)

def open_interest():
    new_win = Toplevel(root)
    new_win.title("Interest Calculator")
    new_win.geometry("400x400")

    Label(new_win, text="Interest Calculator", font=("Arial", 20)).pack(pady=10)

    Label(new_win, text="Principal Amount (P):").pack()
    principal_entry = Entry(new_win, font=("Arial", 14))
    principal_entry.pack()

    Label(new_win, text="Rate of Interest (R) [%]:").pack()
    rate_entry = Entry(new_win, font=("Arial", 14))
    rate_entry.pack()

    Label(new_win, text="Time (T) [years]:").pack()
    time_entry = Entry(new_win, font=("Arial", 14))
    time_entry.pack()

    Label(new_win, text="Compound Frequency (annually=1, quarterly=4, etc):").pack()
    freq_entry = Entry(new_win, font=("Arial", 14))
    freq_entry.pack()

    result_label = Label(new_win, text="", font=("Arial", 14))
    result_label.pack(pady=10)

    def calculate_interest():
        try:
            P = float(principal_entry.get())
            R = float(rate_entry.get())
            T = float(time_entry.get())
            n = int(freq_entry.get())  # compound frequency

            SI = (P * R * T) / 100
            CI = P * ((1 + R/(100*n))**(n*T)) - P

            result_label.config(
                text=f"Simple Interest: ₹{SI:.2f}\nCompound Interest: ₹{CI:.2f}")
        except Exception as e:
            result_label.config(text="Invalid input!")

    Button(new_win, text="Calculate", command=calculate_interest, font=("Arial", 12)).pack(pady=10)


menu = Menu(root)
item = Menu(menu, tearoff=0)
item.add_command(label='Standard Mode', command=open_standard)
item.add_command(label='Scientific Mode', command=open_scientific)
item.add_command(label='Conversions', command=open_conversion)
item.add_command(label='Graphs', command=open_graph)
item.add_command(label='Interest(sciulator', command=open_interest)
menu.add_cascade(label='Modes', menu=item)
root.config(menu=menu)


theme_menu=Menu(menu,tearoff=0)
theme_menu.add_command(label="Light Mode",command=lambda:change_theme("light"))
theme_menu.add_command(label="Dark Mode",command=lambda:change_theme("Dark"))
theme_menu.add_command(label="Retro Mode",command=lambda:change_theme("Retro"))
theme_menu.add_command(label="Default Mode",command=lambda:change_theme("Default"))
menu.add_cascade(label="Themes",menu=theme_menu)
root.config(menu=menu)



def change_theme(mode):
    global history_label  # Ensure history_label updates properly
    
    if mode == "light":
        root.configure(bg="white")
        userentry.config(bg="white", fg="black")
        history_label.config(bg="white", fg="gray")  # Update history label
        buttonframe.config(bg="white")
        for widget in buttonframe.winfo_children():
            for btn in widget.winfo_children():
                btn.config(bg="lightgray", fg="black", activebackground="gray70")

    elif mode == "Dark":
        root.configure(bg="gray25")
        userentry.config(bg="black", fg="white")
        history_label.config(bg="black", fg="gray")  # Update history label
        buttonframe.config(bg="gray25")
        for widget in buttonframe.winfo_children():
            for btn in widget.winfo_children():
                btn.config(bg="black", fg="white", activebackground="gray60")

    elif mode == "Retro":
        root.configure(bg="black")
        userentry.config(bg="black", fg="lime", insertbackground="lime")
        history_label.config(bg="black", fg="gray")  # Keep it black in retro mode
        buttonframe.config(bg="black")
        for widget in buttonframe.winfo_children():
            for btn in widget.winfo_children():
                btn.config(bg="gray20", fg="lime", activebackground="green")

    elif mode == "Default":
        root.configure(bg="gray25")
        userentry.config(bg="black", fg="white")
        history_label.config(bg="black", fg="gray")  # Default back to black
        buttonframe.config(bg="gray25")
        for widget in buttonframe.winfo_children():
            for btn in widget.winfo_children():
                btn_text = btn.cget("text")
                if btn_text in {"+", "-", "/", "*", "="}:
                    operatorcolor = "darkorange"
                elif btn_text in {"C", "+/-", "%", "⌫"}:
                    operatorcolor = "darkorange"
                else:
                    operatorcolor = "gray25"
                btn.config(bg=operatorcolor, fg="white", activebackground="gray60")

# Create labels for expression history and user input


def on_click(btn_text):
    play_sound(btn_text)
    current_text = userentryvar.get()

    if btn_text == "C":  # Clear everything
        userentryvar.set("")
        history_list.clear()  # Clear history
        history_label.config(text="")  # Reset history display

    elif btn_text == "⌫":  # Backspace
        userentryvar.set(current_text[:-1])

    elif btn_text == "+/-":  # Toggle sign
        if current_text:
            if current_text[0] == "-":
                userentryvar.set(current_text[1:])
            else:
                userentryvar.set("-" + current_text)
    elif btn_text == "sqrt(":  # Handle square root operation
        if current_text:
            try:
                num = float(current_text)
                if num < 0:
                    return  # Ignore negative values
                result = str(math.sqrt(num))
                userentryvar.set(result)
            except:
                pass  # Ignore errors
        else:
            userentryvar.set("math.sqrt(")
    elif btn_text == "=":  # Evaluate and move expression to history
        try:
            global expression
            expression = current_text.replace("sqrt(", "math.sqrt(")
            result = str(eval(current_text))
            new_entry = f"{current_text} = {result}"

            # Maintain only the last three(sciulations
            if len(history_list) >= 3:
                history_list.pop(0)  # Remove oldest entry

            history_list.append(new_entry)  # Add latest(sciulation

            # Update history label with the last three(sciulations
            history_label.config(text="\n".join(history_list))

            userentryvar.set(result)  # Set result in entry for further(sciulations

        except Exception:
            userentryvar.set("Error")

    else:
        userentryvar.set(current_text + btn_text)  # Append button text
def on_click(btn_text):
    # play_sound(btn_text)
    current_text = userentryvar.get()

    try:
        if btn_text == "C":  # Clear everything
            userentryvar.set("")
            history_list.clear()  # Clear history
            history_label.config(text="")  # Reset history display

        elif btn_text == "⌫":  # Backspace
            userentryvar.set(current_text[:-1])

        elif btn_text == "+/-":  # Toggle sign
            if current_text:
                if current_text[0] == "-":
                    userentryvar.set(current_text[1:])
                else:
                    userentryvar.set("-" + current_text)

        elif btn_text == "sqrt(":  # Square root operation
            if current_text:
                try:
                    num = float(current_text)
                    if num < 0:
                        return  # Ignore negative values
                    result = str(math.sqrt(num))
                    userentryvar.set(result)
                except:
                    pass  # Ignore errors
            else:
                userentryvar.set("math.sqrt(")

        elif btn_text == "x²":  # Square a number
            if current_text:
                userentryvar.set(str(float(current_text) ** 2))

        elif btn_text == "x³":  # Cube a number
            if current_text:
                userentryvar.set(str(float(current_text) ** 3))

        elif btn_text == "∛":  # Cube root
            if current_text:
                userentryvar.set(str(float(current_text) ** (1/3)))

        elif btn_text == "^":  # Power
            userentryvar.set(current_text + "**")

        elif btn_text == "log":  # Logarithm (base 10)
            userentryvar.set(f"math.log10({current_text})")

        elif btn_text == "ln":  # Natural logarithm (ln)
            userentryvar.set(f"math.log({current_text})")

        elif btn_text == "π":  # Pi constant
            userentryvar.set(current_text + str(math.pi))

        elif btn_text == "e":  # Euler’s number
            userentryvar.set(current_text + str(math.e))

        elif btn_text in {"sin", "cos", "tan", "cot", "sec", "cosec"}:
            if current_text:
                angle = math.radians(float(current_text))  # Convert degrees to radians
                if btn_text == "sin":
                    result = str(math.sin(angle))
                elif btn_text == "cos":
                    result = str(math.cos(angle))
                elif btn_text == "tan":
                    result = str(math.tan(angle))
                elif btn_text == "cot":
                    result = str(1 / math.tan(angle)) if math.tan(angle) != 0 else "Error"
                elif btn_text == "sec":
                    result = str(1 / math.cos(angle)) if math.cos(angle) != 0 else "Error"
                elif btn_text == "cosec":
                    result = str(1 / math.sin(angle)) if math.sin(angle) != 0 else "Error"

                userentryvar.set(result)

        elif btn_text == "!":  # Factorial
            if current_text.isdigit():
                userentryvar.set(str(math.factorial(int(current_text))))

        elif btn_text == "1/x":  # Reciprocal
            if current_text and float(current_text) != 0:
                userentryvar.set(str(1 / float(current_text)))

        elif btn_text == "=":  # Evaluate expression
            try:
                global expression
                expression = current_text.replace("sqrt(", "math.sqrt(")
                result = str(eval(expression))

                # Maintain only the last three(sciulations
                if len(history_list) >= 3:
                    history_list.pop(0)  # Remove oldest entry

                history_list.append(f"{current_text} = {result}")  # Add latest(sciulation

                # Update history label with the last three(sciulations
                history_label.config(text="\n".join(history_list))

                userentryvar.set(result)  # Set result in entry for further(sciulations

            except Exception:
                userentryvar.set("Error")

        else:
            userentryvar.set(current_text + btn_text)  # Append button text

    except:
        userentryvar.set("Error")

buttonframe = Frame(root, bg="gray25")  # frame for buttons
buttonframe.pack(fill=BOTH,expand=TRUE)
# Frame for menu button

buttons = (
    
    ("⌫","+/-","%","/"),
    ("7", "8", "9", "*"),
    ("4", "5", "6", "-"),
    ("1", "2", "3", "+"),
    ("C", "0", ".", "=")
)

# percentage=
# # # play sound
# pygame.mixer.init()
# click_sound = pygame.mixer.Sound("fast.wav")

# def play_sound(btn_text):
#     click_sound.play()

#  create buttons
def create_button(parent, text):  # parent taaki wapas use krpaye root me modify ya baar baar use use nhi krpate 
    operatorcolor = (
    "darkorange" if text in {"+", "-", "/", "*", "C", "+/-", "%","⌫","="} else
    
    "black" if text in {"☰"} else
    
    "gray25"  # Default color for other cases
)    # "default_color"  # Optional: Handle other cases


    return Button(
        parent, text=text, font=("Arial", 18), width=5, height=2,
        bg=operatorcolor, fg="white", bd=1.5, relief=SOLID, activebackground="gray60",
        command=lambda: on_click(text) #  ye tabhi hoga jab click krenge agar lambda nhi lagagega to apne aap chal jayga
    )

# Creating Buttons
for row in buttons:
    rowframe = Frame(buttonframe, bg="gray25")  # Frame for all rows of buttons
    rowframe.pack(fill=BOTH,expand=True)
    for text in row:
        button = create_button(rowframe, text)
        button.pack(side=LEFT, fill=BOTH, expand=True)

root.mainloop()