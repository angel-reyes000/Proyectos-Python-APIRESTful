import socket
import sys
import time

class ErrorRespuesta(Exception):
    pass

if len(sys.argv) not in [2, 3]:
    try:    
        server = input("Servidor: ")
        tiempo_inicio = time.time()

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((server, 80))
        sock.send(b"HEAD /HTTP/1.1\r\nHost:"+bytes(server, "utf-8")+b"\r\nConnection: Close\r\n")
        respuesta = sock.recv(1000)
        sock.shutdown(socket.SHUT_RDWR)
        sock.close()
        sys.argv.append(respuesta)

        tiempo_final = time.time()
        tiempo_total = int(tiempo_final - tiempo_inicio)
    except:
        if len(sys.argv) == 1:
            raise ErrorRespuesta("1")
        elif sys.argv[1] == [x for x in range(1, 65535)]:
            raise ErrorRespuesta("2")
        elif tiempo_total > 3:
            raise ErrorRespuesta("3")
        else:
            raise ErrorRespuesta("Error")
    print(sys.argv)
    print(tiempo_total)

else:
    raise ErrorRespuesta("Error en la conexion")