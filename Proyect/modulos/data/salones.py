import json

def crearJsonSalones():
    datos = {
        "Artemis": {
            "trainer": input("Ingrese el nombre del entrenador de Artemis: "),
            "Horario": input("Ingrese el horario de Artemis: "),
            "Ruta": input("Ingrese la ruta de Artemis: ")
        },
        "Apolo": {
            "trainer": input("Ingrese el nombre del entrenador de Apolo: "),
            "Horario": input("Ingrese el horario de Apolo: "),
            "Ruta": input("Ingrese la ruta de Apolo: ")
        },
        "Sputnik": {
            "trainer": input("Ingrese el nombre del entrenador de Sputnik: "),
            "Horario": input("Ingrese el horario de Sputnik: "),
            "Ruta": input("Ingrese la ruta de Sputnik: ")
        }
    }
    jsonData = json.dumps(datos, indent=4)
    rutaArchivo = "salones.json"
    with open(rutaArchivo, 'w') as archivo:
        archivo.write(jsonData)
    return rutaArchivo

def seleccionarTrainer():
    with open('trainers.json', 'r') as archivo:
        trainers = json.load(archivo)

    print("Por favor, seleccione un trainer:")
    for i, trainer in enumerate(trainers, start=1):
        print(f"{i}. {trainer}")

    seleccion = int(input("Ingrese el número del trainer: "))
    return trainers[seleccion - 1]

jsonCrear = crearJsonSalones()
trainer_seleccionado = seleccionarTrainer()
print(f"Has seleccionado a {trainer_seleccionado}")

