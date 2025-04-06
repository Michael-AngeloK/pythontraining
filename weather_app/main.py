# [x] Display temperature, humidity, and weather conditions for a user-input city
# [x] Save each successful weather query to a file
# [x] Display search history when the user types "history"
# [x] Add timestamps to each entry

import os
from dotenv import load_dotenv
from requests import HTTPError, get
from datetime import datetime
from weather_app.models import WeatherData
# import json

class WeatherAPIError(Exception):
    """Base class for all weather-related errors"""
    pass

class InvalidCityError(WeatherAPIError):
    """Raised when the city doesn't exist"""
    pass

class APIRequestError(WeatherAPIError):
    """Raised when the API request fails (e.g., no internet, wrong API key)"""
    pass

def validate_config():
    """Validate required config"""
    API_KEY = os.getenv("OPENWEATHER_API_KEY")
    if not API_KEY:
        raise APIRequestError("Missing API key - please check your .env file")
    return API_KEY

load_dotenv()  # Loads variables from .env


# Get the script's directory and set history file path
script_dir = os.path.dirname(os.path.abspath(__file__))
history_file = os.path.join(script_dir, "weather_history.txt")

try:
    API_KEY = validate_config()
    print("=== Weather app ===")
    while True:
        # Get user input for city
        try:
            city = input("\nEnter a city name (or 'history'/'exit): ").strip().lower()
            
            if not city:
                print("Format does not allow empty input")
                continue
            
            elif not city.replace(" ", "").isalpha():
                raise ValueError("City name must contain only letters")
            
            elif city == "history":
                try:
                    with open(history_file, "r") as file:
                        print("Search history:")
                        print(file.read())
                except FileNotFoundError:
                    print("File not found!")
                continue
            
            elif city == "delete history":
                if os.path.exists(history_file):
                    os.remove(history_file)
                else:
                    print("File not found!")  
                continue
            
            elif city == "exit":
                print("Exiting... Goodbye!")
                break
            
            try:
                params = {
                    'q': city,
                    'appid': API_KEY
                }
                # Fetch data from the OpenWeatherMap api of the decided city
                response = get("https://api.openweathermap.org/data/2.5/weather", params=params)

                # If successful: parse the data
                if response.status_code == 200:
                    print("Request succesful")
                    data = WeatherData(city, response.json())
                    
                    # Save succesfull query in a file
                    with open(history_file, "a") as file:
                        now = datetime.now().strftime("%d.%m.%Y %H:%M")
                        file.write(f"{now} | {city.title()} | {data.temperature_formatted}\n")
                    
                    # print(json.dumps(jsonResponse, indent=4))
                    
                    # Display results
                    data.displayWeather()
                
                elif response.status_code == 404:
                    raise InvalidCityError(f"City '{city}' doesn't exist")
                
                response.raise_for_status()
            
            except HTTPError as e:
                raise APIRequestError(f"API failed: {e}") 
            except InvalidCityError as e:
                print(f"Check the city name: {e}")
            except APIRequestError as e:
                print(f"API request error: {e}. Try again later.")
            except Exception as e:
                print(f"Unexpected error occured: {e}")
                
        except ValueError as e:
            print(f"Invalid input: {e}")
            
except APIRequestError as e:
    print(f"Configuration error: {e}")
    exit(1)
except Exception as e:
    print(f"Unexpected error occured: {e}")
    exit(1)