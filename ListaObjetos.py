from listaenlazadasimple import *

class ListaObjetos(ListaEnlazadaSimple):
  def buscarObjeto(self, nombre):
    aux = self.inicio
    while aux != None:
      if aux.dato.nombre == nombre:
        return aux.dato
      aux = aux.next
    return None