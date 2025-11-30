from ObjetoClave import *
from Ubicacion import *
from listaenlazadasimple import *
from ListaObjetosClave import *

''' Representa al protagonista y contiene el nombre
personalizado, los puntos de experiencia (XP)
ganados, cantidad de lugares visitados, enemigos
derrotados, un arreglo con el inventario de objetos,
el numero de objetos y la ubicacion actual.'''

class Protagonista:
  def __init__(self, nombre):
    self.nombre=nombre
    self.XP=0
    self.saludMax = 100
    self.salud=100
    self.lugaresVisitados=0
    self.enemDerrotados=0
    self.monedas  = 0
    self.pociones = 0
    self.inventario = ListaObjetosClave()
    self.ubicActual = None
    self.discursos = [0] * 11
    self.atk = 20
    
    for i in range(0, 11):
      self.discursos[i] = ListaEnlazadaSimple()

  def verInventario(self):
    print(f"Monedas: {self.monedas}")
    print(f"Pociones: {self.pociones}")
    
    I = self.inventario
    if not I.estaVacia():
      while I.actual != None:
        print(f"{I.actual.dato.nombre}")
        I.avanzar_ptr()
      I.reiniciar_ptr()

  def verEstadisticas(self):
    print(f"Puntos de Salud: {self.salud}")
    print(f"Puntaje: {self.XP} XP")
    print(f"Lugares visitados: {self.lugaresVisitados}")
    print(f"Enemigos derrotados: {self.enemDerrotados}")
    

  def mover(self, direc):
    self.ubicActual = self.ubicActual.conex[direc]

  def huir(self):
    A = self.ubicActual
    if A.direcHuida != -1:
      self.ubicActual = A.conex[A.direcHuida]