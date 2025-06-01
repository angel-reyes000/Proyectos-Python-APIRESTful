import requests

server = "http://localhost:3000/cars/"
respuesta = requests.get(server)

tres = {
    "id": "3",
    "brand": "Aston Martin",
    "model": "Rapide",
    "production_year": 2010,
    "convertible": True
  }

nueve = {
    "id": "9",
    "brand": "Nissan",
    "model": "Tsuru",
    "production_year": 2000,
    "convertible": False
  }

try:
    postear = requests.post(server, headers={"content-type":"application-json"}, json=nueve)
    print(postear.status_code)
    respuesta = requests.get(server, headers={"connection":"close"})
    print(respuesta.headers)
    for q in respuesta.json():
        print(q)
except requests.ConnectionError as err:
    print(f"Error de coneccion: {err}")
except requests.RequestException:
    print("Algo salio mal")
