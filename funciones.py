# funcion utilitaria para obtener el numero correspondiente
# a una direccion (0,1,2,3) a partir de un string. Si no es
# valido, retorna -1

IZQ = 0
DER = 1
ARR = 2
ABJ = 3

def obtenerNumDireccion(string):
  if string == "arriba":    return ARR
  if string == "abajo":     return ABJ
  if string == "izquierda": return IZQ
  if string == "derecha":   return DER
  return -1

# Ver la ayuda del juego
def verAyuda():
  print('''
Este juego consiste en moverte por distintos mapas
y enfrentar diversos enemigos, a los cuales deberás
vencer para poder continuar la exploración. Como los
venceras? Deberas analizar a cada uno y determinar
la mejor estrategia. Si te derrota, deberas regresar
a una ubicacion anterior para recargar energias.

El mapa consta de 6 ubicaciones mas 6 rutas. En cada
ubicacion podras encontrar objetos, como pociones,
monedas y otros objetos que te seran de utilidad para
enfrentar a los enemigos. Tambien podras encontrar
personajes benevolentes que te daran consejos o hasta
objetos.

Cada vez que logres avanzar, obtendras puntos de
experiencia.

Finalizaras la aventura cuando derrotes al jefe final,
al cual deberas encontrar.

Buena suerte!

Presiona ENTER para iniciar la aventura''')
  input()
