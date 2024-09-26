import requests
from config import API_KEY


def get_weather_data(location):
    api_key = API_KEY  # Usar la API key de OPENWEATHERMAP
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": location, "appid": api_key, "units": "metric", "lang": "es"}
    response = requests.get(base_url, params=params)
    print(f"Código de estado: {response.status_code}")
    if response.status_code == 200:
        data = response.json()
        print("Datos de la API:")
        print(data)  # Imprime todos los datos de la API
        return data
    else:
        print("Error al obtener los datos.")
        print(f"Mensaje de error: {response.text}")
        return None


if __name__ == "__main__":
    location = input("Ingresa la ciudad y el país (ejemplo: Asuncion-PY): ")
    get_weather_data(location)
