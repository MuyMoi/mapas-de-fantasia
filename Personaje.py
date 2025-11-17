'''La clase Personaje representa personas
o criaturas que hablan con el jugador para darle informacion
valiosa. Es decir, ayudan al protagonista. Tiene un metodo
hablar() para decir un texto almacenado en el atributo
"discurso"
''' 
class Personaje:
  def __init__(self, nombre, discurso):
    self.nombre = nombre
    self.discurso = discurso

  def hablar(self):
    print(self.discurso)