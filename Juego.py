from funciones import *
from Protagonista import *
from random import randint

# Crear los lugares que componen el mapa

aldea = Ubicacion("Aldea principal",
  "Un pequeño poblado rodeado de colinas y bosques. Ultimo " +
  "refugio de calma antes de adentrarse en un mundo corrompido")

lago = Ubicacion("Lago sagrado",
  "Antigua fuente sagrada cuyas aguas ahora reflejan una " +
  "corrupción silenciosa y profunda.",
  direccionHuida=IZQ)

campamento = Ubicacion("Campamento", 
  "Puesto de descanso para viajeros, donde confluyen " +
  "advertencias, rumores y las últimas hogueras seguras del mapa")

mazmorra = Ubicacion("Mazmorra",
  "Prisión subterránea de piedra y lamentos, construida para " +
  "encerrar horrores que nunca debieron liberarse",
  direccionHuida=ARR)

castillo = Ubicacion("Castillo antiguo",
  "Fortaleza en ruinas atrapada en el tiempo, gobernada por " +
  "ecos de un reino que se niega a desaparecer",
  direccionHuida=ABJ)

bosque = Ubicacion("Bosque encantado",
  "El aire es frío y oyes ruidos entre los árboles. Cada árbol " +
  "parece observar al viajero",
  direccionHuida=DER)


# Crear las rutas que conectan los lugares

ruta1 = Ubicacion("Ruta 1",
  "Camino inicial entre praderas suaves, donde el peligro aún " +
  "parece lejano y la aventura apenas despierta")
ruta2 = Ubicacion("Ruta 2",
  "Sendero rocoso dominado por bandidos, primer filtro entre " +
  "la inocencia de la aldea y la crudeza del viaje",
  direccionHuida=IZQ)
ruta3 = Ubicacion("Ruta 3",
  "Camino tranquilo en apariencia, donde el viento transporta " +
  "ecos de todo lo que ocurre en las regiones cercanas")
ruta4 = Ubicacion("Ruta 4",
  "Sendero estrecho entre rocas y niebla, paso olvidado que " +
  "conecta regiones sin la protección de rutas seguras")
ruta5 = Ubicacion("Ruta 5",
  "Paso oscuro vigilado por sombras antiguas, conexión directa " +
  "entre las ruinas del castillo y las tierras olvidadas",
  direccionHuida=ABJ)
ruta6 = Ubicacion("Ruta 6",
  "Ruta elevada y solitaria, donde el horizonte anuncia un punto " +
  "de no retorno para el viajero")


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

# Objetos clave
amuleto = ObjetoClave("Amuleto del Agua")
daga = ObjetoClave("Daga oxidada")
llaveEncierro = ObjetoClave("Llave del Encierro Eterno")
llaveAntigua = ObjetoClave("Llave antigua")
corona = ObjetoClave("Corona del Ocaso")
colmillo = ObjetoClave("Colmillo mágico")

# Añadir personajes

sabio = Benevolente("Sabio Anciano", 0)
aldea.benev_pend.enqueue(sabio)

espiritu = Enemigo("Espiritu del lago", 1, 100, 10, 50, 10)
espiritu.objetoRecompensa = amuleto
lago.enem_pend.enqueue(espiritu)

saqueador = Enemigo("Saqueador del sendero", 2, 110, 15, 70, 30)
saqueador.objetoRecompensa = daga
saqueador.objetoRequerido = amuleto
ruta2.enem_pend.enqueue(saqueador)

exploradora = Benevolente("Exploradora Errante", 3)
campamento.benev_pend.enqueue(exploradora)

vigiasombras = Enemigo("Vigia de las Sombras", 4, 150, 20, 90, 15)
vigiasombras.objetoRecompensa = llaveAntigua
vigiasombras.objetoRequerido = llaveEncierro
ruta5.enem_pend.enqueue(vigiasombras)

curandera = Benevolente("Curandera del Camino", 5)
ruta3.benev_pend.enqueue(curandera)

carcelero = Enemigo("Carcelero de las Profundidades", 6, 100, 15, 80, 10)
carcelero.objetoRecompensa = llaveEncierro
mazmorra.enem_pend.enqueue(carcelero)

