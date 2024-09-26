import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description="Consulta el clima de una ubicación.")
    parser.add_argument("location", type=str, help="Nombre de la ciudad y país (Ej: Asuncion-PY)")
    parser.add_argument("-format", type=str, choices=["json", "csv", "text"], default="text", help="Formato de salida")
    return parser.parse_args()
