import json

def print_weather(data):
    if data:
        temp = round(data['main']['temp'], 2)
        feels_like = round(data['main']['feels_like'], 2)
        location = data['name']
        description = data['weather'][0]['description']
        
        print(f"Clima en {location}:")
        print(f"Temperatura: {temp}°C")
        print(f"Sensación térmica: {feels_like}°C")
        print(f"Condiciones: {description}")
        print(f"Humedad: {data['main']['humidity']}%")

def print_as_json(data):
    temp = round(data['main']['temp'], 2)
    feels_like = round(data['main']['feels_like'], 2)
    
    data_to_print = {
        'ubicacion': data['name'],
        'temperatura': temp,
        'sensacion_termica': feels_like,
        'descripcion': data['weather'][0]['description'],
        'humedad': data['main']['humidity']
    }
    print(json.dumps(data_to_print, indent=2, ensure_ascii=False))

def print_as_csv(data):
    temp = round(data['main']['temp'])
    feels_like = round(data['main']['feels_like'])
    location = data['name']
    description = data['weather'][0]['description']
    
    print(f"ubicacion,temperatura,sensacion_termica,descripcion,humedad")
    print(f"{location},{temp},{feels_like},{description},{data['main']['humidity']}")