rey = Enemigo("Rey del Ocaso", 7, 120, 18, 85, 50)
rey.objetoRecompensa = corona
rey.objetoRequerido = llaveAntigua
castillo.enem_pend.enqueue(rey)

guardian = Benevolente("Guardian Liberado", 8)
castillo.benev_pend.enqueue(guardian)

vigiahoriz = Benevolente("Vigia del Horizonte", 9)
ruta6.benev_pend.enqueue(vigiahoriz)

lobo = Enemigo("Lobo Sombrio", 10, 200, 20, 150, 20)
lobo.objetoRecompensa = colmillo
lobo.objetoRequerido = corona
bosque.enem_pend.enqueue(lobo)


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
    limpiarPantalla()
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
P.pociones = 3

# Añadir discursos

#SABIO (id=0)

sabio.discursos.insertarFinal(
'''Ah… así que al fin has despertado, viajero.
Primero que nada, dime: como te llamas?
''')
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

# SAQUEADOR (2)

saqueador.discursos.insertarFinal(
'''Je… otro viajero más saliendo de la Aldea creyéndose héroe. Todos
caminan con la espalda recta cuando aún no saben cuánto pesa el miedo.
Esta ruta ya no pertenece a los aldeanos, ahora es mía. Aquí caen los
que viajan confiados, los que creen en cuentos del Sabio Anciano y en
finales felices. Yo recojo lo que queda… monedas, armas, recuerdos. No
es nada personal, solo supervivencia. Si quieres seguir adelante,
tendrás que aprender la primera lección de este mundo: nadie avanza
sin perder algo.
''')
P.discursos[2].insertarFinal(
'''Tal vez tengas razón… este mundo no es justo. Pero no permitire que
conviertas el miedo en tu ley. Si esta es la prueba para dejar atrás
la Aldea, la aceptaré. Hazte a un lado o serás solo otro obstáculo en
mi camino.
''')

#EXPLORADORA ERRANTE: (3)

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

# VIGIA DE LAS SOMBRAS (4)

vigiasombras.discursos.insertarFinal(
f'''Te observo desde antes de que tomaras este sendero, {P.nombre}.
Esta ruta 5 no es un camino, es una grieta entre lo que existe y lo
que debería haber muerto. Yo fui un guardián del Castillo Antiguo,
pero la oscuridad me reclamó cuando mis juramentos se rompieron. Ahora
 protejo este paso para que nadie más despierte aquello que duerme tras
 sus muros. Regresa, caminante. No todos los destinos están hechos para
 ser alcanzados. Algunos solo traen ruina a quien los persigue.
''')

P.discursos[4].insertarFinal(
'''Entonces eres una advertencia viviente… lo que ocurre cuando uno se
arrodilla ante la oscuridad. No vine hasta aquí para huir ante sombras
del pasado. Si el castillo encierra un mal, lo enfrentaré. Y si debo
cruzarte para hacerlo, que así sea. Tu vigilia termina hoy.
''')

# CURANDERA (5)

curandera.discursos.insertarFinal(
'''No temas, viajero. Pocos se detienen en esta
ruta sin estar heridos… por fuera o por dentro. Ruta 3 es un lugar
extraño: parece tranquila, pero escucha todo lo que pasa en el mapa.
El viento trae susurros del Bosque Encantado y, en noches claras,
incluso lamentos del Lago. Yo decidí quedarme para ayudar a quienes
aún creen que se puede avanzar sin perder del todo la esperanza. Tú
cargas un peso extraño… no solo armas, también decisiones que aún no
has tomado.
''')

P.discursos[5].insertarFinal(
'''No imaginaba encontrar calma en medio del camino. 
Seguiré adelante con más cuidado… y con más fe. Quizás no pueda 
salvarlo todo, pero haré lo posible por no perderme a mí mismo.
''')

curandera.discursos.insertarFinal(
'''Aquí me quedare para cuando necesites comprar pociones. 
Que tengas buena suerte, viajero.
''')

P.discursos[5].insertarFinal(
'''Gracias por tus palabras y por tu ayuda.
''')

# CARCELERO (6)

