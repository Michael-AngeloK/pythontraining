# Goal: Display temperature, humidity, and weather conditions for a user-input city
from config import API_KEY
from requests import get
import json

while True:
    # Get user input for city
    try:
        city = input("What city would you like to know it's weather conditions of? ").strip().lower()

        try:
            # Build API request
            request = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + API_KEY

            # Fetch data from the OpenWeatherMap api of the decided city
            response = get(request)

            # If successful: parse the data
            if response.status_code == 200:
                print("Request succesful")
                jsonResponse = response.json()
                
                # Display results
                print(json.dumps(jsonResponse, indent=4))
                print(f"Weather data in {city}")
                print(f"Temperature is: {jsonResponse['main']['temp'] - 272.15:.1f}°C")
                print(f"Humidity is: {jsonResponse['main']['humidity']}")
                print(f"Weather condition is: {jsonResponse['weather'][0]['description']}")
        
            else:
                print(f"API Request failed with status code: {response.status_code}")
        
        except Exception as e:
            print(f"Other error occured: {e}")
    except ValueError as e:
        print(f"Invalid input:{e}")
        

# If failed show error