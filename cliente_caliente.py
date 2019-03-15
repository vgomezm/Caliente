#!/usr/bin/env python

import socket


clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #Crear el socket

clientsocket.connect(('10.108.33.32',8080)) #Se conecta al servidor (IP,puerto)

#Entra en el bucle si está conectado
try:
    while 1:
            data = str.encode(input('>')) #Escribimos mensaje
            clientsocket.send(data)  #Se envía al servidor
            if not data or (data==str.encode('salir')): break  #Si no hay mensaje (no envía)
            newdata = clientsocket.recv(1024).decode()  #Recibe la respuesta del servidor
            print ('servidor: %s' % newdata)
            if newdata == 'Felicidades, has acertado!!!': break
    clientsocket.close()  #Cierra el socket

except KeyboardInterrupt:
        print()
        print("Ejecución interrumpida por el usuario.")
        print("El programa ha finalizado.")
        clientsocket.close()
