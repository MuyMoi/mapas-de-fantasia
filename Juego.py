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
  "El aire es frío y oyes ruidos entre los árboles",
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
aldea.benev_pend.enqueue(sabio)

espiritu = Enemigo("Espiritu del lago", 1)
lago.enem_pend.enqueue(espiritu)

# = Enemigo("", 2)
#ruta2.enem_pend.enqueue()

exploradora = Benevolente("Exploradora Errante", 3)
campamento.benev_pend.enqueue(exploradora)

''' = Enemigo("", 4)
ruta5.enem_pend.enqueue()

 = Benevolente("", 5)
ruta3.benev_pend.enqueue()

 = Enemigo("", 6)
mazmorra.enem_pend.enqueue()

 = Enemigo("", 7)
castillo.enem_pend.enqueue()

= Benevolente("", 8)
castillo.benev_pend.enqueue()

= Benevolente("", 9)
ruta6.benev_pend.enqueue()

 = Enemigo("", 10)
bosque.enem_pend.enqueue()

= Benevolente("", 11)
bosque.benev_pend.enqueue()'''


# Introduccion

limpiarPantalla()
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

#SABIO (id=0)

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

# ESPIRITU DEL LAGO (id=1)

espiritu.discursos.insertarFinal(
'''Durante siglos fui guardián de aguas puras, reflejo del cielo y
alivio de los vivos… hasta que los hombres arrojaron su ambición
a mis entrañas. Ahora solo queda eco, veneno y lamentos. Tú no eres
distinto a los demás. Vienes buscando poder, respuestas o gloria,
pero todos terminan alimentando la oscuridad. Cada paso que das sobre
estas orillas despierta los recuerdos de quienes se ahogaron en sus
propios deseos. Si avanzas, tu reflejo será lo último que veas antes
de perderte conmigo en el fondo.
''')
P.discursos[1].insertarFinal(
'''No busco corromper lo que queda de este lugar. Pero tampoco
retrocederé. Si tu dolor es lo que te convirtió en esto, entonces te
liberaré… aunque tenga que enfrentar tu furia. El lago puede haber
sido manchado, pero aún puede ser salvado.
''')

#EXPLORADORA ERRANTE: (id=3)

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
  print(f"Estas actualmente en {P.ubicActual.nombre}")
  print(P.ubicActual.descrip)
  print("\n-------------------------------------------------\n")

# Si hay enemigos pendientes por vencer en la ubicacion actual,
# se informa y se dan opciones

  if P.ubicActual.hayEnemigos():
    print("\nUn momento! Parece que hay amenazas...")
    enemigo = P.ubicActual.enem_pend.peek()
    print(f"Aparecio {enemigo.nombre}. ")
    print("------------------------------------------- ")
    verDiscurso(P, enemigo)

    print("------------------------------------")
    print("Que deseas hacer?")
    print(" huir | luchar")
    opc = input("-->")
    if opc == "huir":
      print(f"Has huido a la ubicacion {P.ubicActual.verUbicacionHuida()}")
      P.huir()
    elif opc == "luchar":
      while True:
        print("\nElige una accion:")
        print(" atacar | pocion")
        opc2 = input("-->")

        if opc2 == "atacar":
          print("Has hecho {puntos} puntos de daño")
          break
        elif opc2 == "pocion":
          print("Has recuperado {puntos} puntos de salud")
        else:
          print("Opcion no valida")

        print("Has vencido al enemigo")
    else:
      print("No has elegido una opcion correcta. Has huido!")
      P.huir()

# Aqui se informa al jugador si existe algun personaje benevolente
# con quien haya que hablar primero para poder continuar

  elif P.ubicActual.hayBenevolentes():
    print("Hay un personaje en esta ubicacion que desa hablar contigo\n")
    print("-----------------------------------------------------------")
    personaje = P.ubicActual.benev_pend.dequeue()
    verDiscurso(P, personaje)


# Si no hay nada pendiente, se ofrecen las siguientes opciones

  else:
    arriba = P.ubicActual.conex[ARR]
    abajo = P.ubicActual.conex[ABJ]
    izquier = P.ubicActual.conex[IZQ]
    derecha = P.ubicActual.conex[DER]

    print("Que deseas hacer?")
    print("inventario: Ver el inventario de objetos")
    print("stats     : Ver tus estadisticas")
    print()
    if arriba  is not None: print(f"arriba    : Moverte a {arriba.nombre}")
    if abajo   is not None: print(f"abajo     : Moverte a {abajo.nombre}")
    if izquier is not None: print(f"izquierda : Moverte a {izquier.nombre}")
    if derecha is not None: print(f"derecha   : Moverte a {derecha.nombre}")
    print()
    print("salir     : Salir del juego\n")
    opc = input("--> ")

# Mostrar el inventario del protagonista

    if opc == "inventario":
      print("    INVENTARIO")
      P.verInventario()

# Mostrar las estadisticas

    elif opc == "stats":
      print(f"    ESTADISTICAS DE {P.nombre}")
      P.verEstadisticas()

# Mover al protagonista de ubicacion

    elif opc == "arriba" or opc == "abajo" or opc == "derecha" or opc == "izquierda":
      direc = obtenerNumDireccion(opc)
      
      if P.ubicActual.conex[direc] is not None:
        P.mover(direc)
      else:
        print("No hay nada en esa direccion")

# Salir del juego

    elif opc == "salir":
      print("Saliendo")
      exit()


# Opcion no valida
    else:
      print("Opcion no valida. Asegurate de escribir los comandos en minuscula")

  print("\nPresiona ENTER para continuar")
  input()
