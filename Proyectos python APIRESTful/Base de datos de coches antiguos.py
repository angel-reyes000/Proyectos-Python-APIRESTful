import requests
import json

def verificar_servidor(cid=None):
    # devuelve True o False;
    # cuando se invoca sin argumentos simplemente verifica si el servidor responde;
    if cid is None:
        return False
    # si se invoca con un ID de auto verifica si el ID está presente en la base de datos;
    else:
        respuesta = requests.get("http://localhost:3000/cars/")
        return True

def imprimir_menu():
    # imprime el menú del usuario - no ocurre nada más aquí;
    print("+", end="")
    for q in range(35):
        print("-", end="")
    print("+")
    print("|".ljust(7), "Vintage Cars Database", "|".rjust(7))
    print("+", end="")
    for q in range(35):
        print("-", end="")
    print("+")
    print("M E N U")
    for q in range(8):
        print("=", end="")
    print()
    opciones = ["List cars", "Add new car", "Delete car", "Update car", "Exit"]
    numeros = 0
    for q in opciones:
        numeros+=1
        if numeros == 5:
            numeros-=5
            print(str(numeros)+". "+q)
        else:
            print(str(numeros)+". "+q)

def leer_opcion_usuario():
    # lee la opción del usuario y verifica si es válida;
    opcion = input("Enter your choice(0..4): ")
    respuesta = opcion
    # devuelve '0', '1', '2', '3' o '4' 
    if respuesta in ["0", "1", "2", "3", "4"]:
        return respuesta
    else:
        return None
    
def imprimir_encabezado():
    # imprime el encabezado elegante de la tabla de autos;
    encabezado = ["id", "brand", "model", "production_year", "convertible"]
    espacios = [10, 20, 20, 20, 15]
    for temas, espacios in zip(encabezado, espacios):
        print(temas.ljust(espacios), end="|")
    print()

def imprimir_auto(auto):
    # imprime los datos de un auto de manera que coincida con el encabezado;
    espacios = [10, 20, 20, 20, 15]
    for datos, esp in zip(auto.values(), espacios):
        print(datos.ljust(esp), end="|")
    print()

def listar_autos():
    # obtiene todos los datos de autos del servidor y los imprime;
    server = "http://localhost:3000/cars"
    respuesta = requests.get(server)
    # si la base de datos está vacía imprime un mensaje diagnóstico;
    try:
        datos = respuesta.json()
        if isinstance(datos, list) and not datos:
            print("*** Database is empty ***")
        else:
            for q in datos:
                print(q)
    except ValueError:
        print("Json no valido")

def nombre_es_valido(nombre):
    # verifica si el nombre (marca o modelo) es válido;
    # un nombre válido es una cadena no vacía que contiene
    # dígitos, letras y espacios;
    # devuelve True o False;
    if isinstance(nombre, str) and nombre.strip() != "":
        return all(n.isspace() or n.isalnum for n in nombre)
    return False

def ingresar_id():
    # permite al usuario ingresar el ID del auto y verifica si es válido;
    # un ID válido consiste solo en dígitos;
    try:
        id_carro = int(input("Car ID (empty string to exit): "))
    # devuelve int o None (si el usuario ingresa una línea vacía);
    except ValueError:
        return "Solo numeros y sin espcios"
    else:
        if id_carro == "":
            return None
        return id_carro
    

def ingresar_anio_produccion():
    # permite al usuario ingresar el año de producción del auto y verifica si es válido;
    try:
        anio = int(input("Car production year (empty string to exit)"))
        if anio in [x for x in range(1900, 2001)] and anio != "":
            return anio
        return None
    # un año de producción válido es un int en el rango 1900..2000;
    # devuelve int o None (si el usuario ingresa una línea vacía);
    except ValueError:
        return None


