import json

def crearJsonRutas():
    datos = {
        "nodejs": [],
        "java": [],
        "netcore": []
    }
    jsonData = json.dumps(datos, indent=4)
    rutaArchivo = "rutas.json"
    with open(rutaArchivo, 'w') as archivo:
        archivo.write(jsonData)
    return rutaArchivo

jsonGeneracion = crearJsonRutas()

def imprimirJsonRuta():
    rutaJson = "rutas.json"
    with open(rutaJson, 'r') as f:
        json_data = json.load(f)
        for ruta, sub_rutas in json_data.items():
            print(f"{ruta}: {sub_rutas}")

def agregarSubRuta(ruta_archivo, ruta, nuevo_item):
    with open(ruta_archivo, 'r') as t:
        jsonDato = json.load(t)
        if ruta in jsonDato:
            jsonDato[ruta].append(nuevo_item)
        else:
            print(f"La ruta {ruta} no existe en el JSON.")
            return
    with open(ruta_archivo, 'w') as file:
        json.dump(jsonDato, file, indent=4)

def actualizarSubRutas(ruta_archivo):
    print("Que ruta deseas actualizar? (NodeJS, Java, NetCore)")
    imprimirJsonRuta()
    ruta = input().lower()
    if ruta in ["nodejs", "java", "netcore"]:
        with open(ruta_archivo, 'r') as f:
            json_data = json.load(f)
            print(f"Sub Rutas de {ruta}: {json_data[ruta]}")
            if json_data[ruta]:
                print("¿Cual es el indice de la sub ruta que deseas editar?")
                try:
                    indice = int(input())
                    if 0 <= indice < len(json_data[ruta]):
                        print(f"Sub ruta actual en el indice {indice}: {json_data[ruta][indice]}")
                        nueva_subRuta = input("ingrese la nueva subRuta: ")
                        json_data[ruta][indice] = nueva_subRuta
                        with open(ruta_archivo, 'w') as archivo:
                            json.dump(json_data, archivo, indent=4)
                        print("subRuta actualizada exitosamente")
                    else:
                        print("Indice fuera de rango")
                except ValueError:
                    print("Porfavor, ingrese un numero valido")
            else:
                print("No hay subrutas para editar en esta ruta")
    else:
        print("Ruta no valida")

def optionRutas():
    print("Menu de opciones:\n1 Agregar subRutas\n2 Eliminar subrutas\n3 Actualizar subrutas\n4 Ver Sub Rutas actuales")
    try:
        answerR = int(input())
        if answerR == 1:
            print("¿En qué ruta deseas agregar? (NodeJS, Java, NetCore)")
            imprimirJsonRuta()
            answer_r = input().lower()
            if answer_r in ["nodejs", "java", "netcore"]:
                print("¿Cuántas sub rutas vas a ingresar?")
                try:
                    num_rutas = int(input())
                    if num_rutas > 0:
                        ruta_json = 'rutas.json'
                        for i in range(num_rutas):
                            nuevoItemUsuario = input(f"Ingrese la sub Ruta {i+1} para {answer_r}\n")
                            agregarSubRuta(ruta_json, answer_r, nuevoItemUsuario)
                        with open(ruta_json, 'r') as j:
                            jsonDato = json.load(j)
                            print(json.dumps(jsonDato, indent=4))
                    else:
                        print("El número de rutas debe ser mayor a 0.")
                except ValueError:
                    print("Por favor, ingrese un número válido.")
            else:
                print("Ruta no válida.")
        elif answerR == 2:
            print("Esta opción aún no está implementada.")
        elif answerR == 3:
            ruta_json = 'rutas.json'
            actualizarSubRutas(ruta_json)
            with open(ruta_json, 'r') as j:
                jsonDato = json.load(j)
                print(json.dumps(jsonDato, indent=4))
        elif answerR == 4:
            imprimirJsonRuta()
        else:
            print("Opción no válida.")
    except ValueError:
        print("Por favor, ingrese un número válido.")

print("Actualmente manejamos 3 rutas principales:")
imprimirJsonRuta()
optionRutas()