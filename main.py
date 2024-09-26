from argumentos import parse_arguments
from clima import get_weather_data
from salida import print_weather, print_as_json, print_as_csv

def main():
    args = parse_arguments()
    weather_data = get_weather_data(args.location)

    if weather_data:
        if args.format == "json":
            print_as_json(weather_data)
        elif args.format == "csv":
            print_as_csv(weather_data)
        else:
            print_weather(weather_data)
    else:
        print("Error: No se pudo encontrar la ubicación especificada o hubo un problema con la solicitud.")

if __name__ == "__main__":
    main()
