import json
import requests
import customtkinter
import packaging
from urllib.parse import quote



customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")
root = customtkinter.CTk()
root.geometry("600x400")

    

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

user_db = [
    User(username="falka0", password="falkao01")
]


cityEntry = None
cityInfo = None

def transition_to_new_page(root):
    global cityEntry, cityInfo

    new_page_frame = customtkinter.CTkFrame(master=root)
    new_page_frame.pack(pady=20, padx=60, fill="both", expand=True)

   
    label_new_page = customtkinter.CTkLabel(master=new_page_frame, text="The Weather App")
    label_new_page.pack(pady=12, padx=20)

    cityEntry = customtkinter.CTkEntry(master=new_page_frame, placeholder_text="Enter city:")
    cityEntry.pack(pady=12, padx=10)

    cityInfo = customtkinter.CTkTextbox(master=new_page_frame)
    cityInfo.configure(state="disabled")
    cityInfo.pack(pady=12, padx=10)

    getWeather()

def getWeather():
    global cityEntry, cityInfo

    city = cityEntry.get().strip()
    encoded_city = quote(city)  
    
    API_KEY = "609700f517794fe7b5090429230612"
    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for request errors

        weather_data = response.json()
        temp_c = weather_data["current"]["temp_c"]
        temperature = str(temp_c)

        cityInfo.configure(state="normal")
        cityInfo.insert("0.0", f"The temperature in {city} is {temperature} Celsius\n")
        cityInfo.configure(state="disabled")

    except requests.RequestException as e:
        print(f"Request Error: {e}")
    except json.JSONDecodeError as e:
        print(f"JSON Decode Error: {e}")
    except KeyError as e:
        print(f"Key Error: {e}")


 

def login():
    entered_username = entry1.get()
    entered_password = entry2.get()

    for user in user_db:
        if user.username == entered_username and user.password == entered_password:
            print("Login successful")   
            frame.destroy()
            transition_to_new_page(root)
            return

    print("Error: Invalid username or password")

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")
root = customtkinter.CTk()
root.geometry("600x400")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Login System")
label.pack(pady=12, padx=20)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
entry1.pack(pady=12, padx=10)

entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Password")
entry2.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Login", command=login)
button.pack(pady=12, padx=10)

checkbox = customtkinter.CTkCheckBox(master=frame, text="Remember Me")
checkbox.pack(pady=12, padx=10)

root.mainloop()

