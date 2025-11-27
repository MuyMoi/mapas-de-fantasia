from Objeto import *
from Mapa import *
from listaenlazadasimple import *

''' Representa al protagonista y contiene el nombre
personalizado, los puntos de experiencia (XP)
ganados, cantidad de lugares visitados, enemigos
derrotados, un arreglo con el inventario de objetos,
el numero de objetos y la ubicacion actual.'''

class Protagonista:
  def __init__(self, nombre):
    self.nombre=nombre
    self.XP=0
    self.lugaresVisitados=0
    self.enemDerrotados=0
    self.inventario = [
      Objeto("Monedas"),
      Objeto("Pociones")]
    self.numObjetos = 2
    self.ubicActual = None
    self.discursos = [None] * 11
    for i in range(0, 11):
      self.discursos[i] = ListaEnlazadaSimple()

  def verInventario(self):
    I = self.inventario
    for i in range(self.numObjetos):
      print(f"{I[i].nombre}:\t{I[i].cantidad}")

  def verEstadisticas(self):
    print(f"XP: {self.XP}")
    print(f"Lugares visitados: {self.lugaresVisitados}")
    print(f"Enemigos derrotados: {self.enemDerrotados}")
    print(f"")

  def mover(self, direc):
    self.ubicActual = self.ubicActual.conex[direc]

  def huir(self, direc):
    A = self.ubicActual
    if A.direcHuida != -1:
      self.ubicActual = A.conex[A.direcHuida]