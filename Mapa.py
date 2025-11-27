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
del lugar, "CpP" es una cola donde se almacenan los personajes
pendientes por hablar en la ubicacion, "CeP" es otra cola con los
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

  def agregarconex(self, direc, U2):
    self.conex[direc] = U2
    
    direc2 = -1
    if direc == IZQ:
      direc2 = DER
    elif direc == DER:
      direc2 = IZQ
    elif direc == ARR:
      direc2 = ABJ
    elif direc == ABJ:
      direc2 = ARR
    else:
      return

    U2.conex[direc2] = self


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