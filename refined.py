# from tkinter import *  # tkinter k tools use krne k liye 
# import numpy as np
# import math
# import winsound
# import pygame
# import os
# # import pyttsx3  # Import text-to-speech library

# # # Initialize Text-to-Speech Engine
# # engine = pyttsx3.init()
# # engine.setProperty('rate', 150)  # Adjust speech speed
# root = Tk()  # initializing
# root.title("Calculator")  # name
# root.geometry("330x530+550+230")  # dabbe ka size
# root.resizable(FALSE,FALSE)
# root.configure(bg="gray25")  # background
# history_label = Label(root, text="", font=("Arial", 14), bg= "black", fg="gray", anchor="e")
# history_label.pack( fill=BOTH,expand=TRUE)
# history_label.config(font=("Arial", 12))
# history_list=[]

# userentryvar = StringVar()
# userentry = Entry(root, textvariable=userentryvar, font=("Arial", 20), bg="black", fg="white",  relief=FLAT, justify="right")
# userentry.pack( fill=BOTH, expand=TRUE)


# def open_standard():
#     root.deiconify()  # Ensures main awindow is visible

# def open_scientific():
#     sci = Toplevel(root)
#     sci.title("Scientific Mode")
#     sci.geometry("330x530+820+300")
#     sci.configure(bg="black")

#     # Menu for Switching Modes
#     menu = Menu(sci)
#     item = Menu(menu, tearoff=0)
#     item.add_command(label='Standard Mode', command=lambda: (open_standard(), sci.destroy()))
#     item.add_command(label='Scientific Mode', command=open_scientific)
#     item.add_command(label='Conversions', command=open_conversion)
#     item.add_command(label='Graphs', command=open_graph)
#     item.add_command(label='Interest(sciulator', command=open_interest)
#     menu.add_cascade(label='Modes', menu=item)
#     sci.config(menu=menu)
#     sqrt_button = Button(sci, text="√", command=lambda: on_click("sqrt("), font=("Arial", 18))
#     sqrt_button.grid(row=4, column=0, padx=5, pady=5, sticky="nsew")

#     openbracket_button = Button(sci, text="(", command=lambda: on_click("("), font=("Arial", 18))
#     openbracket_button.grid(row=4, column=1, padx=5, pady=5, sticky="nsew")

#     closebracket_button = Button(sci, text=")", command=lambda: on_click(")"), font=("Arial", 18))
#     closebracket_button.grid(row=4, column=2, padx=5, pady=5, sticky="nsew")

#     power_button = Button(sci, text="xʸ", command=lambda: on_click("**"), font=("Arial", 18))
#     power_button.grid(row=4, column=3, padx=5, pady=5, sticky="nsew")

#     log_button = Button(sci, text="log", command=lambda: on_click("log10("), font=("Arial", 18))
#     log_button.grid(row=5, column=0, padx=5, pady=5, sticky="nsew")

#     ln_button = Button(sci, text="ln", command=lambda: on_click("log("), font=("Arial", 18))
#     ln_button.grid(row=5, column=1, padx=5, pady=5, sticky="nsew")

#     factorial_button = Button(sci, text="n!", command=lambda: on_click("factorial("), font=("Arial", 18))
#     factorial_button.grid(row=5, column=2, padx=5, pady=5, sticky="nsew")

#     mod_button = Button(sci, text="%", command=lambda: on_click("%"), font=("Arial", 18))
#     mod_button.grid(row=5, column=3, padx=5, pady=5, sticky="nsew")

#     sin_button = Button(sci, text="sin", command=lambda: on_click("sin("), font=("Arial", 18))
#     sin_button.grid(row=6, column=0, padx=5, pady=5, sticky="nsew")

#     cos_button = Button(sci, text="cos", command=lambda: on_click("cos("), font=("Arial", 18))
#     cos_button.grid(row=6, column=1, padx=5, pady=5, sticky="nsew")

#     tan_button = Button(sci, text="tan", command=lambda: on_click("tan("), font=("Arial", 18))
#     tan_button.grid(row=6, column=2, padx=5, pady=5, sticky="nsew")

#     sin_inv_button = Button(sci, text="sin⁻¹", command=lambda: on_click("asin("), font=("Arial", 18))
#     sin_inv_button.grid(row=6, column=3, padx=5, pady=5, sticky="nsew")

