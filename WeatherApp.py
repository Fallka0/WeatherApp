import json
import requests
import customtkinter
import packaging
import sqlite3
import hashlib

conn = sqlite3.connect("userdata.db")
cur = conn.cursor()


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")
root = customtkinter.CTk()
root.geometry("600x400")

def login():
    print("test")
    
frame = customtkinter.CTkFrame(master = root)
frame.pack(pady = 20, padx = 60, fill = "both", expand = True)

label = customtkinter.CTkLabel(master=frame, text= "Login System")
label.pack(pady = 12, padx = 20)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
entry1.pack(pady=12, padx=10)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="********")
entry1.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text = "Login", command = login)
button.pack(pady=12, padx=10, )

checkbox = customtkinter.CTkCheckBox(master=frame, text="Remember Me")
checkbox.pack(pady = 12, padx=10, )

root.mainloop()
    
def getWeather():
    API_KEY = "609700f517794fe7b5090429230612"


    city = input("Enter a city: ")

    url = "http://api.weatherapi.com/v1/current.json?key=609700f517794fe7b5090429230612&q=" + city
    
    response = requests.get(url).json()
    temp_c = response ["current"]["temp_c"]
    temperatur = str(temp_c)
    print("Temperature in " + city + " is: " + temperatur + " Celsium")