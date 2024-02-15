import json

def crearJsonHorarios():
    datos = {
        {"mañana1": "6:00-9:30"},
        {"mañana2": "10:00-14:00"},
        {"tarde1": "14:00-17:30"},
        {"tarde2": "18:00-22:00"}
    }
    jsonData = json.dumps(datos, indent=4)
    rutaArchivo = "horarios.json"
    with open(rutaArchivo)
