from funciones import *
from Protagonista import *
from ArbolInverso import *
from pila import *

P = Protagonista("juan")



# -------------------------------------------
# CONFIGURACION DE LOS ELEMENTOS DEL JUEGO
# -------------------------------------------

# Crear los lugares que componen el mapa

aldea = Ubicacion("Aldea principal", "aldea", 
  "Un pequeño poblado rodeado de colinas y bosques. Ultimo " +
  "refugio de calma antes de adentrarse en un mundo corrompido")

lago = Ubicacion("Lago sagrado", "lago", 
  "Antigua fuente sagrada cuyas aguas ahora reflejan una " +
  "corrupción silenciosa y profunda.",
  direccionHuida=IZQ)

campamento = Ubicacion("Campamento", "campamen",
  "Puesto de descanso para viajeros, donde confluyen " +
  "advertencias, rumores y las últimas hogueras seguras del mapa")

mazmorra = Ubicacion("Mazmorra", "mazmorra",
  "Prisión subterránea de piedra y lamentos, construida para " +
  "encerrar horrores que nunca debieron liberarse",
  direccionHuida=ARR)

castillo = Ubicacion("Castillo antiguo", "castillo",
  "Fortaleza en ruinas atrapada en el tiempo, gobernada por " +
  "ecos de un reino que se niega a desaparecer",
  direccionHuida=ABJ)

bosque = Ubicacion("Bosque encantado", "bosque",
  "El aire es frío y oyes ruidos entre los árboles. Cada árbol " +
  "parece observar al viajero",
  direccionHuida=DER)


# Crear las rutas que conectan los lugares

ruta1 = Ubicacion("Ruta 1", "ruta1",
  "Camino inicial entre praderas suaves, donde el peligro aún " +
  "parece lejano y la aventura apenas despierta")
ruta2 = Ubicacion("Ruta 2", "ruta2"
  "Sendero rocoso dominado por bandidos, primer filtro entre " +
  "la inocencia de la aldea y la crudeza del viaje",
  direccionHuida=IZQ)
ruta3 = Ubicacion("Ruta 3", "ruta3",
  "Camino tranquilo en apariencia, donde el viento transporta " +
  "ecos de todo lo que ocurre en las regiones cercanas")
ruta4 = Ubicacion("Ruta 4", "ruta4",
  "Sendero estrecho entre rocas y niebla, paso olvidado que " +
  "conecta regiones sin la protección de rutas seguras")
ruta5 = Ubicacion("Ruta 5", "ruta5",
  "Paso oscuro vigilado por sombras antiguas, conexión directa " +
  "entre las ruinas del castillo y las tierras olvidadas",
  direccionHuida=ABJ)
ruta6 = Ubicacion("Ruta 6", "ruta6",
  "Ruta elevada y solitaria, donde el horizonte anuncia un punto " +
  "de no retorno para el viajero")


# Establecer sus conexiones bidireccionales
# Por ejemplo: partiendo de la aldea, ABAJO, está la ruta 1

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

espiritu = Enemigo("Espiritu del lago", 1, 100, 10, 50, 4)
espiritu.objetoRecompensa = amuleto
#lago.enem_pend.enqueue(espiritu)

saqueador = Enemigo("Saqueador del sendero", 2, 110, 15, 70, 10)
saqueador.objetoRecompensa = daga
#ruta2.objetoRequerido = amuleto
#ruta2.enem_pend.enqueue(saqueador)

exploradora = Benevolente("Exploradora Errante", 3)
campamento.benev_pend.enqueue(exploradora)

vigiasombras = Enemigo("Vigia de las Sombras", 4, 150, 20, 90, 5)
vigiasombras.objetoRecompensa = llaveAntigua
ruta5.objetoRequerido = llaveEncierro
ruta5.enem_pend.enqueue(vigiasombras)

curandera = Benevolente("Curandera del Camino", 5)
ruta3.benev_pend.enqueue(curandera)

