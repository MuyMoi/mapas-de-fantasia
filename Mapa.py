from Personaje import *
from cola import *

'''"Ubicación" representa un punto especifico del mapa. "nombre"
es un string con el nombre del lugar, "conex" es un arreglo de 4
elementos con las conexiones a otras ubicaciones, ordenadas así:
# conex[0] : izquierda
# conex[1] : derecha
# conex[2] : arriba
# conex[3] : abajo
Ademas, tambien tiene un atributo "descrip" con la descripcion
del lugar, "pP" es una cola donde se almacenan los personajes
pendientes por hablar en la ubicacion, "eP" es otra cola con los
enemigos pendientes por vencer, "direcHuida" es la direccion en
la cual el protagonista retrocede cuando huye o pierde contra
algun enemigo. La direccion de huida es un numero entre 0 y 3,
o bien -1 si la ubicacion no necesita direccion hacia donde huir.
Por ultimo, "Lp" es la lista (o mejor dicho arreglo) de personajes
que existen. Se utiliza para poder seguir hablando con los
personajes, incluso despues de que desaparecen de la cola.'''

class Ubicacion:
  def __init__(self, nombre, descripcion, direccionHuida = -1):
    self.nombre = nombre
    self.descrip = descripcion
    self.conex = [None] * 4
    self.CpP = Cola()  # Cola personajes Pendientes
    self.CeP = Cola()  # Cola enemigos Pendientes
    self.Lp = [None] * 2 # Lista de personajes
    self.direcHuida = direccionHuida

  def hayEnemigos(self):
    return not self.CeP.isEmpty()

  def hayPersonajes(self):
    return not self.CpP.isEmpty()


# Constantes de direccion
IZQ = 0
DER = 1
ARR = 2
ABJ = 3


# El siguiente metodo añade una conexion de forma bidireccional
# desde U1 en la direccion "direc" hacia U2. Es decir, que
# U2 tambien hara referencia, en la direccion contraria, a U1

def agregarconex(U1, direc, U2):
  U1.conex[direc] = U2
  direc2 = -1

  match direc:
    case 0:
      direc2 = DER
    case 1:
      direc2 = IZQ
    case 2:
      direc2 = ABJ
    case 3:
      direc2 = ARR

  U2.conex[direc2] = U1



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

agregarconex(aldea, ABJ, ruta1)
agregarconex(ruta1, DER, lago)
agregarconex(aldea, DER, ruta2)
agregarconex(ruta2, DER, campamento)
agregarconex(campamento, DER, ruta3)
agregarconex(ruta3, DER, ruta4)
agregarconex(ruta4, ABJ, mazmorra)
agregarconex(ruta4, ARR, castillo)
agregarconex(castillo, IZQ, ruta6)
agregarconex(ruta6, IZQ, bosque)
agregarconex(ruta6, ABJ, ruta5)
agregarconex(ruta5, ABJ, campamento)


# Añadir personajes

sabio = Personaje("Sabio Anciano",
  '''Hola, joven! Soy un sabio anciano y puedo guiarte en...''')
aldea.CpP.enqueue(sabio)