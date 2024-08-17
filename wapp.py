import tkinter as tk
from tkinter import font
import requests

# Function to fetch and display weather data
def get_weather():
    city = city_entry.get()
    url = f"http://api.weatherapi.com/v1/current.json?key=8de403809a3b406e8eb195106240902&q={city}"
    response = requests.get(url)
    weather_data = response.json()
    current_weather = weather_data.get("current", {})
    
    # Update all the weather information labels
    temp_value.config(text=f"{current_weather.get('temp_c')}°C")
    humidity_value.config(text=f"{current_weather.get('humidity')}%")
    wind_value.config(text=f"{current_weather.get('wind_kph')} kph")
    uv_value.config(text=f"{current_weather.get('uv')}")
    pressure_value.config(text=f"{current_weather.get('pressure_mb')} mb")
    precipitation_value.config(text=f"{current_weather.get('precip_mm')} mm")
    visibility_value.config(text=f"{current_weather.get('vis_km')} km")
    feels_like_value.config(text=f"{current_weather.get('feelslike_c')}°C")

# Create the main window
root = tk.Tk()
root.title("Professional Weather App")
root.geometry("800x600")
root.configure(bg="#1e272e")  # Background color

# Define custom fonts
title_font = font.Font(family="Helvetica", size=26, weight="bold")
label_font = font.Font(family="Helvetica", size=14)
value_font = font.Font(family="Helvetica", size=18, weight="bold")

# Title Label
title_label = tk.Label(root, text="Weather App", font=title_font, fg="white", bg="#1e272e")
title_label.pack(pady=20)

# City entry frame for better styling
city_frame = tk.Frame(root, bg="#2f3640", bd=2)
city_frame.pack(pady=10)

city_label = tk.Label(city_frame, text="Enter City:", font=label_font, fg="white", bg="#2f3640")
city_label.grid(row=0, column=0, padx=5, pady=5)

city_entry = tk.Entry(city_frame, font=label_font, bg="#dcdde1", bd=1, relief="solid")
city_entry.grid(row=0, column=1, padx=5, pady=5)

get_weather_btn = tk.Button(root, text="Get Weather", command=get_weather, font=label_font, bg="#e74c3c", fg="white", bd=0, relief="solid", padx=20, pady=10)
get_weather_btn.pack(pady=20)

# Frame for weather information
info_frame = tk.Frame(root, bg="#1e272e")
info_frame.pack(pady=20)

# Function to create a custom graphical container for each weather parameter
def create_container(frame, title, row, column):
    container = tk.Frame(frame, bg="#2f3640", bd=2, relief="ridge", width=200, height=100)
    container.grid(row=row, column=column, padx=15, pady=15, sticky="nsew")
    
    container.grid_propagate(False)  # Prevent the frame from resizing
    
    title_label = tk.Label(container, text=title, font=label_font, fg="#dcdde1", bg="#2f3640")
    title_label.pack(pady=5)
    
    value_label = tk.Label(container, text="...", font=value_font, fg="#00a8ff", bg="#2f3640")
    value_label.pack(pady=5)
    
    return value_label

# Create containers for each weather parameter
temp_value = create_container(info_frame, "Temperature", 0, 0)
humidity_value = create_container(info_frame, "Humidity", 0, 1)
wind_value = create_container(info_frame, "Wind Speed", 0, 2)
uv_value = create_container(info_frame, "UV Index", 1, 0)
pressure_value = create_container(info_frame, "Pressure", 1, 1)
precipitation_value = create_container(info_frame, "Precipitation", 1, 2)
visibility_value = create_container(info_frame, "Visibility", 2, 0)
feels_like_value = create_container(info_frame, "Feels Like", 2, 1)

# Adjust grid weights for responsiveness
info_frame.grid_rowconfigure(0, weight=1)
info_frame.grid_rowconfigure(1, weight=1)
info_frame.grid_rowconfigure(2, weight=1)
info_frame.grid_columnconfigure(0, weight=1)
info_frame.grid_columnconfigure(1, weight=1)
info_frame.grid_columnconfigure(2, weight=1)

# Run the application
root.mainloop()
