
from os import system
from funciones import *
from Protagonista import *


''' En este archivo se muestra la logica principal del juego,
desde la parte introductoria hasta la toma de decisiones
con respecto a enemigos, personajes y ubicaciones'''


# Introduccion

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
  system("cls")

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



# Pedir el nombre para iniciar el protagonista

print("\nEscribe un nombre para tu personaje:")
nombre = input("-->")
print(f'''\nHola {nombre}! Que gusto tenerte aqui :)
A partir de ahora comienza tu nueva y divertida aventura\n''')
print("Presiona ENTER para continuar")
input()

P = Protagonista(nombre)



# Parte principal

while True:
# Se limpia la pantalla y se muestra la ubicacion actual

  system("cls")
  print("\n-------------------------------------------------")
  print(f"Estas actualmente en {P.ubicActual.nombre}")
  print(P.ubicActual.descrip)


# Aqui se informa al jugador si existe algun personaje
# con quien haya que hablar primero para poder continuar

  if P.ubicActual.hayPersonajes():
    print("Hay un personaje en esta ubicacion que desa hablar contigo\n")
    personaje = P.ubicActual.CpP.dequeue()
    print(f"       {personaje.nombre}:")
    personaje.hablar()


# Si hay enemigos pendientes por vencer en la ubicacion actual,
# se informa y se dan opciones

  elif P.ubicActual.hayEnemigos():
    print("Un momento! Parece que hay amenazas...")
    enemigo = P.ubicActual.CeP.peek()
    print(f"Aparecio {enemigo.nombre}. Que deseas hacer?")
    print("huir  : Huir y regresar a la ruta anterior")
    print("luchar: Arriesgarte y enfrentar a la amenaza")
    if opc == "huir":
      P.huir()
    elif opc == "luchar":
      print("aun no hay codigo para luchar")



# Si no hay nada pendiente, se ofrecen las siguientes opciones

  else:
    print("Que deseas hacer?")
    print("inventario: Ver el inventario de objetos")
    print("mover     : Moverte de mapa")
    print("hablar    : Hablar con un personaje")
    print("salir     : Salir del juego")
    opc = input("--> ")

    system("cls")

# Mostrar el inventario del protagonista

    if opc == "inventario":
      print("    INVENTARIO")
      P.verInventario()


# Mover al protagonista de ubicacion

    elif opc == "mover":
      arriba = P.ubicActual.conex[ARR]
      abajo = P.ubicActual.conex[ABJ]
      izquier = P.ubicActual.conex[IZQ]
      derecha = P.ubicActual.conex[DER]

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
      
      if P.ubicActual.conex[direc] is not None:
        P.mover(direc)
      else:
        print("No hay nada en esa direccion")

# Hablar con alguno de los personajes benevolentes que aparecieron
# al llegar a la ubicacion
    elif opc == "hablar":
      pass


# Salir del juego

    elif opc == "salir":
      print("Saliendo")
      exit()


# Opcion no valida
    else:
      print("Opcion no valida. Asegurate de escribir los comandos en minuscula")

  print("\nPresiona ENTER para continuar")
  input()