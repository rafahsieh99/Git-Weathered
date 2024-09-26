import requests
from config import API_KEY


def get_weather_data(location):
    api_key = API_KEY  # Reemplaza con tu propia API key de OPENWEATHERMAP
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": location, "appid": api_key, "units": "metric"}
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None