carcelero.discursos.insertarFinal(
'''Así que otro más desciende buscando respuestas… Todos creen que la 
mazmorra es solo piedra y oscuridad, pero aquí abajo se encierra algo 
peor: las culpas que nadie quiso cargar. Yo fui un guardián, como 
tantos otros, hasta que comprendí que las puertas no solo retenían 
monstruos… también protegían al mundo de ellos. Cuando mis hermanos 
huyeron, yo me quedé. La soledad me consumió, la oscuridad me enseñó 
su lenguaje… y ahora ya no distingo al prisionero del guardián. Si 
cruzas esta sala, te convertirás en parte del encierro eterno
''')

P.discursos[6].insertarFinal(
'''Tal vez fuiste un héroe alguna vez, pero ahora solo eres una sombra 
de lo que eras. No vine a liberar horrores, sino a terminar con ellos. 
Si este es el precio para que nadie más caiga en esta prisión, lo 
pagaré. Tu vigilia termina aquí.
''')

# REY DEL OCASO (7)

rey.discursos.insertarFinal(
'''¿Así que has logrado atravesar rutas, sombras y guardianes para 
llegar hasta mi trono en ruinas? Hace siglos defendí este reino con 
honor, pero cuando el mundo me dio la espalda, solo la oscuridad 
respondió a mi llamado. Mis súbditos huyeron, mis muros cayeron… pero 
yo permanecí. El tiempo no avanza aquí como en el exterior. Cada 
piedra de este castillo recuerda la traición, cada pasillo repite mi 
nombre en susurros. Tú vienes creyéndote salvador, como tantos otros, 
pero todos terminaron arrodillados ante mi voluntad. Aquí no queda 
esperanza, solo un rey que se niega a desaparecer.
''')

P.discursos[7].insertarFinal(
'''Este castillo ya no es un reino, es una tumba. Aferrarte al pasado 
te convirtió en prisionero de tu propia corona. No vine a destronar 
a un rey, sino a liberar a este lugar de su maldición.
''')

# GUARDIAN LIBERADO (8)

guardian.discursos.insertarFinal(
'''…Así que al fin terminó. Durante años incontables estuve atrapado 
entre estas paredes, viendo al rey convertirse en algo que ya no era 
humano. Yo fui su capitán, su sombra en la guerra, su último fiel. 
Cuando el reino cayó, juré protegerlo incluso de sí mismo… y ese 
juramento se volvió mi cadena. La oscuridad lo consumió, y a mí 
conmigo. Pero tú rompiste el ciclo. El castillo vuelve a sentirse… 
silencioso, como debe ser. Gracias, viajero. No todos tienen el valor 
de enfrentarse a un rey que ya no sabe que ha muerto. Toma esto como 
prueba de tu victoria y como recuerdo: incluso los tronos más poderosos 
pueden convertirse en prisiones.
''')

P.discursos[8].insertarFinal(
'''No luché por gloria, sino para que este lugar pudiera descansar. 
Cumpliste tu deber hasta el final, capitán. Ahora eres libre.
''')

# VIGIA DEL HORIZONTE (9)

vigiahoriz.discursos.insertarFinal(
'''No muchos llegan hasta aquí sin cargar cicatrices… visibles o no. 
Ruta 6 es el último respiro antes de que el mundo se vuelva más oscuro. 
Yo observo desde esta colina desde hace años, buscando señales de que 
el ciclo por fin cambiará. He visto pasar héroes, bandidos, reyes 
disfrazados de mendigos… y casi todos retrocedieron. Tú no miras atrás 
del mismo modo. Hay cansancio en tus pasos, pero también determinación. 
Eso es raro. Si sigues adelante, ya no habrá rutas seguras, solo 
decisiones sin retorno. No te daré promesas, solo una verdad: aquello 
que buscas también te está buscando.
''')

P.discursos[9].insertarFinal(
'''Entonces no soy el único que siente ese llamado. He llegado 
demasiado lejos para dudar ahora. Gracias por tu advertencia, vigía. 
Si vuelvo a pasar por aquí, espero que sea con el mundo un poco más 
libre que hoy.
''')

# LOBO SOMBRIO (10)

