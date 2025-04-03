# Goal: Display temperature, humidity, and weather conditions for a user-input city
from config import API_KEY
from requests import get
import json

# Get user input for city
city = input("What city would you like to know it's weather conditions of? ")

# Build API request
request_build = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + API_KEY

# Fetch data from the OpenWeatherMap api of the decided city
request = get(request_build)

# If successful: parse the data
if 

# Display results


# If failed show error