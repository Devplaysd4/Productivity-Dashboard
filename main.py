
import customtkinter
from PIL import Image, ImageTk
import pyjokes
import requests
import cal
import theclock

from refined import CalculatorApp
# You can place it in fullscreen mode or below joke_label

app = customtkinter.CTk()
app.geometry("500x300+900+500")
customtkinter.set_appearance_mode("System")  # "Light" or "System"
customtkinter.set_default_color_theme("dark-blue")  # or "green", "dark-blue"

app.fullscreen_mode = False
widgets_visible = False  # To track widgets show/hide toggle

screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()


# img_path = r"C:\Users\Dev\OneDrive\Desktop\Python\projects\usingtkinter\tkinter.py\Main window\Designer.png"
# bg_image = customtkinter.CTkImage(Image.open(img_path), size=(screen_width, screen_height))
# bg_label = customtkinter.CTkLabel(app, image=bg_image, text="")
# bg_label.place(x=0, y=0, relwidth=1, relheight=1)
# # Load Background Image Once (avoid resizing or redrawing)


weather_label = customtkinter.CTkLabel(
    app,
    text="",
    font=("Arial", 16, "bold"),
    text_color="#00BFFF",
    justify="center"
)
# weather_label.configure(bg="transparent")
def start_weather_refresh():
    get_weather()
    app.after(15*60*1000, start_weather_refresh)  #refreshes every 15 minutes

import datetime

time_label = customtkinter.CTkLabel(
    app,
    text="",
    font=("Arial", 13, "bold"),
    text_color="white",  # soft dark gray
    bg_color="transparent",
    justify="left"
)
def update_time():
    now = datetime.datetime.now()
    time_string = now.strftime("%A, %d %B %Y — %I:%M:%S %p")
    time_label.configure(text=time_string)
    app.after(1000, update_time)



def get_weather():
    api_key = "ab6e19a5d6c84d7689d190343251404"
    city = "Dehradun"
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no"

    try:
        response = requests.get(url)
        data = response.json()
        temp = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]

        # --- Time-based greeting ---
        current_hour = datetime.datetime.now().hour
        if 5 <= current_hour < 12:
            greeting = "Good morning! ☀️"
        elif 12 <= current_hour < 17:
            greeting = "Good afternoon! 🌤️"
        elif 17 <= current_hour < 20:
            greeting = "Good evening! 🌇"
        else:
            greeting = "Good night! 🌙"

        # Format last updated time
        last_updated_time = datetime.datetime.now().strftime("%I:%M %p")

        weather_label.configure(
            text=f"{greeting}\n{city}: {temp}°C, {condition}\nLast updated: {last_updated_time}"
        )

    except:
        weather_label.configure(text="Unable to fetch weather")

# Function to update joke
def update_joke():
    joke = pyjokes.get_joke(language="en", category="neutral")
    joke_label = customtkinter.CTkLabel(app,
    text="",
    wraplength=400,
    font=("Arial", 14,"bold"),
    text_color="white",
    bg_color="transparent",
    justify="left")



def explore_fullscreen():
    global widgets_visible

    if not app.fullscreen_mode:
        try:
            app.state('zoomed')
        except:
            app.geometry(f"{screen_width}x{screen_height}+0+0")

        app.fullscreen_mode = True

        # Show background image now
        # bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        # bg_label.lower()  # Send it behind everything else

        explore_button.configure(text="Nice to have you here!")
        explore_button.place_forget()
        app.update_idletasks()
        explore_button.place(relx=0.5, y=100, anchor="center")
        place_widgets()
        
        time_label.place(x=63, y=30)  # Top-left corner
        quote_display.pack(padx=20,pady=60)
        get_quote_button.pack()
        # app.after(2, place_widgets)
        visit_button.place(x=110,y=500)
        visit_button2.place(x=110,y=550)
        visit_button3.place(x=110,y=600)
        toss_button.place(x=1230,y=30)
        toss_label.place(x=1230,y=70)
        # btnvs.place(x=110,y=650)
        
    else:
        app.state('normal')
        app.geometry("500x300+900+500")
        app.fullscreen_mode = False
        widgets_visible = False

        # Hide background image
        # bg_label.place_forget()

        explore_button.configure(text="Explore")
        explore_button.place_forget()
        explore_button.pack(padx=20, pady=115)

        widgets_button.place_forget()
        hide_widgets()
        joke_label.place_forget()
        joke_button.place_forget()
        weather_label.place_forget()
        
