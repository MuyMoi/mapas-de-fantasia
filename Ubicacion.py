from Benevolente import *
from Enemigo import *
from cola import *

# Constantes de direccion
IZQ = 0
DER = 1
ARR = 2
ABJ = 3

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
o bien -1 si la ubicacion no necesita direccion hacia donde huir.'''

class Ubicacion:
  def __init__(self, nombre, descripcion, direccionHuida = -1):
    self.nombre = nombre
    self.descrip = descripcion
    self.conex = [None] * 4
    self.benev_pend = Cola()  # Cola Benevolentes Pendientes
    self.enem_pend = Cola()   # Cola enemigos Pendientes
    self.direcHuida = direccionHuida

# comprobar si hay enemigos por vencer en la ubicacion actual

  def hayEnemigos(self):
    return not self.enem_pend.isEmpty()

# comprobar si hay personajes buenos que quieran hablar

  def hayBenevolentes(self):
    return not self.benev_pend.isEmpty()

  def verUbicacionHuida(self):
    return self.conex[self.direcHuida].nombre

# El siguiente metodo añade una conexion de forma bidireccional
# desde la ubicacion actual en direccion "direc" hacia U2. Es
# decir, que U2 tambien hara referencia, en la direccion contraria,
# a U1

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