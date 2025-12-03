class ElementoPila:
	def __init__(self, dato):
		self.next = None
		self.dato = dato

class Pila:
	def __init__(self):
		self.top = None

	def push(self,x):
		e = ElementoPila(x)
		e.next = self.top
		self.top = e

	def pop(self):
		if self.top == None:
			return None
		else:
			dato = self.top.dato
			self.top = self.top.next
			return dato

	def peek(self):
		if self.top == None:
			return None
		else:
			return self.top.dato

	def imprimir(self):
		e = self.top
		if e == None:
			print("Pila vacia")
		while e != None:
			print(e.dato)
			e = e.next