#     cos_inv_button = Button(sci, text="cos⁻¹", command=lambda: on_click("acos("), font=("Arial", 18))
#     cos_inv_button.grid(row=7, column=0, padx=5, pady=5, sticky="nsew")

#     tan_inv_button = Button(sci, text="tan⁻¹", command=lambda: on_click("atan("), font=("Arial", 18))
#     tan_inv_button.grid(row=7, column=1, padx=5, pady=5, sticky="nsew")

#     pi_button = Button(sci, text="π", command=lambda: on_click("pi"), font=("Arial", 18))
#     pi_button.grid(row=7, column=2, padx=5, pady=5, sticky="nsew")

#     e_button = Button(sci, text="e", command=lambda: on_click("e"), font=("Arial", 18))
#     e_button.grid(row=7, column=3, padx=5, pady=5, sticky="nsew")
   
 
    
#     theme_menu = Menu(menu, tearoff=0)
#     theme_menu.add_command(label="Light Mode", command=lambda: change_theme("light"))
#     theme_menu.add_command(label="Dark Mode", command=lambda: change_theme("Dark"))
#     theme_menu.add_command(label="Retro Mode", command=lambda: change_theme("Retro"))
#     theme_menu.add_command(label="Default Mode", command=lambda: change_theme("Default"))
#     menu.add_cascade(label="Themes", menu=theme_menu)
#     sci.config(menu=menu)
    


# def open_conversion():
#     new_win = Toplevel(root)
#     new_win.title("Conversions Mode")
#     new_win.geometry("330x530+1150+300")
#     Label(new_win, text="Conversion Tools", font=("Arial", 20)).pack(pady=20)

# def open_graph():
#     new_win = Toplevel(root)
#     new_win.title("Graph Mode")
#     new_win.geometry("330x530+1150+300")
#     Label(new_win, text="Graphing(sciulator", font=("Arial", 20)).pack(pady=20)

# def open_interest():
#     new_win = Toplevel(root)
#     new_win.title("Interest(sciulator")
#     new_win.geometry("330x530+1150+300")
#     Label(new_win, text="Interest(sciulator", font=("Arial", 20)).pack(pady=20)



# menu = Menu(root)
# item = Menu(menu, tearoff=0)
# item.add_command(label='Standard Mode', command=open_standard)
# item.add_command(label='Scientific Mode', command=open_scientific)
# item.add_command(label='Conversions', command=open_conversion)
# item.add_command(label='Graphs', command=open_graph)
# item.add_command(label='Interest(sciulator', command=open_interest)
# menu.add_cascade(label='Modes', menu=item)
# root.config(menu=menu)


# theme_menu=Menu(menu,tearoff=0)
# theme_menu.add_command(label="Light Mode",command=lambda:change_theme("light"))
# theme_menu.add_command(label="Dark Mode",command=lambda:change_theme("Dark"))
# theme_menu.add_command(label="Retro Mode",command=lambda:change_theme("Retro"))
# theme_menu.add_command(label="Default Mode",command=lambda:change_theme("Default"))
# menu.add_cascade(label="Themes",menu=theme_menu)
# root.config(menu=menu)



# def change_theme(mode):
#     global history_label  # Ensure history_label updates properly
    
#     if mode == "light":
#         root.configure(bg="white")
#         userentry.config(bg="white", fg="black")
#         history_label.config(bg="white", fg="gray")  # Update history label
#         buttonframe.config(bg="white")
#         for widget in buttonframe.winfo_children():
#             for btn in widget.winfo_children():
#                 btn.config(bg="lightgray", fg="black", activebackground="gray70")

#     elif mode == "Dark":
#         root.configure(bg="gray25")
#         userentry.config(bg="black", fg="white")
#         history_label.config(bg="black", fg="gray")  # Update history label
#         buttonframe.config(bg="gray25")
#         for widget in buttonframe.winfo_children():
#             for btn in widget.winfo_children():
#                 btn.config(bg="black", fg="white", activebackground="gray60")

#     elif mode == "Retro":
#         root.configure(bg="black")
#         userentry.config(bg="black", fg="lime", insertbackground="lime")
#         history_label.config(bg="black", fg="gray")  # Keep it black in retro mode
#         buttonframe.config(bg="black")
#         for widget in buttonframe.winfo_children():
#             for btn in widget.winfo_children():
#                 btn.config(bg="gray20", fg="lime", activebackground="green")

