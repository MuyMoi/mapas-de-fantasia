'''Arbol que almacena referencia del hijo al padre,
no del padre a hijos'''

class ArbolInverso:
  def __init__(self, nodo_grafo, arbol_inverso):
    self.nodo = nodo_grafo
    self.padre = arbol_inverso