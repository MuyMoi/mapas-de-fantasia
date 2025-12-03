from listaenlazadasimple import *
from ListaObjetosClave import *

'''Enemigos que el jugador debe vencer.

- "discursos": lista con los parrafos que dice el personaje
'''


class Enemigo:
  def __init__(self, nombre, _id, saludMax, atk, xp_recompensa, monedas):
    self.nombre = nombre
    self.id = _id
    self.discursos = ListaEnlazadaSimple()
    self.saludMax = saludMax  # salud maxima
    self.salud = saludMax     # salud actual
    self.atk = atk            # puntos de ataque
    self.xp_recompensa = xp_recompensa # recompensa de xp
    self.monedas = monedas    # recompensa en monedas
    self.objetoRecompensa = None  # objeto recompensa