def ingresar_nombre(que):
    # permite al usuario ingresar el nombre del auto (marca o modelo) y verifica si es válido;
    marca_modelo = ""
    if que == "marca":
        marca = input("Car brand (empty string to exit): ")
        marca_modelo = marca
    elif que == "modelo":
        modelo = input("Car model (empty string to exit): ")
        marca_modelo = modelo
    # usa nombre_es_valido() para verificar el nombre ingresado;
    # devuelve una cadena o None (si el usuario ingresa una línea vacía);
    if nombre_es_valido(marca_modelo):
        return marca_modelo
    return None
    # el argumento describe cuál de los dos nombres se está ingresando actualmente ('marca' o 'modelo');


def ingresar_convertible():
    # permite al usuario ingresar una respuesta Sí/No que determina si el auto es convertible;
    pregunta = input("Is this car convertible? [y/n] (empty string to exit): ")
    # devuelve True, False o None (si el usuario ingresa una línea vacía);
    if len(pregunta) == 1 and pregunta in ["n", "y"]:
        if pregunta == "n":
            return False
        elif pregunta == "y":
            return True
    else:
        return False

def eliminar_auto():
    # solicita al usuario el ID del auto e intenta eliminarlo de la base de datos;
    try:
        borrar = input("Car ID (empty string to exit): ")
        respuesta = borrar
        url = "http://localhost:3000/cars/"+str(respuesta)
        server = requests.get("http://localhost:3000/cars/")
        rep = requests.delete(url, headers={"Connection":"Close"})
        print ("Success!")
    except requests.RequestException as e:
        return ("Error: ", e)
    except ValueError as e:
        return "Error: ", e


def ingresar_datos_auto(con_id):
    # permite al usuario ingresar los datos del auto;
    # el argumento determina si se ingresa el ID del auto (True) o no (False);
    valor_id = ingresar_id()
    valor_marca = ingresar_nombre("marca")
    valor_modelo = ingresar_nombre("modelo")
    valor_anio = ingresar_anio_produccion()
    valor_convertible = ingresar_convertible()
    # devuelve None si el usuario cancela la operación o un diccionario con la siguiente estructura:
    # {'id': int, 'marca': str, 'modelo': str, 'anio_produccion': int, 'convertible': bool }
    if valor_id and valor_marca and valor_modelo and valor_anio and valor_convertible in [True, False]:
        return {'id': valor_id, 'marca': valor_marca, 'modelo': valor_modelo, 'anio_produccion': valor_anio, 'convertible': valor_convertible}
    elif isinstance(con_id, dict):
        return None
    return None

def agregar_auto():
    # invoca ingresar_datos_auto(True) para recopilar la información del auto y lo agrega a la base de datos;
    encabezados = {"content-type":"application/json", "Connection":"Close"}
    valor = ingresar_datos_auto(True)
    if valor:
        server = requests.get("http://localhost:3000/cars/")
        requests.post("http://localhost:3000/cars/", headers=encabezados, data=json.dumps(valor))
    else:
        print("Error al agregar")

def actualizar_auto():
    # invoca ingresar_id() para obtener el ID del auto si el ID está presente en la base de datos;
    valor_id = ingresar_id()
    car_id = "http://localhost:3000/cars/"+str(valor_id)
    # invoca ingresar_datos_auto(False) para recopilar la nueva información del auto y actualizar la base de datos;
    encabezados = {"content-type":"application/json", "Connection":"Close"}
    if car_id:
        datos = ingresar_datos_auto(True)
        server = requests.get("http://localhost:3000/cars/")
        resp = requests.put(car_id, headers=encabezados, data=json.dumps(datos))
    return None

while True:
    if not verificar_servidor("http://localhost:3000/cars"):
        print("¡El servidor no responde - saliendo!")
        exit(1)
    imprimir_menu()
    opcion = leer_opcion_usuario()
    if opcion == '0':
        print("¡Adiós!")
        exit(0)
    elif opcion == '1':
        listar_autos()
    elif opcion == '2':
        agregar_auto()
    elif opcion == '3':
        eliminar_auto()
    elif opcion == '4':
        actualizar_auto()