#     elif mode == "Default":
#         root.configure(bg="gray25")
#         userentry.config(bg="black", fg="white")
#         history_label.config(bg="black", fg="gray")  # Default back to black
#         buttonframe.config(bg="gray25")
#         for widget in buttonframe.winfo_children():
#             for btn in widget.winfo_children():
#                 btn_text = btn.cget("text")
#                 if btn_text in {"+", "-", "/", "*", "="}:
#                     operatorcolor = "darkorange"
#                 elif btn_text in {"C", "+/-", "%", "⌫"}:
#                     operatorcolor = "darkorange"
#                 else:
#                     operatorcolor = "gray25"
#                 btn.config(bg=operatorcolor, fg="white", activebackground="gray60")

# # Create labels for expression history and user input


# def on_click(btn_text):
#     play_sound(btn_text)
#     current_text = userentryvar.get()

#     if btn_text == "C":  # Clear everything
#         userentryvar.set("")
#         history_list.clear()  # Clear history
#         history_label.config(text="")  # Reset history display

#     elif btn_text == "⌫":  # Backspace
#         userentryvar.set(current_text[:-1])

#     elif btn_text == "+/-":  # Toggle sign
#         if current_text:
#             if current_text[0] == "-":
#                 userentryvar.set(current_text[1:])
#             else:
#                 userentryvar.set("-" + current_text)
#     elif btn_text == "sqrt(":  # Handle square root operation
#         if current_text:
#             try:
#                 num = float(current_text)
#                 if num < 0:
#                     return  # Ignore negative values
#                 result = str(math.sqrt(num))
#                 userentryvar.set(result)
#             except:
#                 pass  # Ignore errors
#         else:
#             userentryvar.set("math.sqrt(")
#     elif btn_text == "=":  # Evaluate and move expression to history
#         try:
#             global expression
#             expression = current_text.replace("sqrt(", "math.sqrt(")
#             result = str(eval(current_text))
#             new_entry = f"{current_text} = {result}"

#             # Maintain only the last three(sciulations
#             if len(history_list) >= 3:
#                 history_list.pop(0)  # Remove oldest entry

#             history_list.append(new_entry)  # Add latest(sciulation

#             # Update history label with the last three(sciulations
#             history_label.config(text="\n".join(history_list))

#             userentryvar.set(result)  # Set result in entry for further(sciulations

#         except Exception:
#             userentryvar.set("Error")

#     else:
#         userentryvar.set(current_text + btn_text)  # Append button text
# def on_click(btn_text):
#     # play_sound(btn_text)
#     current_text = userentryvar.get()

#     try:
#         if btn_text == "C":  # Clear everything
#             userentryvar.set("")
#             history_list.clear()  # Clear history
#             history_label.config(text="")  # Reset history display

#         elif btn_text == "⌫":  # Backspace
#             userentryvar.set(current_text[:-1])

#         elif btn_text == "+/-":  # Toggle sign
#             if current_text:
#                 if current_text[0] == "-":
#                     userentryvar.set(current_text[1:])
#                 else:
#                     userentryvar.set("-" + current_text)

#         elif btn_text == "sqrt(":  # Square root operation
#             if current_text:
#                 try:
#                     num = float(current_text)
#                     if num < 0:
#                         return  # Ignore negative values
#                     result = str(math.sqrt(num))
#                     userentryvar.set(result)
#                 except:
#                     pass  # Ignore errors
#             else:
#                 userentryvar.set("math.sqrt(")

#         elif btn_text == "x²":  # Square a number
#             if current_text:
#                 userentryvar.set(str(float(current_text) ** 2))

#         elif btn_text == "x³":  # Cube a number
#             if current_text:
#                 userentryvar.set(str(float(current_text) ** 3))

#         elif btn_text == "∛":  # Cube root
#             if current_text:
#                 userentryvar.set(str(float(current_text) ** (1/3)))

#         elif btn_text == "^":  # Power
#             userentryvar.set(current_text + "**")

#         elif btn_text == "log":  # Logarithm (base 10)
#             userentryvar.set(f"math.log10({current_text})")

#         elif btn_text == "ln":  # Natural logarithm (ln)
#             userentryvar.set(f"math.log({current_text})")

