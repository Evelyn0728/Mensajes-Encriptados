# Mensajes Encriptados

Proyecto de **encriptación y desencriptación de mensajes** utilizando **álgebra lineal (matrices)** en Python.  
El programa convierte un mensaje de texto en números, lo multiplica por una matriz aleatoria y genera una "llave" para poder recuperar el mensaje original.

---

## Descripción

Este proyecto implementa un sistema de cifrado simple basado en matrices:

1. Se convierte cada letra del mensaje a un número (según un abecedario predefinido).
2. Se genera una **matriz aleatoria** del mismo tamaño que el mensaje.
3. Se multiplica la matriz por el vector del mensaje → **mensaje encriptado**.
4. Se guarda una **llave** (`.npz`) con la matriz y el mensaje encriptado.
5. Para desencriptar, se usa la **matriz inversa** para recuperar el mensaje original.

---

## Tecnologías utilizadas

- **Python 3.x**
- **NumPy** (operaciones con matrices)
- **random** (generación de la matriz aleatoria)
- **os / sys** (manejo de rutas para guardar la llave)

---

## Estructura del proyecto

MensajesEncriptados/
│
├── MensajesEncriptados.py # Código fuente
├── MensajesEncriptados.exe # Ejecutable (Windows)
├── README.md # Este archivo
└── .gitignore # Archivos ignorados por Git

---

## Instalación

### Opción 1: Ejecutar el `.exe` (Windows)
Solo haz doble clic en `MensajesEncriptados.exe`. No requiere instalar nada.

### Opción 2: Ejecutar desde el código fuente

1. Clona el repositorio:
   ```bash
   git clone https://github.com/TuUsuario/MensajesEncriptados.git
   cd MensajesEncriptados
2. Instala la dependencia:
   pip install numpy
3. Ejecuta el programa:
   python MensajesEncriptados.py

---

##Uso

Al ejecutar el programa verás el siguiente menú:
Que desea realizar?

1. Mandar mensaje encriptado

2. Desencriptar mensaje

Opción 1: Encriptar un mensaje
Selecciona 1.

Escribe el mensaje que quieres encriptar.
El programa genera automáticamente una llave (Llave.npz) que contiene:
El mensaje encriptado (matriz).
La matriz aleatoria usada.
Comparte el archivo Llave.npz con el destinatario.

Opción 2: Desencriptar un mensaje
Selecciona 2.

Ingresa el nombre del archivo llave (ej: Llave.npz).
El programa mostrará:
La matriz encriptada.
La matriz aleatoria.
La matriz inversa.
El mensaje original desencriptado.

---

##¿Cómo funciona matemáticamente?
Encriptación:
MensajeEncriptado = MatrizRandom × MensajeVector
Desencriptación:
MensajeOriginal = MatrizRandom⁻¹ × MensajeEncriptado
Donde MatrizRandom⁻¹ es la inversa de la matriz aleatoria (calculada con numpy.linalg.inv).

###Nota: Este sistema es una implementación educativa. Para cifrado real se recomiendan algoritmos como AES o RSA.

---

##Ejemplo de uso
Mensaje original:
hola mundo
Mensaje encriptado (matriz):
[[ 45.  78.  12. ...]]
Mensaje desencriptado:
hola mundo

---

Autores:
Aaron Hernandez Rendón
Evelyn Ramirez Aguilar
Ricardo Sánchez Ponce

GitHub:
AaronRnx
Evelyn0728
RicardoSanchezPonce 

---

##Licencia
Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.