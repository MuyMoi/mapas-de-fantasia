from funciones import *
from Protagonista import *

# Crear los lugares que componen el mapa

aldea = Ubicacion("Aldea principal",
  "")
lago = Ubicacion("Lago sagrado",
  "Dicen que si tocas el agua de este lago moriras de formas " +
  "insospechables. Cuidado!",
  direccionHuida=IZQ)
campamento = Ubicacion("Campamento", 
  "")
mazmorra = Ubicacion("Mazmorra",
  "",
  direccionHuida=ARR)
castillo = Ubicacion("Castillo antiguo",
  "",
  direccionHuida=ABJ)
bosque = Ubicacion("Bosque encantado",
  "",
  direccionHuida=DER)


# Crear las rutas que conectan los lugares

ruta1 = Ubicacion("Ruta 1",
  "")
ruta2 = Ubicacion("Ruta 2",
  "", direccionHuida=IZQ)
ruta3 = Ubicacion("Ruta 3",
  "")
ruta4 = Ubicacion("Ruta 4",
  "")
ruta5 = Ubicacion("Ruta 5",
  "", direccionHuida=ABJ)
ruta6 = Ubicacion("Ruta 6",
  "")


# Establecer sus conexiones bidireccionales
# Por ejemplo: partiendo de la aldea, ABAJO, esta la ruta 1

aldea.agregarconex(ABJ, ruta1)
ruta1.agregarconex(DER, lago)
aldea.agregarconex(DER, ruta2)
ruta2.agregarconex(DER, campamento)
campamento.agregarconex(DER, ruta3)
ruta3.agregarconex(DER, ruta4)
ruta4.agregarconex(ABJ, mazmorra)
ruta4.agregarconex(ARR, castillo)
castillo.agregarconex(IZQ, ruta6)
ruta6.agregarconex(IZQ, bosque)
ruta6.agregarconex(ABJ, ruta5)
ruta5.agregarconex(ABJ, campamento)


# Añadir personajes

sabio = Benevolente("Sabio Anciano", 0)
aldea.CpP.enqueue(sabio)

exploradora = Benevolente("Exploradora Errante", 3)
campamento.CpP.enqueue(exploradora)




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
  limpiarPantalla()

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
P.ubicActual = aldea


# Añadir discursos

#SABIO

sabio.discursos.insertarFinal(
'''Ah… así que al fin has despertado, viajero.
Primero que nada, dime: como te llamas?''')
P.discursos[0].insertarFinal(
f'''Me llamo {P.nombre}
''')
sabio.discursos.insertarFinal(
f'''Encantado de conocerte, {P.nombre}. No es casualidad que
tus pasos comiencen aquí. Este mundo, aunque pequeño, arde
con antiguos conflictos que pocos recuerdan.
El Bosque Encantado susurra advertencias, el Castillo Antiguo
guarda secretos que aún respiran, y el Lago Sagrado... ya no es
tan puro como solía ser. Muchos han partido por esas rutas y
pocos han regresado con respuestas. Tú tienes en la mirada algo
distinto… una voluntad que no se rinde con facilidad. Si deseas
explorar, hazlo con prudencia. Cada sendero transforma a quien
lo recorre. No busques solo tesoros: busca la verdad de este mundo.
''')
P.discursos[0].insertarFinal(
f'''No sé por qué estoy aquí, pero siento que debo avanzar. Algo
me llama desde más allá de la aldea. Gracias por advertirme, señor.
Prometo no ignorar sus palabras. Volveré con respuestas… o no
volveré en absoluto.
''')

#EXPLORADORA ERRANTE:

exploradora.discursos.insertarFinal(
'''No esperaba ver a alguien nuevo por estos caminos. Normalmente
solo pasan comerciantes desesperados o guerreros que no regresan.
Yo vigilo este campamento para quienes se atreven a cruzar el
corazón del mapa. Desde aquí se siente cómo las rutas se tensan,
como si el mundo respirara antes de una tormenta. La ruta 3 es
relativamente segura… si sabes escuchar. La ruta 5, en cambio,
está manchada por algo que no pertenece a este tiempo. He visto
sombras moverse sin cuerpo. Si sigues adelante, guarda provisiones,
guarda fuerzas… y guarda recuerdos. A veces eso es lo único que
regresa contigo.
''')
P.discursos[3].insertarFinal(
'''No pensé encontrar a alguien tan lejos de la aldea. Gracias por
la hospitalidad. Tu advertencia no caerá en oídos sordos. Seguiré
adelante, pero lo haré con cautela. Quizás, cuando todo termine,
este campamento ya no sea solo un lugar de paso.
''')

# Parte principal

while True:
# Se limpia la pantalla y se muestra la ubicacion actual

  limpiarPantalla()
  print("\n-------------------------------------------------")
  print(f"Estas actualmente en {P.ubicActual.nombre}")
  print(P.ubicActual.descrip)


# Si hay enemigos pendientes por vencer en la ubicacion actual,
# se informa y se dan opciones

  if P.ubicActual.hayEnemigos():
    print("Un momento! Parece que hay amenazas...")
    enemigo = P.ubicActual.CeP.peek()
    print(f"Aparecio {enemigo.nombre}. Que deseas hacer?")
    print("huir  : Huir y regresar a la ruta anterior")
    print("luchar: Arriesgarte y enfrentar a la amenaza")
    if opc == "huir":
      P.huir()
    elif opc == "luchar":
      print("aun no hay codigo para luchar")

# Aqui se informa al jugador si existe algun personaje
# con quien haya que hablar primero para poder continuar

  elif P.ubicActual.hayPersonajes():
    print("Hay un personaje en esta ubicacion que desa hablar contigo\n")
    per = P.ubicActual.CpP.dequeue()
    disc_per = per.discursos
    disc_prot = P.discursos[per.id]
    
    while disc_per.actual is not None:
      print(f"{per.nombre}: {disc_per.actual.dato}\n")
      print(f"{P.nombre}: {disc_prot.actual.dato}")
      disc_per.avanzar_ptr()
      disc_prot.avanzar_ptr()

    disc_per.reiniciar_ptr()
    disc_prot.reiniciar_ptr()


# Si no hay nada pendiente, se ofrecen las siguientes opciones

  else:
    print("Que deseas hacer?")
    print("inventario: Ver el inventario de objetos")
    print("stats     : Ver tus estadisticas")
    print("mover     : Moverte de mapa")
    #print("hablar    : Hablar con un personaje")  #########
    print("salir     : Salir del juego")
    opc = input("--> ")

    limpiarPantalla()

# Mostrar el inventario del protagonista

    if opc == "inventario":
      print("    INVENTARIO")
      P.verInventario()

# Mostrar las estadisticas

    elif opc == "stats":
      print(f"    ESTADISTICAS DE {P.nombre}")
      P.verEstadisticas()

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
      """    elif opc == "hablar":
      if P.ubicActual.Lp[0] is None and P.ubicActual.Lp[0] is None:
        print("No hay nadie en esta ubicacion")
      else:
        print("Escribe el numero del personaje con quien deseas hablar:")
        for i in range(0, 2):
          if P.ubicActual.Lp[i] is not None:
            print(f"{i+1}: {P.ubicActual.Lp[i].nombre}")
      """



# Salir del juego

    elif opc == "salir":
      print("Saliendo")
      exit()


# Opcion no valida
    else:
      print("Opcion no valida. Asegurate de escribir los comandos en minuscula")

  print("\nPresiona ENTER para continuar")
  input()
