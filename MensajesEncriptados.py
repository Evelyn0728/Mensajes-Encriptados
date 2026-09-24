import random
import numpy as np
import os
import sys
np.set_printoptions(linewidth=200, precision=2, suppress=True)

def EncriptacionSimple(mensaje):
    mensaje = mensaje.lower()
    abecedario = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    MensajeEncriptadoSimple = []
    for i in range(len(mensaje)):
        for j in range(len(abecedario)):
            if mensaje[i] == abecedario[j]:
                MensajeEncriptadoSimple.append(j)
          
        
    return MensajeEncriptadoSimple



def EncriptacionMatricial(MensajeEncriptadoSimple, MatrizRandom):
    MensajeEncriptadoSimple = np.array(MensajeEncriptadoSimple)
    MatrizRandom = np.array(MatrizRandom)
    matrizResultante = MatrizRandom @ MensajeEncriptadoSimple

    return matrizResultante

def DesencriptacionSimple(arregloEncriptado):
    abecedario = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    mensaje = []
    for i in range(len(arregloEncriptado)):
        x = int(arregloEncriptado[i] + 0.5)
        mensaje.append(abecedario[x])
    mensajeDesencriptado = "".join(mensaje)
    return mensajeDesencriptado

def DesencriptacionMatricial(MensajeEncriptadoMatricial, MatrizRandom):
    MensajeEncriptadoMatricial = np.array(MensajeEncriptadoMatricial)
    MatrizRandom = np.array(MatrizRandom)
    MensajeEncriptadoMatricialInv = np.linalg.inv(MatrizRandom)
    MensajeDesencriptadoMatricial = DesencriptacionSimple((MensajeEncriptadoMatricialInv @ MensajeEncriptadoMatricial))
    
    return MensajeDesencriptadoMatricial, MensajeEncriptadoMatricialInv

def CrearLlaves(MensajeEncriptadoMatricial, MatrizRandom):
    ruta = os.path.join(os.path.dirname(sys.executable), "Llave")
    np.savez(ruta, MensajeEncriptadoMatricial, MatrizRandom)

def LeerLlave(NombreLlave):
    ruta = os.path.join(os.path.dirname(sys.executable), NombreLlave)
    datos = np.load(ruta)
    return datos ["arr_0"], datos ["arr_1"]







while True:
    x = input ("Que desea realizar?\n\n1. Mandar mensaje encriptado\n\n2. Desencriptar mensaje\n\n")
    if x == '1':
        mensaje = input ("\nEscriba su mensaje: ")
        columnas = len(mensaje)
        filas = columnas
        MatrizRandom = np.array([[random.randint(1, 10) for _ in range(columnas)] for _ in range(filas)])
        MensajeEncriptadoSimple = EncriptacionSimple(mensaje)
        MensajeEncriptadoMatricial = EncriptacionMatricial(MensajeEncriptadoSimple, MatrizRandom)
        CrearLlaves(MensajeEncriptadoMatricial, MatrizRandom)
        print ("Su mensaje ha sido encriptado con exito\n\n")
        respuesta = input ("\nDesea realizar otra operacion? s/n")
        if respuesta == 'n':
            break    
    if x == '2':
        NombreLlave = input ("\nIngrese el nombre de la llave con su extension: ")
        MensajeEncriptadoMatricial, MatrizRandom = LeerLlave(NombreLlave)
        MensajeDesencriptadoMatricial, MensajeDesencriptadoMatricialInv = DesencriptacionMatricial(MensajeEncriptadoMatricial, MatrizRandom)
        print ("\nMatriz Encriptada\n ")
        print (MensajeEncriptadoMatricial)
        print ("\nMatriz Random\n ")
        print (MatrizRandom)
        print ("\nMatriz Random Inversa\n ")
        print (MensajeDesencriptadoMatricialInv)
        print ("\nSu mensaje es: "+MensajeDesencriptadoMatricial)
        respuesta = input ("\nDesea realizar otra operacion?\n s/n\n")
        if respuesta == 'n':
            break    

