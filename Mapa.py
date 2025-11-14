# "Ubicación" representa un punto especifico del mapa. Tiene
# un nombre y un arreglo de 4 elementos con las conexiones
# a otras ubicaciones, ordenadas así:
# conex[0] : izquierda
# conex[1] : derecha
# conex[2] : arriba
# conex[3] : abajo
class Ubicacion:
  def __init__(self, nombre, descripcion, esRuta=True):
    self.nombre = nombre
    self.descrip = descripcion
    self.conex = [None] * 4
    self.esRuta = esRuta

# Constantes de direccion
IZQ = 0
DER = 1
ARR = 2
ABJ = 3

class Mapa:
  def __init__(self):
    # Crear los lugares que componen el mapa
    aldea = Ubicacion("Aldea principal",
      "Tu hogar desde niño")
    lago = Ubicacion("Lago sagrado",
      "Dicen que si tocas esta agua tendras una muerte indeseable. Cuidado!")
    campamento = Ubicacion("Campamento", 
      "")
    mazmorra = Ubicacion("Mazmorra",
      "")
    castillo = Ubicacion("Castillo antiguo",
      "")
    bosque = Ubicacion("Bosque encantado",
      "")

    # Crear las rutas que conectan los lugares
    ruta1 = Ubicacion("Ruta 1",
      "", True)
    ruta2 = Ubicacion("Ruta 2",
      "", True)
    ruta3 = Ubicacion("Ruta 3",
      "", True)
    ruta4 = Ubicacion("Ruta 4",
      "", True)
    ruta5 = Ubicacion("Ruta 5",
      "", True)
    ruta6 = Ubicacion("Ruta 6",
      "", True)
    
    # Establecer sus conexiones bidireccionales
    self.agregarconex(aldea, ABJ, ruta1)
    self.agregarconex(ruta1, DER, lago)
    self.agregarconex(aldea, DER, ruta2)
    self.agregarconex(ruta2, DER, campamento)
    self.agregarconex(campamento, DER, ruta3)
    self.agregarconex(ruta3, DER, ruta4)
    self.agregarconex(ruta4, ABJ, mazmorra)
    self.agregarconex(ruta4, ARR, castillo)
    self.agregarconex(castillo, IZQ, ruta6)
    self.agregarconex(ruta6, IZQ, bosque)
    self.agregarconex(ruta6, ABJ, ruta5)
    self.agregarconex(ruta5, ABJ, campamento)

    # Establecer la ubicacion actual inicial
    self.actual = aldea


# El siguiente metodo añade una conexion de forma bidireccional
# desde U1 en la direccion "direc" hacia U2. Es decir, que
# U2 tambien hara referencia, en la direccion contraria, a U1

  def agregarconex(self, U1, direc, U2):
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
  

  # Mueve la ubicacion actual en la direccion dada
  def mover(self, direc):
    self.actual = self.actual.conex[direc]