from Mapa import *
from colorama import Fore, Back

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
  print(f"\n{Fore.GREEN}Estas actualmente en {mapa.actual.nombre}")
  print(Fore.RESET)  

  arriba = mapa.actual.conex[ARR]
  abajo = mapa.actual.conex[ABJ]
  izquier = mapa.actual.conex[IZQ]
  derecha = mapa.actual.conex[DER]

  print("Hacia donde te deseas mover?")
  print(Fore.RESET + " - Arriba:   ", Fore.GREEN + arriba.nombre if arriba is not None else Fore.RED + "NADA")
  print(Fore.RESET + " - Abajo:    ", Fore.GREEN + abajo.nombre if abajo is not None else Fore.RED + "NADA")
  print(Fore.RESET + " - Izquierda:", Fore.GREEN + izquier.nombre if izquier is not None else Fore.RED + "NADA")
  print(Fore.RESET + " - Derecha:  ", Fore.GREEN + derecha.nombre if derecha is not None else Fore.RED + "NADA")
  
  print(Back.WHITE + Fore.BLUE)
  string = input("--> ")
  print(Back.RESET)
  
  direc = obtenerNumDireccion(string)
  if direc == -1:
    print(f"{Fore.RED}Direccion no valida{Fore.RESET}")
    continue
  
  if mapa.actual.conex[direc] is not None:
    mapa.mover(direc)
  else:
    print(F"{Fore.RED}No hay nada en esa direccion{Fore.RESET}")
