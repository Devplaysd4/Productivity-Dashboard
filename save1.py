
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
customtkinter.set_appearance_mode("Light")  # "Light" or "System"
customtkinter.set_default_color_theme("dark-blue")  # or "green", "dark-blue"

app.fullscreen_mode = False
widgets_visible = False  # To track widgets show/hide toggle

screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()


# img_path = r"C:\Users\Dev\OneDrive\Desktop\Python\projects\usingtkinter\tkinter.py\Main window\icy.jpg"
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

def get_weather():
    api_key = "ab6e19a5d6c84d7689d190343251404"
    city = "Dehradun"
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no"

    try:
        response = requests.get(url)
        data = response.json()
        temp = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]

        # --- Time-based greeting & emoji ---
        current_hour = datetime.datetime.now().hour

        if 5 <= current_hour < 12:
            greeting = "Good morning! ☀️"
        elif 12 <= current_hour < 17:
            greeting = "Good afternoon! 🌤️"
        elif 17 <= current_hour < 20:
            greeting = "Good evening! 🌇"
        else:
            greeting = "Good night! 🌙"

        weather_label.configure(
            text=f"{greeting}\n{city}: {temp}°C, {condition}"
        )

    except:
        weather_label.configure(text="Unable to fetch weather")

# Function to update joke
def update_joke():
    joke = pyjokes.get_joke(language="en", category="neutral")
    joke_label = customtkinter.CTkLabel(app,
    text="",
    wraplength=400,
    font=("Arial", 14),
    text_color="#39FF14",
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
        # app.after(2, place_widgets)

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

    y_weather = int(screen_height * 0.32)
    y_joke = int(screen_height * 0.4)
    y_joke_btn = int(screen_height * 0.3)
    y_widgets_btn = int(screen_height * 0.3)

    # Animate other widgets as usual (non-centered)
    animate_widget(weather_label, screen_width + 300, final_weather_x, y_weather)
    animate_widget(joke_label, screen_width + 300, final_joke_x, y_joke)
    animate_widget(joke_button, screen_width + 300, final_joke_btn_x, y_joke_btn)
    animate_widget(widgets_button, screen_width + 300, final_widgets_btn_x, y_widgets_btn)

    get_weather()



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
        animate_widget(calendar_button, screen_width + 250, final_x, int(screen_height * 0.5))
        animate_widget(calc_button, screen_width + 250, final_x, int(screen_height * 0.6))
        animate_widget(calc_label,screen_width + 250, final_x, int(screen_height * 0.65))
        widgets_visible = True
    else:
        hide_widgets()

def hide_widgets():
    global widgets_visible
    clock_button.place_forget()
    calendar_button.place_forget()
    calc_button.place_forget()
    widgets_visible = False


explore_button = customtkinter.CTkButton(app, text="Explore", command=explore_fullscreen,text_color="black",hover_color="SeaGreen1",corner_radius=15,bg_color="transparent")
explore_button.pack(padx=20, pady=115)

widgets_button = customtkinter.CTkButton(app, text="Widgets", command=toggle_widgets, text_color="black",hover_color="SeaGreen1",corner_radius=15,bg_color="transparent")

# These Buttons Are Widgets
def open_clock():
    theclock.launch_clock()

def open_calendar():
    cal.launch_calendar()

def open_calc():
    CalculatorApp().run()

clock_button = customtkinter.CTkButton(app,
    text="Clock",
    command=open_clock,
    width=100,
    compound="left",
    fg_color="transparent",  # 🔥 was neon green
    bg_color="transparent",
    text_color="#333333",     # softer than pure black
    hover_color="#e6e6e6",    # soft gray hover
    corner_radius=15
)

calendar_button = customtkinter.CTkButton(app, text="Calendar", command=open_calendar, width=100,compound="left",
    
    
    fg_color="transparent",  # 🔥 was neon green
    bg_color="transparent",
    text_color="#333333",     # softer than pure black
    hover_color="#e6e6e6",    # soft gray hover
    corner_radius=15
)
calc_button = customtkinter.CTkButton(app, text="Calculator", command=open_calc, width=100,compound="left",
   
    fg_color="transparent",  # 🔥 was neon green
    bg_color="transparent",
    text_color="#333333",     # softer than pure black
    hover_color="#e6e6e6",    # soft gray hover
    corner_radius=15
)
calc_label=customtkinter.CTkLabel(app,text="This widget is under construction, please access it manually. ", compound="left",
    fg_color="transparent",  # 🔥 was neon green
    bg_color="transparent",
    text_color="#333333",     # softer than pure black
    
    corner_radius=15)

# Hide widgets initially
hide_widgets()
widgets_button.place_forget()

# Joke display section
# Add this near the top
# --- Pyjokes Section (Left Side) ---
# --- Pyjokes Section (Left Side) ---
def get_joke():
    return pyjokes.get_joke(language="en", category="neutral")

def update_joke():
    joke_label.configure(text=get_joke())

# Define them but don't place them yet
joke_label = customtkinter.CTkLabel(app,
    text="",
    wraplength=300,
    font=("Arial", 14),
    text_color="#39FF14",bg_color="transparent",
    justify="left",corner_radius=15)

joke_button = customtkinter.CTkButton(app,
    text="Get Joke",
    command=update_joke,
    bg_color="transparent",
    
    
    text_color="black",
    hover_color="SeaGreen1",
    corner_radius=15)



app.bind("<Escape>", lambda e: explore_fullscreen())

app.mainloop()

# to do 
# random quotes
# text to speach for jokes

# news
# pomodoro timer