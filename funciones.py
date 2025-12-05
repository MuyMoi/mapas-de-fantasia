from os import system
from cola import *
from pila import *
from listaenlazadasimple import *
from ArbolInverso import *


IZQ = 0
DER = 1
ARR = 2
ABJ = 3

# funcion utilitaria para obtener el numero correspondiente
# a una direccion (0,1,2,3) a partir de un string. Si no es
# valido, retorna -1
def obtenerNumDireccion(string):
  if string == "arriba":    return ARR
  if string == "abajo":     return ABJ
  if string == "izquierda": return IZQ
  if string == "derecha":   return DER
  return -1

# Ver la ayuda del juego
def verAyuda():
  print('''
Este juego consiste en moverte por distintas ubicaciones
y explorarlos todos, enfrentando cualquier amenaza que
te impida seguir con comodidad.

Tendras un menu principal con opciones para ver tus stats,
objetos, usar pociones, moverte de mapa, comprar pociones
(solo disponibles en una ubicacion) y salir del juego.
Es posible que al llegar a un lugar aparezca un personaje
benevolente con algo que decirte, o bien un enemigo con
ganas de luchar.

Si te aparece un enemigo, deberas vencerlo en un combate
simple para poder continuar la exploración. Si los vences,
te daran recompensas en forma de monedas, puntos XP y
objetos clave que necesitaras para poder continuar.
Si te derrota, seras regresado a una ubicacion anterior.
Si no tienes un objeto necesario para seguir por una
ubicacion, deberas buscarlo en otro lado.

Puedes usar pociones para recuperar 30 puntos de salud, pero
no podrás tener más de 100 puntos de salud, así que usalas
sabiamente.

Finalizaras la aventura cuando explores todos los mapas y
derrotes al último enemigo.

Buena suerte, viajero!
''')
  input("Presiona ENTER para iniciar la aventura...")

# Limpiar la pantalla de la terminal
# - Si estas en Windows, cambialo por system("cls")
# - Si estas en Linux o macOS, cambialo por system("clear")
def limpiarPantalla():
  system("clear")

# Ver si un objeto clave ya fue conseguido
def objetoEnInventario(objeto, listaobjetos):
  return listaobjetos.buscar(objeto.nombre) != None

# Pedir un numero al usuario, con manejo de errores
def pedirnumero():
  try:
    n = int(input("-->"))
  except:
    print("Numero no valido")
    return pedirnumero()  #volver a pedir
  return n

# Ver el dialogo entre el protagonista y un personaje
def verDialogo(protagonista, personaje):
  discurso1 = personaje.discursos
  discurso2 = protagonista.discursos[personaje.id]

  while discurso1.actual is not None:
    print(f"{personaje.nombre}: {discurso1.actual.dato}")
    print(f"{protagonista.nombre}: {discurso2.actual.dato}")
    discurso1.avanzar_ptr()
    discurso2.avanzar_ptr()

  discurso1.reiniciar_ptr()
  discurso2.reiniciar_ptr()

def usarPocion(prota, poderpocion):
  if prota.pociones <= 0:
    print("No te quedan pociones!")
    return False
  if prota.salud == prota.saludMax:
    print("Tu salud ya esta al maximo!")
    print("No has gastado la pocion.")
    print(f"Te quedan {prota.pociones} pociones.")
    return False
  
  prota.salud += poderpocion    # sumar puntos de salud
  prota.pociones -= 1
  if prota.salud > prota.saludMax:
    prota.salud = prota.saludMax   # limitar a salud maxima
  print(f"Has usado una pocion y recuperado {poderpocion} puntos de salud.")
  print(f"Te quedan {prota.pociones} pociones.")
  print(f"Tu salud actual es {prota.salud}.")
  return True


