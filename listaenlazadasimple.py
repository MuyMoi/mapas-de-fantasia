class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.next = None
    
class ListaEnlazadaSimple:
    def __init__(self):
        self.inicio = None
        self.fin = None
        self.actual = None
    
    def insertarInicio(self, dato):
        n = Nodo(dato)
        n.next = self.inicio
        self.inicio = n
        if self.fin == None:
            self.fin = self.inicio

    def insertarFinal(self, dato):
        n = Nodo(dato)
        if self.fin == None:
            self.fin = self.inicio = n
            self.actual = n
        else:
            self.fin.next = n
            self.fin = n

    def insertarOrdenado(self, x):
        if self.inicio != None:
            if x <= self.inicio.dato:
                self.insertarInicio(x)
            elif x >= self.fin.dato:
                self.insertarFinal(x)
            else:
                aux = self.inicio
                while aux!=None and aux.next!=None:
                    if x>aux.dato and x<aux.next.dato:
                        break
                    aux=aux.next
                n = Nodo(x)
                n.next = aux.next
                aux.next = n
        else:
            self.insertarInicio(x)
    
    def buscar(self, x):
        if self.inicio != None:
            aux = self.inicio
            while aux != None:
                if x == aux.dato:
                    return aux.dato
                aux = aux.next
            return None
        return None

    def eliminar(self, x):
        if self.inicio == None:
            return False
        if x==self.inicio.dato:
            self.inicio = self.inicio.next
            if self.inicio == None:
                self.fin = None
            return True

        if self.inicio == self.fin:
            return False

        ant = self.inicio
        actual = ant.next

        while actual.dato != x and actual.next != None:
            ant = actual
            actual = actual.next
        if actual.dato == x:
            ant.next = actual.next
            if ant.next == None:
                self.fin = ant
            return True
        else:
            return False

    def avanzar_ptr(self):
        self.actual = self.actual.next

    def reiniciar_ptr(self):
        self.actual = self.inicio

    def imprimir(self):
        if self.inicio == None:
            print("Lista vacia")
            return
        n = self.inicio
        while n != None:
            print(n.dato)
            n = n.next
