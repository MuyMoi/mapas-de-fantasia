from Benevolente import *
from Enemigo import *
from cola import *

# Constantes de direccion
IZQ = 0
DER = 1
ARR = 2
ABJ = 3

''' "Ubicación" representa un punto especifico del mapa.

"conex" es un arreglo de 4
elementos con las conexiones a otras ubicaciones, ordenadas así:

# conex[0] : izquierda
# conex[1] : derecha
# conex[2] : arriba
# conex[3] : abajo

- "benev_pend" y "enem_pend" almacenan los personajes pendientes
que esperan su turno para hablar con el jugador
- "nombre_menu" es el nombre que se mostrara en el menu principal
para acceder a este lugar
- "direcHuida" es el numero de direccion hacia la cual el protagonista
huye cuando es derrotado por los enemigos de la ubicacion actual
- "visitado" es True cuando el jugador ya ha visitado la ubicacion
- "objetoRequerido" es el objeto clave que se necesita para
entrar a la ubicacion
'''

class Ubicacion:
  def __init__(self, nombre, nombre_menu, descripcion, direccionHuida = -1):
    self.nombre = nombre
    self.nombre_menu = nombre_menu # nombre para mostrar en menu
    self.descrip = descripcion
    self.conex = [None] * 4   # conexiones
    self.benev_pend = Cola()  # Benevolentes Pendientes
    self.enem_pend = Cola()   # Enemigos Pendientes
    self.direcHuida = direccionHuida
    self.visitado = False
    self.objetoRequerido = None

# comprobar si hay enemigos por vencer en la ubicacion actual
  def hayEnemigos(self):
    return not self.enem_pend.isEmpty()

# comprobar si hay personajes buenos que quieran hablar
  def hayBenevolentes(self):
    return not self.benev_pend.isEmpty()

# ver nombre de la ubicacion de huida
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