from datetime import datetime

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