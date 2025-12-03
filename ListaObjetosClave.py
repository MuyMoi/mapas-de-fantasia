from listaenlazadasimple import *

'''Lista de objetos clave (inventario del jugador)
Hereda de ListaEnlazadaSimple
'''
class ListaObjetosClave(ListaEnlazadaSimple):

  # buscar por nombre de objeto
  def buscar(self, nombre):
    aux = self.inicio
    while aux != None:
      if aux.dato.nombre == nombre:
        return aux.dato
      aux = aux.next
    return None
  
  # agregar objeto
  def agregar(self, objeto):
    self.insertarFinal(objeto)