#         elif btn_text == "π":  # Pi constant
#             userentryvar.set(current_text + str(math.pi))

#         elif btn_text == "e":  # Euler’s number
#             userentryvar.set(current_text + str(math.e))

#         elif btn_text in {"sin", "cos", "tan", "cot", "sec", "cosec"}:
#             if current_text:
#                 angle = math.radians(float(current_text))  # Convert degrees to radians
#                 if btn_text == "sin":
#                     result = str(math.sin(angle))
#                 elif btn_text == "cos":
#                     result = str(math.cos(angle))
#                 elif btn_text == "tan":
#                     result = str(math.tan(angle))
#                 elif btn_text == "cot":
#                     result = str(1 / math.tan(angle)) if math.tan(angle) != 0 else "Error"
#                 elif btn_text == "sec":
#                     result = str(1 / math.cos(angle)) if math.cos(angle) != 0 else "Error"
#                 elif btn_text == "cosec":
#                     result = str(1 / math.sin(angle)) if math.sin(angle) != 0 else "Error"

#                 userentryvar.set(result)

#         elif btn_text == "!":  # Factorial
#             if current_text.isdigit():
#                 userentryvar.set(str(math.factorial(int(current_text))))

#         elif btn_text == "1/x":  # Reciprocal
#             if current_text and float(current_text) != 0:
#                 userentryvar.set(str(1 / float(current_text)))

#         elif btn_text == "=":  # Evaluate expression
#             try:
#                 global expression
#                 expression = current_text.replace("sqrt(", "math.sqrt(")
#                 result = str(eval(expression))

#                 # Maintain only the last three(sciulations
#                 if len(history_list) >= 3:
#                     history_list.pop(0)  # Remove oldest entry

#                 history_list.append(f"{current_text} = {result}")  # Add latest(sciulation

#                 # Update history label with the last three(sciulations
#                 history_label.config(text="\n".join(history_list))

#                 userentryvar.set(result)  # Set result in entry for further(sciulations

#             except Exception:
#                 userentryvar.set("Error")

#         else:
#             userentryvar.set(current_text + btn_text)  # Append button text

#     except:
#         userentryvar.set("Error")

# buttonframe = Frame(root, bg="gray25")  # frame for buttons
# buttonframe.pack(fill=BOTH,expand=TRUE)
# # Frame for menu button

# buttons = (
    
#     ("⌫","+/-","%","/"),
#     ("7", "8", "9", "*"),
#     ("4", "5", "6", "-"),
#     ("1", "2", "3", "+"),
#     ("C", "0", ".", "=")
# )

# # percentage=
# # # # play sound
# # pygame.mixer.init()
# # click_sound = pygame.mixer.Sound("fast.wav")

# # def play_sound(btn_text):
# #     click_sound.play()

# #  create buttons
# def create_button(parent, text):  # parent taaki wapas use krpaye root me modify ya baar baar use use nhi krpate 
#     operatorcolor = (
#     "darkorange" if text in {"+", "-", "/", "*", "C", "+/-", "%","⌫","="} else
    
#     "black" if text in {"☰"} else
    
#     "gray25"  # Default color for other cases
# )    # "default_color"  # Optional: Handle other cases


#     return Button(
#         parent, text=text, font=("Arial", 18), width=5, height=2,
#         bg=operatorcolor, fg="white", bd=1.5, relief=SOLID, activebackground="gray60",
#         command=lambda: on_click(text) #  ye tabhi hoga jab click krenge agar lambda nhi lagagega to apne aap chal jayga
#     )

# # Creating Buttons
# for row in buttons:
#     rowframe = Frame(buttonframe, bg="gray25")  # Frame for all rows of buttons
#     rowframe.pack(fill=BOTH,expand=True)
#     for text in row:
#         button = create_button(rowframe, text)
#         button.pack(side=LEFT, fill=BOTH, expand=True)

# root.mainloop()
from tkinter import *
import numpy as np
import math
import winsound
import pygame
import os