lobo.discursos.insertarFinal(
'''Huelo tu miedo desde que cruzaste las raíces del bosque, {P.nombre} ..., aunque 
intentes ocultarlo con valor. Yo no nací como sombra. Fui guardián de 
estas tierras cuando aún estaban llenas de luz. Cazaba para proteger, 
no para destruir. Pero la magia torcida del Castillo y la codicia de 
los hombres envenenaron el bosque… y a mí con él. Ahora soy el colmillo 
de su rencor, el aullido que anuncia que nadie cruza este lugar sin 
pagar un precio. No lucho por maldad, viajero. Lucho porque ya no sé 
vivir de otra forma.
''')

P.discursos[10].insertarFinal(
'''Entonces aún queda algo de ti bajo esa oscuridad. No vine a cazar un 
animal, sino a romper una maldición. Si debo enfrentarte para 
devolverle la paz al bosque… lo haré. Que este combate sea el 
final de tu tormento.
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
    enem = P.ubicActual.enem_pend.peek()
    obj = enem.objetoRequerido
    if obj is not None:
      if P.inventario.buscar(obj.nombre) == None:
        print(f"Necesitas el objeto '{enem.objetoRequerido.nombre}' para enfrentarte a este enemigo.")
        print(f"Parece que tendras que regresar y buscarlo en otra parte.")
        P.huir()
        input("\nPresiona ENTER para continuar...")
        continue

    print("Un momento! Parece que hay amenazas...\n")
    print(f"Aparecio {enem.nombre}. ")
    print("------------------------------------------- ")
    verDiscurso(P, enem)
    print("------------------------------------")
    print("Que deseas hacer?")
    print(" huir | luchar")

    while True:
      opc = input("-->")
      if opc == "huir" or opc == "luchar":
        break
      else:
        print("Opcion no valida. Elige 'huir' o 'luchar'")

    if opc == "huir":
      print(f"Has huido a {P.ubicActual.verUbicacionHuida()}")
      P.huir()
      input("\nPresiona ENTER para continuar...")
    elif opc == "luchar":
      while True:
        #Combate por turnos simple
        print(f"\nTu salud: {P.salud}  |  Salud de {enem.nombre}: {enem.salud}")
        print("\nElige una accion:")
        print(" atacar | pocion")
        opc2 = input("-->")

        if opc2 == "atacar":
          damage = randint(P.atk - 10, P.atk + 5)
          enem.salud -= damage
          print(f"Has causado {damage} puntos de daño a {enem.nombre}")
          if enem.salud <= 0:
            print(f"Has vencido a {enem.nombre}!")
            P.ubicActual.enem_pend.dequeue()
            P.XP += enem.xp_recompensa
            P.monedas += enem.monedas
            P.enemDerrotados += 1
            P.inventario.agregar(enem.objetoRecompensa)
            print(f"Has ganado {enem.xp_recompensa} XP y {enem.monedas} monedas.")
            print(f"Has obtenido el objeto clave: {enem.objetoRecompensa.nombre}")
            input("\nPresiona ENTER para continuar...")
            break

        elif opc2 == "pocion":
          if P.pociones <= 0:
            print("No te quedan pociones!")
            continue
          if P.salud == P.saludMax:
            print("Tu salud ya esta al maximo!")
            continue

          P.salud += 30
          P.pociones -= 1
          if P.salud > P.saludMax:
            P.salud = P.saludMax
          print("Has usado una pocion y recuperado 30 puntos de salud.")
          print(f"Te quedan {P.pociones} pociones.")

        else:
          print("Opcion no valida")
          continue
        # Turno del enemigo
        damage = randint(enem.atk - 5, enem.atk + 5)
        P.salud -= damage
        print(f"{enem.nombre} te ha causado {damage} puntos de daño.")
        if P.salud <= 0:
          print("Has sido derrotado...")
          print(f"Regresas a {P.ubicActual.verUbicacionHuida()}")
          P.huir()
          P.salud = P.saludMax
          enem.salud = enem.saludMax
          input("\nPresiona ENTER para continuar...")
          break

# Aqui se informa al jugador si existe algun personaje benevolente
# con quien haya que hablar primero para poder continuar

  elif P.ubicActual.hayBenevolentes():
    print("Hay un personaje en esta ubicacion que desa hablar contigo\n")
    print("-----------------------------------------------------------")
    personaje = P.ubicActual.benev_pend.dequeue()
    verDiscurso(P, personaje)
    input("\nPresiona ENTER para continuar...")

# Si no hay nada pendiente, se ofrecen las siguientes opciones

  else:

    if P.ubicActual.visitado == False:
      P.lugaresVisitados += 1
      P.ubicActual.visitado = True

    print(f"Puntos de salud: {P.salud} de {P.saludMax}\n")
    arriba = P.ubicActual.conex[ARR]
    abajo = P.ubicActual.conex[ABJ]
    izquier = P.ubicActual.conex[IZQ]
    derecha = P.ubicActual.conex[DER]

    print("         Que deseas hacer?\n")
    print("stats     : Ver tus estadisticas y objetos")
    print("pocion    : Usar una pocion para recuperar salud")
    print()
    if arriba  is not None: print(f"arriba    : Moverte a {arriba.nombre}")
    if abajo   is not None: print(f"abajo     : Moverte a {abajo.nombre}")
    if izquier is not None: print(f"izquierda : Moverte a {izquier.nombre}")
    if derecha is not None: print(f"derecha   : Moverte a {derecha.nombre}")

    if P.ubicActual.nombre == "Ruta 3":
      print("\ncomprar   : Comprar pociones a la curandera")

    print()
    print("salir     : Salir del juego\n")
    opc = input("--> ")
    print()

# Mostrar las estadisticas

    if opc == "stats":
      print(f"    ESTADISTICAS DE {P.nombre}")
      P.verEstadisticas()
      print("\n    INVENTARIO")
      P.verInventario()
      input("\nPresiona ENTER para continuar...")


# Usar una pocion para recuperar salud

    elif opc == "pocion":
      if P.pociones <= 0:
        print("No te quedan pociones!")
      elif P.salud == 100:
        print("Tu salud ya esta al maximo!")
        print("No has gastado la pocion.")
      else:
        P.salud += 30
        P.pociones -= 1
        if P.salud > 100:
          P.salud = 100
        print("Has usado una pocion y recuperado 30 puntos de salud.")
        print(f"Te quedan {P.pociones} pociones.")

      print(f"Tu salud actual es {P.salud}.")
      input("\nPresiona ENTER para continuar...")

# Comprar pociones a la curandera

    elif opc == "comprar":
      if P.ubicActual.nombre == "Ruta 3":
        costo = 3
        print(f"La curandera ofrece pociones por {costo} monedas cada una.")
        print(f"Tienes {P.monedas} monedas.")

        if P.monedas < costo:
          print("\nNo tienes suficientes monedas para comprar pociones.")
          input("\nPresiona ENTER para continuar...")
          continue
        
        while True:
          print("\nCuantas pociones deseas comprar?")
          cantidad = pedirnumero()
          if cantidad < 0:
            print("Ingresa un numero valido.")
            continue
          costototal = cantidad * costo
          if costototal > P.monedas:
            print("No tienes suficientes monedas para esa cantidad.")
            continue
          break
        
        P.monedas -= costototal
        P.pociones += cantidad
        if cantidad == 0:
          print("No has comprado ninguna pocion.")
        else:
          print(f"Has comprado {cantidad} pociones por {costototal} monedas.")
          print(f"Ahora tienes {P.pociones} pociones y {P.monedas} monedas restantes.")
        input("\nPresiona ENTER para continuar...")

      else:
        print("No hay nadie aqui para comprar pociones.")
      
      input("\nPresiona ENTER para continuar...")

# Mover al protagonista de ubicacion

    elif opc == "arriba" or opc == "abajo" or opc == "derecha" or opc == "izquierda":
      direc = obtenerNumDireccion(opc)
      
      if P.ubicActual.conex[direc] is not None:
        P.mover(direc)
      else:
        print("No hay nada en esa direccion")
        input("\nPresiona ENTER para continuar...")

# Salir del juego

    elif opc == "salir":
      print("Saliendo")
      exit()


# Opcion no valida
    else:
      print("Opcion no valida. Asegurate de escribir los comandos en minuscula")
      input("\nPresiona ENTER para continuar...")
