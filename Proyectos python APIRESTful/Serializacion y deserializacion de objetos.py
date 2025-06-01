import json

class vehiculo:
    def __init__(self, numero_registro, año_produccion, pasajero, peso):
        self.numero_registro=numero_registro
        self.año_produccion=año_produccion
        self.pasajero=pasajero
        self.peso=peso

class serializacion(json.JSONEncoder):
    def default(self, clase):
        if isinstance(clase, vehiculo):
            return clase.__dict__
        return super().default(clase)
    
class deserializacion(json.JSONDecoder):
    def __init__(self):
        json.JSONDecoder.__init__(self, object_hook=self.decodificacion)

    def decodificacion(self, clase):
        return vehiculo(**clase)
    
print("Que puedo hacer por ti?")
print("1-Producir una cadena json describiendo un vehiculo")
print("2-Decodificar una cadena json hacia los datos de un  vehiculo?")

boleano = True

try:
    while boleano:
        elegir = input("Tu eleccion: ")
        if elegir == "q":
            break
        elif len(str(elegir)) > 1 or elegir not in ["1","2"]:
            print("Solo numeros 1 y 2")
        elif elegir == "1":
            print("Crea un vehiculo de cadena json")
            nr = input("Numero de registro (cadena): ")
            ap = int(input("Año de produccion (numero): "))
            p = input("Pasajero (booleano): ")
            peso = float(input("Peso(flotante): "))
            if type(nr) != str:
                print("Numero de registro invalido")
            elif type(ap) != int:
                print("Año de produccion invalido")
            elif type(p) != str:
                print("Pasajero incorrecto")
            elif type(peso) != float:
                print("Peso invalido")
            else:
                v = vehiculo(nr, ap, p, peso)
                s = json.dumps(v, cls = serializacion)
                print("Cadena serializada: ", s)
                print("Hecho")
        elif elegir == "2":
            try:
                d = json.loads(s, cls = deserializacion)
                print("Cadena deserializada: ", d.__dict__)
                print("Hecho")
            except NameError:
                print("Primero crea un json")
except ValueError as v:
    print("Solo numeros 1 y 2")
