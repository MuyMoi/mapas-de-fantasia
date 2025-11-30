from os import system

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
Este juego consiste en moverte por distintas ubicaciones
y explorarlos todos, enfrentando cualquier amenaza que
te impida seguir con comodidad.

Tendras un menu principal con opciones para ver tus stats,
objetos, usar pociones, moverte de mapa, comprar pociones
(solo disponibles en una ubicacion) y salir del juego.
Es posible que al llegar a un lugar aparezca un personaje
benevolente con algo que decirte, o bien un enemigo con
ganas de luchar.

Si te aparece un enemigo, deberas vencerlo en un combate
simple para poder continuar la exploración. Si los vences,
te daran recompensas en forma de monedas, puntos XP y
objetos clave que necesitaras para poder continuar.
Si te derrota, seras regresado a una ubicacion anterior.
Si no tienes un objeto necesario para seguir por una
ubicacion, deberas buscarlo en otro lado.

Puedes usar pociones para recuperar 30 puntos de salud, pero
no podrás tener más de 100 puntos de salud, así que usalas
sabiamente.

Finalizaras la aventura cuando explores todos los mapas y
derrotes al último enemigo.

Buena suerte, viajero!
''')
  input("Presiona ENTER para iniciar la aventura...")

def limpiarPantalla():
  system("clear")

def objetoConseguido(objeto, listaobjetos):
  return listaobjetos.buscar(objeto.nombre) != None

def pedirnumero():
    try:
        n = int(input("-->"))
    except:
        print("Numero no valido")
        return pedirnumero()  #volver a pedir
    return n

def verDialogo(protagonista, personaje):
  discurso1 = personaje.discursos
  discurso2 = protagonista.discursos[personaje.id]

  while discurso1.actual is not None:
    print(f"{personaje.nombre}: {discurso1.actual.dato}")
    print(f"{protagonista.nombre}: {discurso2.actual.dato}")
    discurso1.avanzar_ptr()
    discurso2.avanzar_ptr()

  discurso1.reiniciar_ptr()
  discurso2.reiniciar_ptr()

def verMensajeFinal(prota):
  print(f'''    Felicitaciones, {prota.nombre}!
Has sabido mantener la calma en situaciones que muchos otros no
fueron capaces de soportar. Has liberado este mapa de todas las
amenazas, maleantes y espíritus que la arrinconaban y mantenian
en vilo a los pocos habitantes. Ahora se respira paz y alegría.

Eres un heroe!

    TUS ESTADISTICAS FINALES:
''')
  prota.verEstadisticas()
  print("\n    OBJETOS RECOLECTADOS:")
  prota.verInventario()