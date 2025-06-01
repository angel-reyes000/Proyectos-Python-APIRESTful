import xml.etree.ElementTree

temas = ["Company", "Last", "Change", "Min", "Max"]
espacios = [50, 20, 20, 20, 20]

def mostrar_temas():
    for n, w in zip(temas, espacios):
        print(n.ljust(w), end="")
    print()

    for q in range(125):
        print("-", end="")
    print()

def mostrar_info():
    for cuotas in root:
        print(cuotas.text.ljust(50), end="")
        for datos in cuotas.attrib.values():
            print(datos.ljust(20), end="")
        print()

def mostrar_todo():
    mostrar_temas()
    mostrar_info()

try:
    leer = xml.etree.ElementTree.parse("C:\\Users\\Luis Reyes\\Downloads\\nyse.xml")
    root = leer.getroot()
except xml.etree.ElementTree.ParseError:
    print("Error al leer el archivo, mal formado o mal escrito")
except FileNotFoundError:
    print("Archivo no encontrado, verificar ruta")
else:
    mostrar_todo()


