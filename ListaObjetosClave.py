from listaenlazadasimple import *

class ListaObjetosClave(ListaEnlazadaSimple):
  def buscar(self, nombre):
    aux = self.inicio
    while aux != None:
      if aux.dato.nombre == nombre:
        return aux.dato
      aux = aux.next
    return None
  
  def agregar(self, objeto):
    self.insertarFinal(objeto)