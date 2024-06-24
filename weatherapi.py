import tkinter as tk
from tkinter import ttk
import requests
import json
import os

def get_weather_data():
    city = city_entry.get()
    url = f"https://api.weatherapi.com/v1/current.json?key=39165204343341cb853163540230506&q={city}"

    response = requests.get(url)
    response.raise_for_status()
    weather_data = json.loads(response.text)

    try:
        t = weather_data['current']['temp_c']
        c = weather_data['current']['condition']['text']
        h = weather_data['current']['humidity']
        w = weather_data['current']['wind_kph']
        d = weather_data['current']['wind_dir']
        p = weather_data['current']['pressure_mb']
        v = weather_data['current']['vis_km']

        result_label.config(text=f"{city}'s Weather: {t} degrees\n"
                            f"Humidity: {h}\n"
                            f"Wind Speed: {w} kilometres per hour towards {d} direction\n"
                            f"Pressure: {p} mb/n\n"
                            f"Visibility: {v} km")

        os.system(f"say 'The current weather in {city} is {t} degrees and {c} with {h} humidity {p} pressure and {v} visibility kilometres recorded and wind speed of {w} kilometers per hour towards {d} direction.'")
    except requests.exceptions.HTTPError as e:
        result_label.config(text=f"Error: {e.response.status_code} - {e.response.reason}")


root = tk.Tk()
root.title("Weather Report")
root.geometry("400x300")

style = ttk.Style()
style.configure("TFrame", background="white")
style.configure("TLabel", background="white", font=("Arial", 12))

main_frame = ttk.Frame(root, padding=20)
main_frame.grid(row=0, column=0)

city_label = ttk.Label(main_frame, text="Enter City: ")
city_label.grid(row=0, column=0, pady=10)

city_entry = ttk.Entry(main_frame)
city_entry.grid(row=0, column=0, padx=10, pady=10)

get_weather_button = ttk.Button(main_frame, text="Get Weather", command=get_weather_data)
get_weather_button.grid(row=0, column=2, padx=10, pady=10)

result_label = ttk.Label(main_frame, wraplength=400)
result_label.grid(row=1, column=0, columnspan=3, padx=10, pady=20)

root.mainloop()