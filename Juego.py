from Mapa import *
from os import system
from funciones import *
from Protagonista import *

mapa = Mapa()

while True:
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
  print("Escribe el comando en letras minusculas:")
  opc = input("-->")
  system("clear")

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
print(f'''\nHola {nombre}! Que gusto tenerte aqui :)
A partir de ahora comienza tu nueva y divertida aventura\n''')
print("Presiona ENTER para continuar")
input()

P = Protagonista(nombre)

while True:
  system("clear")
  print("\n-------------------------------------------------")
  print(f"Estas actualmente en {mapa.actual.nombre}")
  print(mapa.actual.descrip)

  print("Que deseas hacer?")
  print("inventario: Ver el inventario de objetos")
  print("mover     : Moverte de mapa")
  print("hablar    : Hablar con un personaje")
  print("luchar    : Luchar contra el siguiente enemigo")
  print("salir     : Salir del juego")
  opc = input("--> ")

  system("clear")

  if opc == "inventario":
    print("    INVENTARIO")
    P.verInventario()

  elif opc == "mover":
    arriba = mapa.actual.conex[ARR]
    abajo = mapa.actual.conex[ABJ]
    izquier = mapa.actual.conex[IZQ]
    derecha = mapa.actual.conex[DER]

    print("    Hacia donde te deseas mover?")
    if arriba is not None: print(f" - Arriba:    {arriba.nombre}")
    if abajo is not None:  print(f" - Abajo:     {abajo.nombre}")
    if izquier is not None: print(f" - Izquierda: {izquier.nombre}")
    if derecha is not None: print(f" - Derecha:   {derecha.nombre}")
    print("\nEscribe la direccion en letras minusculas:")
    string = input("--> ")

    direc = obtenerNumDireccion(string)
    if direc == -1:
      print("Direccion no valida")
      continue
    
    if mapa.actual.estaBloqueado(direc):
      print("No puedes avanzar en esta direccion. Tal vez te falta " + 
        "algun objetivo por cumplir")
    elif mapa.actual.conex[direc] is not None:
      mapa.mover(direc)
    else:
      print("No hay nada en esa direccion")

  elif opc == "hablar":
    personaje = mapa.actual.pP.dequeue()
    if personaje != None:
      personaje.hablar()

  elif opc == "luchar":
    pass

  elif opc == "salir":
    print("Saliendo")
    exit()

  else:
    print("Opcion no valida. Asegurate de escribir los comandos en minuscula")

  print("Presiona ENTER para continuar")
  input()