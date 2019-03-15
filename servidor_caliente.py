
#!/usr/bin/env python

import socket
from random import randint

serversocket    =   socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Creamos socket

serversocket.bind(('10.108.33.32', 8080)) #Mantenemos en esucucha el puerto (8000)

serversocket.listen(1) #Mantenemos en escucha el servidor

numero=randint(0,99) #Elige numero al azar
clientsocket, clientaddress = serversocket.accept()  #Aceptamos la conexión
print ('Conexion desde: ', clientaddress)  #Imprimir la IP del clientsocket
#Entra en el bucle mientras se mantenga la conexión
try:
    while True:
            data = clientsocket.recv(1024).decode() #Recibimos los datos del cliente
            if numero == int(data):
                reply = 'Felicidades, has acertado!!!'
                clientsocket.sendall(reply.encode())
                serversocket.listen(1) #Mantenemos en escucha el servidor #Elige numero al azar
                clientsocket, clientaddress = serversocket.accept()  #Aceptamos la conexión
                print ('Conexion desde: ', clientaddress)
            elif numero-10<int(data)<numero+10:
                reply = 'caliente, caliente'
                clientsocket.sendall(reply.encode())
            elif numero-10 > int(data):
                reply = 'frio, por encima'
                clientsocket.sendall(reply.encode())
            elif numero-10 < int(data):
                reply ='frio, por debajo'
                clientsocket.sendall(reply.encode())
    clientsocket.close()
except ValueError:
        reply = 'Por favor introduzca un número del 0 al 99'
        clientsocket.sendall(reply.encode())
except KeyboardInterrupt:
        print()
        print("Ejecución interrumpida por el usuario.")
        print("El programa ha finalizado.")
        clientsocket.close() #Cierra el socket
except BrokenPipeError:
        print()
        print("Ejecución interrumpida por el usuario.")
        print("El programa ha finalizado.")
        clientsocket.close() #Cierra el socket
