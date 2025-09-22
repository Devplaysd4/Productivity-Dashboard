# calendar_widget.py

from tkinter import *
import ttkbootstrap as tb
from datetime import date
from ttkbootstrap.dialogs import Querybox

def launch_calendar():
    calendar = tb.Window(themename="superhero")
    calendar.title("DateEntry")
    calendar.geometry('500x300')

    def datey():
        my_label.config(text=f"You Picked: {my_date.entry.get()}")

    def thing():
        cal = Querybox()
        my_label.config(text=f"You Picked: {cal.get_date()}")

    my_date = tb.DateEntry(calendar, bootstyle="danger", firstweekday=0)
    my_date.pack(pady=50)

    my_button = tb.Button(calendar, text="Get Date", bootstyle="danger outline", command=datey)
    my_button.pack(pady=20)

    my_button2 = tb.Button(calendar, text="Get Calendar", bootstyle="success outline", command=thing)
    my_button2.pack(pady=20)

    my_label = tb.Label(calendar, text="You Picked: ")
    my_label.pack(pady=20)

    calendar.mainloop()

# Runs only when the file is executed directly
if __name__ == "__main__":
    launch_calendar()
# import customtkinter
# from tkcalendar import Calendar
# import datetime

# def launch_calendar():
#     # Create a Toplevel window styled like your main app
#     calendar_window = customtkinter.CTkToplevel()
#     calendar_window.title("Calendar")
#     calendar_window.geometry("400x400")
#     calendar_window.resizable(False, False)

#     # Set appearance to match main window
#     customtkinter.set_appearance_mode("Light")  # or "Dark"
#     customtkinter.set_default_color_theme("dark-blue")

#     # Add Calendar widget (native tkcalendar)
#     today = datetime.date.today()
#     cal = Calendar(calendar_window,
#                    selectmode='day',
#                    year=today.year,
#                    month=today.month,
#                    day=today.day,
#                    date_pattern='dd/mm/yyyy')
#     cal.pack(pady=20)

#     # Button to print selected date (optional)
#     def print_selected():
#         selected_date = cal.get_date()
#         print("Selected Date:", selected_date)

#     select_button = customtkinter.CTkButton(
#         master=calendar_window,
#         text="Select Date",
#         command=print_selected,
#         corner_radius=10,
#         text_color="black",
#         hover_color="SeaGreen1"
#     )
#     select_button.pack(pady=10)
