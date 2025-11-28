from Objeto import *
from Ubicacion import *
from listaenlazadasimple import *
from ListaObjetos import *

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
    self.monedas=0
    self.pociones=3
    self.inventario = ListaObjetos()
    self.numObjetos = 2
    self.ubicActual = None
    self.discursos = [0] * 11
    self.atk = 20
    
    for i in range(0, 11):
      self.discursos[i] = ListaEnlazadaSimple()

  def verInventario(self):
    print(f"Monedas: {self.monedas}")
    print(f"Pociones: {self.pociones}")
    
    I = self.inventario
    while I.actual != None:
      print(f"- {aux.dato.nombre}")
      I.avanzar_ptr()
    I.reiniciar_ptr()

  def verEstadisticas(self):
    print(f"Puntos de Salud: {self.salud}")
    print(f"XP: {self.XP}")
    print(f"Lugares visitados: {self.lugaresVisitados}")
    print(f"Enemigos derrotados: {self.enemDerrotados}")
    

  def mover(self, direc):
    self.ubicActual = self.ubicActual.conex[direc]

  def huir(self):
    A = self.ubicActual
    if A.direcHuida != -1:
      self.ubicActual = A.conex[A.direcHuida]