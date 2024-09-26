import requests

def get_weather_data(location):
    api_key = "489cf306c218f90bc09f9539bd195c81"  # Reemplaza con tu propia API key
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": location, "appid": api_key, "units": "metric"}
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None