def place_widgets():
    final_weather_x = screen_width // 2 # Centered X for weather
    final_joke_x = 205
    final_joke_btn_x = 180
    final_widgets_btn_x = int(screen_width * 0.90)

    y_weather = int(screen_height * 0.4)
    y_joke = int(screen_height * 0.4)
    y_joke_btn = int(screen_height * 0.3)
    y_widgets_btn = int(screen_height * 0.3)

    # Animate other widgets as usual (non-centered)
    animate_widget(weather_label, screen_width + 300, final_weather_x, y_weather)
    animate_widget(joke_label, screen_width + 300, final_joke_x, y_joke)
    animate_widget(joke_button, screen_width + 300, final_joke_btn_x, y_joke_btn)
    animate_widget(widgets_button, screen_width + 300, final_widgets_btn_x, y_widgets_btn)
    if app.fullscreen_mode:
                                animate_widget(todo_title, screen_width + 300, screen_width // 2, int(screen_height * 0.56))
                                animate_widget(todo_subtitle, screen_width + 300, screen_width // 2, int(screen_height * 0.6))
                                animate_widget(task_entry, screen_width + 300, screen_width // 2, int(screen_height * 0.64))
                                animate_widget(add_high_button, screen_width + 300, screen_width // 2 - 100, int(screen_height * 0.7))
                                animate_widget(add_medium_button, screen_width + 300, screen_width // 2, int(screen_height * 0.7))
                                animate_widget(add_low_button, screen_width + 300, screen_width // 2 + 100, int(screen_height * 0.7))
                                animate_widget(todo_display, screen_width + 300, screen_width // 2, int(screen_height * 0.837))
                                    
                           

    get_weather()

# --- To-Do List Section ---
todo_title = customtkinter.CTkButton(app, text="To-Do List", state="disabled",
    text_color="white", fg_color="transparent", font=("Arial", 20, "bold"), corner_radius=15)

todo_subtitle = customtkinter.CTkLabel(app, text="Let’s finish them tasks",
    text_color="lightgray", font=("Arial", 14, "italic"), bg_color="transparent")

task_entry = customtkinter.CTkEntry(app, placeholder_text="Enter your task", width=400)

todo_display = customtkinter.CTkTextbox(app, width=400, height=190, corner_radius=15)
todo_display.configure(state="disabled")

def add_task(urgency):
    save_tasks()

    task = task_entry.get()
    if not task.strip():
        return

    color = {"High": "red", "Medium": "orange", "Low": "green"}[urgency]
    task_entry.delete(0, "end")
    todo_display.configure(state="normal")
    todo_display.insert("end", f"{urgency} - {task}\n")
    todo_display.tag_add(urgency, "end-2l", "end-1l")
    todo_display.tag_config(urgency, foreground=color)
    todo_display.configure(state="disabled")

add_high_button = customtkinter.CTkButton(app, text="High", command=lambda: add_task("High"),
    fg_color="red", hover_color="#ff6666", text_color="white", width=80)

add_medium_button = customtkinter.CTkButton(app, text="Medium", command=lambda: add_task("Medium"),
    fg_color="orange", hover_color="#ffae42", text_color="white", width=80)

add_low_button = customtkinter.CTkButton(app, text="Low", command=lambda: add_task("Low"),
    fg_color="green", hover_color="#66ff66", text_color="white", width=80)

# delete ka option 
def save_tasks():
    tasks_txt=r"C:\Users\Dev\OneDrive\Desktop\Python\projects\usingtkinter\tkinter.py\Main window\tasks.txt"
    with open(tasks_txt, "w") as file:
        content = todo_display.get("1.0", "end").strip()
        file.write(content)
def load_tasks():
    tasks_txt = r"C:\Users\Dev\OneDrive\Desktop\Python\projects\usingtkinter\tkinter.py\Main window\tasks.txt"
    try:
        with open(tasks_txt, "r") as file:
            content = file.read()
            if content:
                todo_display.configure(state="normal")
                for line in content.split("\n"):
                    if line:
                        urgency = line.split(" - ")[0]
                        todo_display.insert("end", f"{line}\n")
                        todo_display.tag_add(urgency, "end-2l", "end-1l")
                        color = {"High": "red", "Medium": "orange", "Low": "green"}[urgency]
                        todo_display.tag_config(urgency, foreground=color)
                todo_display.configure(state="disabled")
    except FileNotFoundError:
        pass











def animate_widget(widget, current_x, target_x, y, step=20):
    if current_x > target_x:
        current_x -= step
        widget.place(x=current_x, y=y, anchor="center")
        app.after(1, lambda: animate_widget(widget, current_x, target_x, y, step))
    else:
        widget.place(x=target_x, y=y, anchor="center")

def toggle_widgets():
    global widgets_visible
    final_x = (screen_width // 2) + 575

    if not widgets_visible:
        animate_widget(clock_button, screen_width + 250, final_x, int(screen_height * 0.4))
        animate_widget(calendar_button, screen_width + 250, final_x, int(screen_height * 0.6))
        animate_widget(calc_button, screen_width + 250, final_x, int(screen_height * 0.5))
        # animate_widget(calc_label,screen_width + 250, final_x, int(screen_height * 0.65))
        widgets_visible = True
    else:
        hide_widgets()

def hide_widgets():
    global widgets_visible
    clock_button.place_forget()
    calendar_button.place_forget()
    calc_button.place_forget()
    widgets_visible = False


explore_button = customtkinter.CTkButton(app, text="Explore", command=explore_fullscreen,text_color="black",hover_color="SeaGreen1",corner_radius=15,bg_color="transparent",fg_color="white")
explore_button.pack(padx=20, pady=115)

widgets_button = customtkinter.CTkButton(app, text="Widgets", command=toggle_widgets, text_color="black",hover_color="SeaGreen1",corner_radius=15,bg_color="transparent",fg_color="white")




# These Buttons Are Widgets
def open_clock():
    theclock.launch_clock()
    
def open_calendar():
    cal.launch_calendar()

def open_calc():
    app = CalculatorApp()
    app.run()

clock_button = customtkinter.CTkButton(app,
    text="Clock",
    command=open_clock,font=("Arial" ,16, "bold"),
    width=100,
    compound="left",
    fg_color="transparent",  # 🔥 was neon green
    bg_color="transparent",
    text_color="white",     # softer than pure black
    hover_color="cyan",    # soft gray hover
    corner_radius=15
)

calendar_button = customtkinter.CTkButton(app, text="Calendar", command=open_calendar, width=100,compound="left",
    
    
    fg_color="transparent",  # 🔥 was neon green
    bg_color="transparent",font=("Arial", 16, "bold"),
    text_color="white",     # softer than pure black
    hover_color="cyan",    # soft gray hover
    corner_radius=15
)
calc_button = customtkinter.CTkButton(app, text="Calculator", command=open_calc, width=100,compound="left",
   
    fg_color="transparent",  # 🔥 was neon green
    bg_color="transparent",font=("Arial", 16, "bold"),
    text_color="white",     # softer than pure black
    hover_color="cyan",    # soft gray hover
    corner_radius=15
)
# calc_label=customtkinter.CTkLabel(app,text="This widget is under construction, please access it manually. ", compound="left",
#     fg_color="transparent",  # 🔥 was neon green
#     bg_color="transparent",font=("Arial", 16, "bold"),
#     text_color="",     # softer than pure black
    
#     corner_radius=15)

# Hide widgets initially
hide_widgets()
widgets_button.place_forget()

# Joke display section


def get_joke():
    return pyjokes.get_joke(language="en", category="neutral")

def update_joke():
    joke_label.configure(text=get_joke())

# Define them but don't place them yet
joke_label = customtkinter.CTkLabel(app,
    text="",
    wraplength=300,
    font=("Arial", 14),
    text_color="white",bg_color="transparent",
    justify="left",corner_radius=15)

joke_button = customtkinter.CTkButton(app,
    
    text="Get Joke",
    command=update_joke,
    fg_color="white",  # Button's foreground color
    bg_color="transparent",  # Background color (transparent)
    text_color="black",  # Text color inside the button
    hover_color="lightgrey",  # Color when hovering over the button
    corner_radius=15  # Rounded corners
)
import random

# List of quotes

quotes = [
    "Believe you can and you're halfway there.",
    "Work hard in silence, let your success be your noise.",
    "Don't watch the clock; do what it does. Keep going.",
    "Success is not for the lazy.",
    "Stay focused and never give up.",
    "Do one thing every day that scares you.",
    "If not now, then when?",
    "Push yourself, because no one else is going to do it for you.",
    "Dream it. Wish it. Do it.",
    "Great things never come from comfort zones.",
    "Don’t stop when you’re tired. Stop when you’re done.",
    "Wake up with determination. Go to bed with satisfaction.",
    "The key to success is to focus on goals, not obstacles.",
    "You are capable of amazing things.",
    "Your only limit is your mind.",
    "Doubt kills more dreams than failure ever will.",
    "Small steps every day lead to big results.",
    "Discipline is doing it even when you don’t feel like it.",
    "Don’t wish for it. Work for it.",
    "Fall seven times, stand up eight.",
    "You don’t find willpower — you create it.",
    "Don’t be afraid to start over. It’s a chance to build something better.",
    "Success is the sum of small efforts repeated daily.",
    "You get what you work for, not what you wish for.",
    "A little progress each day adds up to big results.",
    "Be stronger than your excuses.",
    "Winners are not people who never fail. They’re people who never quit.",
    "Stop doubting yourself. Work hard and make it happen.",
    "Keep going. Everything you need will come to you at the perfect time.",
    "Your future needs you. Your past doesn’t.",
    "Stay positive. Work hard. Make it happen.",
    "The harder you work, the luckier you get.",
    "You got this.",
    "It always seems impossible until it’s done.",
    "Be the energy you want to attract.",
    "Focus on being productive instead of busy.",
    "Action is the foundational key to all success.",
    "Done is better than perfect.",
    "You were not born to be mediocre.",
    "Success doesn’t come from what you do occasionally. It comes from what you do consistently.",
    "Train your mind to see the good in everything.",
    "You didn’t come this far to only come this far.",
    "Stay humble, hustle hard.",
    "You are your only competition.",
    "Silence the noise and trust the process.",
    "Hustle in silence, let your results make the noise.",
    "Start where you are. Use what you have. Do what you can.",
    "Consistency > Motivation.",
    "One day or day one. You decide.",
    "Don’t count the days. Make the days count."
]


# Quote display (initially hidden)
quote_display = customtkinter.CTkTextbox(app, width=400, height=60, corner_radius=15)
quote_display.insert("end", "💭 Click below to get inspired!")
quote_display.configure(state="disabled")

# Get Quote function
def get_random_quote():
    quote = random.choice(quotes)
    quote_display.configure(state="normal")
    
    quote_display.delete("1.0", "end")
    
    quote_display.insert("end", f"💭 {quote}")
    quote_display.config( font=("helvetica", 16, "bold"), foreground="white", justify="center")
    quote_display.configure(state="disabled")

# Get Quote button (initially hidden)
get_quote_button = customtkinter.CTkButton(
    app,
    text="Get Quote",
    command=get_random_quote,
    fg_color="#6C63FF",
    hover_color="#8884ff",
    text_color="white",
    width=120
)

import webbrowser
import customtkinter


app.bind("<Escape>", lambda e: explore_fullscreen())
update_time()


def my_upes():
    webbrowser.open("https://myupes-beta.upes.ac.in/connectportal/user/student/home/dashboard")  # replace with your desired URL

visit_button = customtkinter.CTkButton(app, text="Myupes", command=my_upes,fg_color="#FFFF00",  # Button's foreground color
    bg_color="transparent",  # Background color (transparent)
    text_color="black",  # Text color inside the button
    hover_color="lightgrey",  # Color when hovering over the button
    corner_radius=15  )
 # or use .place or .grid if you're positioning specifically
def my_chess():
    webbrowser.open("https://www.chess.com/home")  # replace with your desired URL

visit_button2 = customtkinter.CTkButton(app, text="Chess", command=my_chess,fg_color="#FF7F00",  # Button's foreground color
    bg_color="transparent",  # Background color (transparent)
    text_color="black",  # Text color inside the button
    hover_color="lightgrey",  # Color when hovering over the button
    corner_radius=15  )
def ipl():
    webbrowser.open("https://www.google.com/search?q=ipl&rlz=1C1RXQR_enIN1116IN1118&oq=ipl&gs_lcrp=EgZjaHJvbWUqBggAEEUYOzIGCAAQRRg7MgYIARBFGEAyBggCEEUYPDIGCAMQRRg8MgYIBBBFGDzSAQgyNDMyajBqOagCALACAQ&sourceid=chrome&ie=UTF-8")  # replace with your desired URL

visit_button3 = customtkinter.CTkButton(app, text="IPL", command=ipl,fg_color="#FF0000",  # Button's foreground color
    bg_color="transparent",  # Background color (transparent)
    text_color="black",  # Text color inside the button
    hover_color="lightgrey",  # Color when hovering over the button
    corner_radius=15  )
    #spotify
    # yt
    # whatsapp
    # 
    


import random



def toss_coin():
    result = random.choice(["Heads", "Tails"])
    toss_label.configure(text=f"Toss Result: {result}")

toss_button = customtkinter.CTkButton(
    app, text="Toss Coin", command=toss_coin,
    text_color="black", hover_color="SeaGreen1",
    corner_radius=15, bg_color="transparent", fg_color="medium purple3"
)

toss_label = customtkinter.CTkLabel(
    app, text="", font=("Arial", 16, "bold"),
    text_color="white", bg_color="transparent"
)

import subprocess

# def launch_spotify():
#     subprocess.Popen(r"C:\Program Files\WindowsApps\SpotifyAB.SpotifyMusic_1.261.443.0_x64__zpdnekdrzrea0") 

# btnvs = customtkinter.CTkButton(app, text="Spotify", command=launch_spotify,fg_color="darkgreen",bg_color="transparent")








app.mainloop()


# random quotes


# news
# pomodoro timer