class CalculatorApp:
    def __init__(self):
        self.root = Tk()  # initializing
        self.root.title("Calculator")  # name
        self.root.geometry("330x530+550+230")  # dabbe ka size
        self.root.resizable(FALSE,FALSE)
        self.root.configure(bg="gray25")  # background

        self.history_list = []
        self.userentryvar = StringVar()

        self.history_label = Label(self.root, text="", font=("Arial", 14), bg= "black", fg="gray", anchor="e")
        self.history_label.pack(fill=BOTH, expand=TRUE)
        self.history_label.config(font=("Arial", 12))

        self.userentry = Entry(self.root, textvariable=self.userentryvar, font=("Arial", 20), bg="black", fg="white",  relief=FLAT, justify="right")
        self.userentry.pack(fill=BOTH, expand=TRUE)

        self.create_menu()
        self.create_buttons()

    def create_menu(self):
        menu = Menu(self.root)
        item = Menu(menu, tearoff=0)
        item.add_command(label='Standard Mode', command=self.open_standard)
        item.add_command(label='Scientific Mode', command=self.open_scientific)
        item.add_command(label='Conversions', command=self.open_conversion)
        item.add_command(label='Graphs', command=self.open_graph)
        item.add_command(label='Interest(sciulator', command=self.open_interest)
        menu.add_cascade(label='Modes', menu=item)

        theme_menu = Menu(menu, tearoff=0)
        theme_menu.add_command(label="Light Mode", command=lambda: self.change_theme("light"))
        theme_menu.add_command(label="Dark Mode", command=lambda: self.change_theme("Dark"))
        theme_menu.add_command(label="Retro Mode", command=lambda: self.change_theme("Retro"))
        theme_menu.add_command(label="Default Mode", command=lambda: self.change_theme("Default"))
        menu.add_cascade(label="Themes", menu=theme_menu)

        self.root.config(menu=menu)

    def open_standard(self):
        self.root.deiconify()  # Ensures main window is visible

    def open_scientific(self):
        sci = Toplevel(self.root)
        sci.title("Scientific Mode")
        sci.geometry("330x530+820+300")
        sci.configure(bg="black")

        menu = Menu(sci)
        item = Menu(menu, tearoff=0)
        item.add_command(label='Standard Mode', command=lambda: (self.open_standard(), sci.destroy()))
        item.add_command(label='Scientific Mode', command=self.open_scientific)
        item.add_command(label='Conversions', command=self.open_conversion)
        item.add_command(label='Graphs', command=self.open_graph)
        item.add_command(label='Interest(sciulator', command=self.open_interest)
        menu.add_cascade(label='Modes', menu=item)
        sci.config(menu=menu)

        # Scientific buttons
        sqrt_button = Button(sci, text="√", command=lambda: self.on_click("sqrt("), font=("Arial", 18))
        sqrt_button.grid(row=4, column=0, padx=5, pady=5, sticky="nsew")

        openbracket_button = Button(sci, text="(", command=lambda: self.on_click("("), font=("Arial", 18))
        openbracket_button.grid(row=4, column=1, padx=5, pady=5, sticky="nsew")

        closebracket_button = Button(sci, text=")", command=lambda: self.on_click(")"), font=("Arial", 18))
        closebracket_button.grid(row=4, column=2, padx=5, pady=5, sticky="nsew")

        power_button = Button(sci, text="xʸ", command=lambda: self.on_click("**"), font=("Arial", 18))
        power_button.grid(row=4, column=3, padx=5, pady=5, sticky="nsew")

        log_button = Button(sci, text="log", command=lambda: self.on_click("log10("), font=("Arial", 18))
        log_button.grid(row=5, column=0, padx=5, pady=5, sticky="nsew")

        ln_button = Button(sci, text="ln", command=lambda: self.on_click("log("), font=("Arial", 18))
        ln_button.grid(row=5, column=1, padx=5, pady=5, sticky="nsew")

        factorial_button = Button(sci, text="n!", command=lambda: self.on_click("factorial("), font=("Arial", 18))
        factorial_button.grid(row=5, column=2, padx=5, pady=5, sticky="nsew")

        mod_button = Button(sci, text="%", command=lambda: self.on_click("%"), font=("Arial", 18))
        mod_button.grid(row=5, column=3, padx=5, pady=5, sticky="nsew")

        sin_button = Button(sci, text="sin", command=lambda: self.on_click("sin("), font=("Arial", 18))
        sin_button.grid(row=6, column=0, padx=5, pady=5, sticky="nsew")

        cos_button = Button(sci, text="cos", command=lambda: self.on_click("cos("), font=("Arial", 18))
        cos_button.grid(row=6, column=1, padx=5, pady=5, sticky="nsew")

        tan_button = Button(sci, text="tan", command=lambda: self.on_click("tan("), font=("Arial", 18))
        tan_button.grid(row=6, column=2, padx=5, pady=5, sticky="nsew")

        sin_inv_button = Button(sci, text="sin⁻¹", command=lambda: self.on_click("asin("), font=("Arial", 18))
        sin_inv_button.grid(row=6, column=3, padx=5, pady=5, sticky="nsew")

        cos_inv_button = Button(sci, text="cos⁻¹", command=lambda: self.on_click("acos("), font=("Arial", 18))
        cos_inv_button.grid(row=7, column=0, padx=5, pady=5, sticky="nsew")

        tan_inv_button = Button(sci, text="tan⁻¹", command=lambda: self.on_click("atan("), font=("Arial", 18))
        tan_inv_button.grid(row=7, column=1, padx=5, pady=5, sticky="nsew")

        pi_button = Button(sci, text="π", command=lambda: self.on_click("pi"), font=("Arial", 18))
        pi_button.grid(row=7, column=2, padx=5, pady=5, sticky="nsew")

        e_button = Button(sci, text="e", command=lambda: self.on_click("e"), font=("Arial", 18))
        e_button.grid(row=7, column=3, padx=5, pady=5, sticky="nsew")

        theme_menu = Menu(menu, tearoff=0)
        theme_menu.add_command(label="Light Mode", command=lambda: self.change_theme("light"))
        theme_menu.add_command(label="Dark Mode", command=lambda: self.change_theme("Dark"))
        theme_menu.add_command(label="Retro Mode", command=lambda: self.change_theme("Retro"))
        theme_menu.add_command(label="Default Mode", command=lambda: self.change_theme("Default"))
        menu.add_cascade(label="Themes", menu=theme_menu)
        sci.config(menu=menu)

    def open_conversion(self):
        new_win = Toplevel(self.root)
        new_win.title("Conversions Mode")
        new_win.geometry("330x530+1150+300")
        Label(new_win, text="Conversion Tools", font=("Arial", 20)).pack(pady=20)

    def open_graph(self):
        new_win = Toplevel(self.root)
        new_win.title("Graph Mode")
        new_win.geometry("330x530+1150+300")
        Label(new_win, text="Graphing(sciulator", font=("Arial", 20)).pack(pady=20)

    def open_interest(self):
        new_win = Toplevel(self.root)
        new_win.title("Interest(sciulator")
        new_win.geometry("330x530+1150+300")
        Label(new_win, text="Interest(sciulator", font=("Arial", 20)).pack(pady=20)

    def change_theme(self, mode):
        if mode == "light":
            self.root.configure(bg="white")
            self.userentry.config(bg="white", fg="black")
            self.history_label.config(bg="white", fg="gray")
            self.buttonframe.config(bg="white")
            for widget in self.buttonframe.winfo_children():
                for btn in widget.winfo_children():
                    btn.config(bg="lightgray", fg="black", activebackground="gray70")

        elif mode == "Dark":
            self.root.configure(bg="gray25")
            self.userentry.config(bg="black", fg="white")
            self.history_label.config(bg="black", fg="gray")
            self.buttonframe.config(bg="gray25")
            for widget in self.buttonframe.winfo_children():
                for btn in widget.winfo_children():
                    btn.config(bg="black", fg="white", activebackground="gray60")

        elif mode == "Retro":
            self.root.configure(bg="black")
            self.userentry.config(bg="black", fg="lime", insertbackground="lime")
            self.history_label.config(bg="black", fg="gray")
            self.buttonframe.config(bg="black")
            for widget in self.buttonframe.winfo_children():
                for btn in widget.winfo_children():
                    btn.config(bg="gray20", fg="lime", activebackground="green")

        elif mode == "Default":
            self.root.configure(bg="gray25")
            self.userentry.config(bg="black", fg="white")
            self.history_label.config(bg="black", fg="gray")
            self.buttonframe.config(bg="gray25")
            for widget in self.buttonframe.winfo_children():
                for btn in widget.winfo_children():
                    btn_text = btn.cget("text")
                    if btn_text in {"+", "-", "/", "*", "="}:
                        operatorcolor = "darkorange"
                    elif btn_text in {"C", "+/-", "%", "⌫"}:
                        operatorcolor = "darkorange"
                    else:
                        operatorcolor = "gray25"
                    btn.config(bg=operatorcolor, fg="white", activebackground="gray60")

    def on_click(self, btn_text):
        current_text = self.userentryvar.get()

        try:
            if btn_text == "C":  # Clear everything
                self.userentryvar.set("")
                self.history_list.clear()
                self.history_label.config(text="")

            elif btn_text == "⌫":  # Backspace
                self.userentryvar.set(current_text[:-1])

            elif btn_text == "+/-":  # Toggle sign
                if current_text:
                    if current_text[0] == "-":
                        self.userentryvar.set(current_text[1:])
                    else:
                        self.userentryvar.set("-" + current_text)

            elif btn_text == "sqrt(":  # Square root operation
                if current_text:
                    try:
                        num = float(current_text)
                        if num < 0:
                            return
                        result = str(math.sqrt(num))
                        self.userentryvar.set(result)
                    except:
                        pass
                else:
                    self.userentryvar.set("math.sqrt(")

            elif btn_text == "x²":  # Square a number
                if current_text:
                    self.userentryvar.set(str(float(current_text) ** 2))

            elif btn_text == "x³":  # Cube a number
                if current_text:
                    self.userentryvar.set(str(float(current_text) ** 3))

            elif btn_text == "∛":  # Cube root
                if current_text:
                    self.userentryvar.set(str(float(current_text) ** (1/3)))

            elif btn_text == "^":  # Power
                self.userentryvar.set(current_text + "**")

            elif btn_text == "log":  # Logarithm (base 10)
                self.userentryvar.set(f"math.log10({current_text})")

            elif btn_text == "ln":  # Natural logarithm (ln)
                self.userentryvar.set(f"math.log({current_text})")

            elif btn_text == "π":  # Pi constant
                self.userentryvar.set(current_text + str(math.pi))

            elif btn_text == "e":  # Euler’s number
                self.userentryvar.set(current_text + str(math.e))

            elif btn_text in {"sin", "cos", "tan", "cot", "sec", "cosec"}:
                if current_text:
                    angle = math.radians(float(current_text))
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

                    self.userentryvar.set(result)

            elif btn_text == "!":  # Factorial
                if current_text.isdigit():
                    self.userentryvar.set(str(math.factorial(int(current_text))))

            elif btn_text == "1/x":  # Reciprocal
                if current_text and float(current_text) != 0:
                    self.userentryvar.set(str(1 / float(current_text)))

            elif btn_text == "=":  # Evaluate expression
                try:
                    expression = current_text.replace("sqrt(", "math.sqrt(")
                    result = str(eval(expression))

                    if len(self.history_list) >= 3:
                        self.history_list.pop(0)

                    self.history_list.append(f"{current_text} = {result}")
                    self.history_label.config(text="\n".join(self.history_list))

                    self.userentryvar.set(result)

                except Exception:
                    self.userentryvar.set("Error")

            else:
                self.userentryvar.set(current_text + btn_text)

        except:
            self.userentryvar.set("Error")

    def create_buttons(self):
        self.buttonframe = Frame(self.root, bg="gray25")
        self.buttonframe.pack(fill=BOTH, expand=TRUE)

        buttons = (
            ("⌫", "+/-", "%", "/"),
            ("7", "8", "9", "*"),
            ("4", "5", "6", "-"),
            ("1", "2", "3", "+"),
            ("C", "0", ".", "=")
        )

        for r, row in enumerate(buttons):
            row_frame = Frame(self.buttonframe)
            row_frame.pack(expand=TRUE, fill=BOTH)
            for c, btn_text in enumerate(row):
                btn = self.create_button(row_frame, btn_text)
                btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

    def create_button(self, parent, text):
        operatorcolor = (
            "darkorange" if text in {"+", "-", "/", "*", "C", "+/-", "%", "⌫", "="} else
            "black" if text == "☰" else
            "gray25"
        )
        return Button(
            parent, text=text, font=("Arial", 18), width=5, height=2,
            bg=operatorcolor, fg="white", bd=1.5, relief=SOLID,
            activebackground="gray60",
            command=lambda: self.on_click(text)
        )

    def run(self):
        self.root.mainloop()


# If you want to run this file directly, uncomment below:
if __name__ == "__main__":
    app = CalculatorApp()
    app.run()