carcelero = Enemigo("Carcelero de las Profundidades", 6, 200, 15, 80, 0)
carcelero.objetoRecompensa = llaveEncierro
mazmorra.objetoRequerido = corona
mazmorra.enem_pend.enqueue(carcelero)

rey = Enemigo("Rey del Ocaso", 7, 120, 18, 85, 40)
rey.objetoRecompensa = corona
castillo.enem_pend.enqueue(rey)

guardian = Benevolente("Guardian Liberado", 8)
castillo.benev_pend.enqueue(guardian)

vigiahoriz = Benevolente("Vigia del Horizonte", 9)
ruta6.benev_pend.enqueue(vigiahoriz)

lobo = Enemigo("Lobo Sombrio", 10, 200, 20, 150, 5)
lobo.objetoRecompensa = colmillo
bosque.objetoRequerido = llaveAntigua
bosque.enem_pend.enqueue(lobo)






def esTransitable(ubicacion, inventario):
    if ubicacion is None:
        return False

    obj = ubicacion.objetoRequerido
    if obj is None:
        return True
    return objetoEnInventario(obj, inventario)


# Esta funcion busca la ubicación mas proxima al protagonista en la
# cual hay enemigos que puede enfrentar. Tiene en cuenta la restriccion
# de que no puede pasar por algunos mapas por no tener algun objeto
# en su inventario, y evita repetir nodos añadiendolos a una lista de
# visitados.
# Para permitir reconstruir la ruta,se utiliza un "arbol inverso", en 
# el cual se considera que el nodo de partida es el padre, y los
# nodos vecinos a este son sus hijos. Sin embargo, solo se almacena
# una referencia al nodo padre, no al nodo hijo. Esto permitirá
# devolverse para reconstruir la ruta mas cercana, ya que el nodo final
# es el nodo hijo.

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

def reconstruirRuta(arbol_inverso_fin):
  p = Pila()
  aux = arbol_inverso_fin
  while aux != None and aux.nodo != None:
    p.push(aux.nodo)
    aux = aux.padre

  return p

def mostrarRuta(pila_ubicaciones):
  ub = pila_ubicaciones.pop()
  if ub == None:
    print("No hay enemigos disponibles")
    return

  # Si el siguiente elemento a imprimir ya no existe,
  # no imprimo el actual todavia
  while pila_ubicaciones.top != None:
    print(f"{ub.nombre} -> ", end="")
    ub = pila_ubicaciones.pop()

  # lo imprimo por separado para evitar que quede una flechita sin nada
  print(ub.nombre)


ruta = reconstruirRuta( busquedaBFS(ruta2, P.inventario) )
mostrarRuta(ruta)

while True:
  try:
    print("salida comando:", eval(input("-->")))
  except Exception as e:
    print(f"error: {e}")
'''

# buscar el mapa al cual ir para continuar la aventura
def buscarUbicacionMision(actual, visitados=None):        
    visitados.insertarFinal(actual)
    print(actual.nombre)
    
    if actual.hayEnemigos():
        return actual

    for i in range(4):
        vecino = actual.conex[i]
        if vecino != None and visitados.buscar(vecino) == None:
            if esTransitable(vecino, P.inventario):
                encontrado = buscarUbicacionMision(vecino, visitados)
                if encontrado != None:
                    return encontrado
    return None

print("DFS Recursivo:")
v = ListaEnlazadaSimple()
ub = buscarUbicacionMision(aldea, v)
print(ub.nombre if ub != None else "No se encontró ningún enemigo.")


def dfsBuscarEnemigo(origen, inventario):
    if origen is None:
        return None

    if origen.objetoRequerido and origen.objetoRequerido not in inventario:
        return None

    origen.visitado = True

    if origen.hayEnemigos():
        return origen

    for vecino in origen.conex:
        if vecino and not vecino.visitado:
            encontrado = dfsBuscarEnemigo(vecino, inventario)
            if encontrado:
                return encontrado

    return None

#print(dfsBuscarEnemigo(campamento, P.inventario))
'''