# Ver el mensaje final al completar la aventura
def verMensajeFinal(prota):
  print(f'''    Felicitaciones, {prota.nombre}!
Has sabido mantener la calma en situaciones que muchos otros no
fueron capaces de soportar. Has liberado este mapa de todas las
amenazas, maleantes y espíritus que la arrinconaban y mantenian
en vilo a los pocos habitantes. Ahora se respira paz y alegría.

Eres un heroe!

    TUS ESTADISTICAS FINALES:
''')
  prota.verEstadisticas()
  print("\n    OBJETOS RECOLECTADOS:")
  prota.verInventario()

# Ver si una ubicacion es transitable con el inventario actual
def esTransitable(ubicacion, inventario):
  if ubicacion is None:
    return False

  obj = ubicacion.objetoRequerido
  if obj is None:
    return True
  return objetoEnInventario(obj, inventario)


# ----------------------------
# Algoritmos de busqueda
#-----------------------------
# En este juego, se usan para saber hacia que mapa debe moverse
# el protagonista para encontrar al siguiente enemigo.
# El protagonista no puede pasar por algunos mapas porque
# requieren un objeto clave que el protagonista podria no
# tener todavía, así que se tiene en cuenta esta
# restriccion.


# algoritmo DFS (Depth First Search). Solo
# Permite saber el nombre de dicha ubicacion,
# mas no la ruta completa
def busquedaDFS(actual, visitados, inventario):
  visitados.insertarFinal(actual)

  if actual.hayEnemigos():
    return actual

  for i in range(4):
    vecino = actual.conex[i]
    if vecino != None and visitados.buscar(vecino) == None:
      if esTransitable(vecino, inventario):
        encontrado = buscarUbicacionMision(vecino, visitados, inventario)
        if encontrado:
          return encontrado
  return None


# algoritmo BFS (Breadth First Search)
# Devuelve un arbol con el que se puede reconstruir la ruta
# completa mas cercana

def busquedaBFS(origen, inventario):
  cola = Cola()              # cola de nodos pendientes por visitar
  visitados = ListaEnlazadaSimple()  # lista de nodos visitados
  nodo_inverso_padre = ArbolInverso(origen, None)  # Dato: ubicacion origen, Padre: None
  visitados.insertarFinal(origen)

  # en la cola no voy a meter directamente el nodo origen, sino
  # que lo voy a "encapsular" en la clase nodo inverso, para
  # no perder la referencia a cada nodo padre.
  cola.enqueue(nodo_inverso_padre)

  while not cola.isEmpty():   # mientras no quede nada por visitar
    actual = cola.dequeue()

    # Si aquí hay enemigos, terminamos la busqueda
    if actual.nodo.hayEnemigos():
      return actual

    # examino las direcciones
    for i in range(0,4):
      vecino = actual.nodo.conex[i]
      if (vecino is not None) and (visitados.buscar(vecino) is None):
        if esTransitable(vecino, inventario):
          visitados.insertarFinal(vecino)
          # Creo un nodo inverso, cuyo dato es el nodo vecino, y su padre
          # es el nodo inverso actual
          nodo_inv = ArbolInverso(vecino, actual)
          cola.enqueue(nodo_inv)
  return None  # No hay enemigos alcanzables

# Toma el arbol resultante, y reconstruye la ruta completa,
# devolviendola en una pila
def reconstruirRuta(arbol_inverso_fin):
  p = Pila()
  aux = arbol_inverso_fin
  while aux != None and aux.nodo != None:
    p.push(aux.nodo)
    aux = aux.padre

  return p

# Toma la pila e imprime, en orden, las ubicaciones
# desde la actual hasta la ultima
def mostrarRuta(pila_ubicaciones):
  ub = pila_ubicaciones.pop()
  if ub == None:
    print("No hay enemigos disponibles")
    return

  # Si el siguiente elemento a imprimir ya no existe,
  # no imprimo el actual todavia...
  while pila_ubicaciones.top != None:
    print(f"{ub.nombre} -> ", end="")
    ub = pila_ubicaciones.pop()

  # ...lo imprimo por separado para evitar que quede una flecha sin nada
  print(ub.nombre)
