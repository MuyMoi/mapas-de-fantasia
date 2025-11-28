from listaenlazadasimple import *

class Enemigo:
  def __init__(self, nombre, _id):
    self.nombre = nombre
    self.id = _id
    self.discursos = ListaEnlazadaSimple()