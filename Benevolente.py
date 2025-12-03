from listaenlazadasimple import *

'''Personas o criaturas que hablan con el jugador para
darle informacion valiosa

- "discursos": lista con los parrafos que dice el personaje
'''

class Benevolente:
  def __init__(self, nombre, _id):
    self.nombre = nombre
    self.id = _id
    self.discursos = ListaEnlazadaSimple()
