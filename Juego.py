from Mapa import *

mapa = Mapa()

# funcion utilitaria para obtener el numero correspondiente
# a una direccion (0,1,2,3) a partir de un string. Si no es valido,
# retorna -1
def obtenerNumDireccion(string):
  if string == "arriba":    return ARR
  if string == "abajo":     return ABJ
  if string == "izquierda": return IZQ
  if string == "derecha":   return DER
  return -1


while True:
  print(f"\nEstas actualmente en {mapa.actual.nombre}")

  arriba = mapa.actual.conex[ARR]
  abajo = mapa.actual.conex[ABJ]
  izquier = mapa.actual.conex[IZQ]
  derecha = mapa.actual.conex[DER]

  print("Hacia donde te deseas mover? (Escribe la direccion en minuscula)")
  print(f" - Arriba:    {arriba.nombre if arriba is not None else "NADA"}")
  print(f" - Abajo:     {abajo.nombre if abajo is not None else "NADA"}")
  print(f" - Izquierda: {izquier.nombre if izquier is not None else "NADA"}")
  print(f" - Derecha:   {derecha.nombre if derecha is not None else "NADA"}")
  
  string = input("--> ")
  
  direc = obtenerNumDireccion(string)
  if direc == -1:
    print("Direccion no valida")
    continue
  
  if mapa.actual.conex[direc] is not None:
    mapa.mover(direc)
  else:
    print("No hay nada en esa direccion")