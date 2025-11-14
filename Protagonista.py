from Objeto import *

class Protagonista:
    def __init__(self, nombre):
        self.nombre=nombre
        self.XP=0
        self.rutasVisitadas =0
        self.lugaresVisitados=0
        self.enemDerrotados=0
        self.inventario = [Objeto("Monedas"),
            Objeto("Pociones")]