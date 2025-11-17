class Objeto:
  def __init__(self, nombre):
    self.nombre = nombre
    self.cantidad = 0

  def agregarCantidad(self):
    self.cantidad += 1

  def reducirCantidad(self):
    self.cantidad -= 1