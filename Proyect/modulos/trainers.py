import json

def crearJsonTrainers():
    datos = {
        "Pedro": [],
        "Jholver": [],
        "Miguel": [],
        "Garcia": [],
        "Holguer": [],
        "Efrain": []
    }
    jsonData = json.dumps(datos, indent=4)
    rutaArchivo = "trainers.json"
    with open(rutaArchivo, 'w') as archivo:
        archivo.write(jsonData)
    return rutaArchivo
def crearJsonTrainers():
    datos = {
        "Pedro": [],
        "Jholver": [],
        "Miguel": [],
        "Garcia": [],
        "Holguer": [],
        "Efrain": [],
    }
    jsonData = json.dumps(datos, indent=4)
    rutaArchivo = "trainers.json"
    with open(rutaArchivo, 'w') as archivo:
        archivo.write(jsonData)
    return rutaArchivo

jsonGeneracion = crearJsonTrainers()
jsonGeneracion = crearJsonTrainers()

def agregarDato(ruta_archivo, trainer, nuevo_dato):
    with open(ruta_archivo, 'r') as t:
        jsonDato = json.load(t)
        if trainer in jsonDato:
            jsonDato[trainer].append(nuevo_dato)
        else:
            print(f"El trainer {trainer} no existe en el JSON.")
            return
    with open(ruta_archivo, 'w') as file:
        json.dump(jsonDato, file, indent=4)
def agregarDato(ruta_archivo, trainer, nuevo_dato):
    with open(ruta_archivo, 'r') as t:
        jsonDato = json.load(t)
        if trainer in jsonDato:
            jsonDato[trainer].append(nuevo_dato)
        else:
            print(f"El trainer {trainer} no existe en el JSON.")
            return
    with open(ruta_archivo, 'w') as file:
        json.dump(jsonDato, file, indent=4)

ruta_json = 'trainers.json'
for trainer in ["Pedro", "Jholver", "Miguel", "Garcia", "Holguer", "Efrain"]:
    nuevo_dato = input(f"Ingrese el salon para {trainer}: ")
    agregarDato(ruta_json, trainer, nuevo_dato)
ruta_json = 'trainers.json'
for trainer in ["Pedro", "Jholver", "Miguel", "Garcia", "Holguer", "Efrain"]:
    nuevo_dato = input(f"Ingrese un dato para {trainer}: ")
    agregarDato(ruta_json, trainer, nuevo_dato)

with open(ruta_json, 'r') as j:
    jsonDato = json.load(j)
    for trainer, datos in jsonDato.items():
        print(f"{trainer}: {datos}")