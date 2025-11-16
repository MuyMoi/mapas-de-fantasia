class Personaje:
  def hablar(self):
    print(self.discurso)

class Sabio (Personaje):
  def __init__(self):
    self.discurso = '''Hola, soy un sabio que puede ayudarte'''
