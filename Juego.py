from Mapa import *
from os import system
from funciones import *
from Protagonista import *

mapa = Mapa()

print('''
----------------------------------------
     EXPLORADOR DE MAPAS DE FANTASIA
----------------------------------------

Bienvenido, aventurero.
Tu misión es descubrir todos los rincones de este mundo
y enfrentarte a los peligros que habitan en él.

Comandos disponibles:
- iniciar
- ayuda
- salir
''')

while True:
  print("Escribe el comando en letras minusculas:")
  opc = input("-->")

  if opc == "ayuda":
    verAyuda()
    break
  elif opc == "iniciar":
    print("OK, comencemos.")
    break
  elif opc == "salir":
    print("Saliendo...")
    exit()
  else:
    print("Opcion no valida. Escribe otra vez el comando.")

print("\nEscribe un nombre para tu personaje:")
nombre = input("-->")
print(f'''\nHola {nombre}!! Que gusto tenerte aqui! :)
A partir de ahora comienza tu nueva y divertida
aventura, explorador\n''')
print("Presiona ENTER para continuar")
input()

P = Protagonista(nombre)

while True:
  print(f"\nEstas actualmente en {mapa.actual.nombre}")
  print(mapa.actual.descrip)

  arriba = mapa.actual.conex[ARR]
  abajo = mapa.actual.conex[ABJ]
  izquier = mapa.actual.conex[IZQ]
  derecha = mapa.actual.conex[DER]

  print("\nHacia donde te deseas mover?\n")
  if arriba is not None: print(f" - Arriba:    {arriba.nombre}")
  if abajo is not None:  print(f" - Abajo:     {abajo.nombre}")
  if izquier is not None: print(f" - Izquierda: {izquier.nombre}")
  if derecha is not None: print(f" - Derecha:   {derecha.nombre}")
  print("\nEscribe la direccion en letras minusculas:")
  string = input("--> ")
  
  system("clear")
  direc = obtenerNumDireccion(string)
  if direc == -1:
    print("Direccion no valida")
    continue
  
  if mapa.actual.conex[direc] is not None:
    mapa.mover(direc)
  else:
    print("No hay nada en esa direccion")