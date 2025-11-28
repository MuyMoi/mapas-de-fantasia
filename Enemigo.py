from listaenlazadasimple import *
from ListaObjetos import *

class Enemigo:
  def __init__(self, nombre, _id, saludMax, atk, xp_recompensa, monedas):
    self.nombre = nombre
    self.id = _id
    self.saludMax = saludMax
    self.salud = saludMax
    self.atk = atk
    self.xp_recompensa = xp_recompensa
    self.monedas = monedas
    self.discursos = ListaEnlazadaSimple()
    self.objetosRequeridos = ListaObjetos()
    self.objetosRecompensa = ListaObjetos()