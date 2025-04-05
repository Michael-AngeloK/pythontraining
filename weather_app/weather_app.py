# [x] Display temperature, humidity, and weather conditions for a user-input city
# [ ] Save each successful weather query to a file
# [ ] Display search history when the user types "history"
# [ ] Bonus: Add timestamps to each entry

from config import API_KEY
from requests import get

def displayWeather(jsondata):
    print(f"Weather data in {city.title()}")
    print(f"Temperature is: {jsondata['main']['temp'] - 272.15:.1f}°C")
    print(f"Humidity is: {jsondata['main']['humidity']}")
    print(f"Weather condition is: {jsondata['weather'][0]['description']}")


while True:
    # Get user input for city
    try:
        print("=== Weather app ===")
        city = input("What city would you like to know it's weather conditions of? ").strip().lower()
        if not city:
            print("Format does not allow empty input")
            continue
        elif city == "history":
            try:
                with open("weather_history.txt", "r") as file:
                    print("Search history:")
                    print(file.read())
            except FileNotFoundError:
                print("File not found")
            continue
        elif city == "exit":
            print("Exiting... Goodbye!")
            break
        try:
            # Build API request
            request = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + API_KEY

            # Fetch data from the OpenWeatherMap api of the decided city
            response = get(request)

            # If successful: parse the data
            if response.status_code == 200:
                print("Request succesful")
                jsonResponse = response.json()
                
                # Save succesfull query in a file
                with open("weather_history.txt", "a") as file:
                    file.write(f"city: {city.title()}, temperature: {jsonResponse['main']['temp'] - 272.15:.1f}°C\n")
                
                # print(json.dumps(jsonResponse, indent=4))
                
                # Display results
                displayWeather(jsonResponse)
                
            else:
                print(f"API Request failed with status code: {response.status_code}")
        
        except Exception as e:
            print(f"Other error occured: {e}")
    except ValueError as e:
        print(f"Invalid input:{e}")