from listaenlazadasimple import *

'''La clase Personaje representa personas
o criaturas que hablan con el jugador para darle informacion
valiosa. Es decir, ayudan al protagonista. Tiene un metodo
hablar() para decir un texto almacenado en el atributo
"discurso"
''' 

class Benevolente:
  def __init__(self, nombre, _id):
    self.nombre = nombre
    self.id = _id
    self.discursos = ListaEnlazadaSimple()
