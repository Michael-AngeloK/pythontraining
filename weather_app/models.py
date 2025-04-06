from datetime import datetime
from requests import get

class WeatherData:
    CELSIUS = "°C"
    def __init__(self, name, jsondata):
        self.cityName = name
        self.temperature = jsondata['main']['temp'] - 273.15
        self.humidity = jsondata['main']['humidity']
        self.description = jsondata['weather'][0]['description']
        self.timestamp = datetime.now()
        
    @property
    def temperature_formatted(self):
        return f"{self.temperature:.1f}{self.CELSIUS}"
    
    def __str__(self):
        return f"{self.cityName}: {self.temperature}°C, {self.description.capitalize()}"
        
    def __repr__(self):
        return f"WeatherData(city='{self.cityName}', temp={self.temperature})"
    
    def displayWeather(self):
        print(f"Weather data in {self.cityName.title()}")
        print(f"Temperature is: {self.temperature_formatted}")
        print(f"Humidity is: {self.humidity}")
        print(f"Weather condition is: {self.description.capitalize()}") 

class WeatherFetcher:
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
    
    def __init__(self, api_key):
        self.api_key = api_key
    
    def fetch_weather(self, api_key, city):
        params = {
            'q': city,
            'appid': api_key
        }
        response = get(self.BASE_URL, params=params)
        response.raise_for_status()
        return WeatherData(city, response.json()), response.status_code