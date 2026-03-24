from weather_app.weather_api import WeatherAPI
from weather_app.weather_parser import parse_current_weather, parse_forecast
from weather_app.weather_display import show_current_weather, show_forecast
from weather_app import config

def main():
    api = WeatherAPI(config.API_KEY)
    city = input("Enter city name: ")
    current = parse_current_weather(api.get_current_weather(city))
    forecast = parse_forecast(api.get_forecast(city))

    show_current_weather(current)
    show_forecast(forecast)

if __name__ == "__main__":
    main()
