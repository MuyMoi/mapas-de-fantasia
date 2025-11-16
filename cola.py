class ElementoCola:
    def __init__(self, dato):
        self.dato = dato
        self.next = None

class Cola:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, x):
        e = ElementoCola(x)
        if self.isEmpty():
            self.head = e
            self.tail = e
        else:
            self.tail.next = e
            self.tail = e

    def dequeue(self):
        if self.head == None:
            return None
        
        x = self.head.dato
        self.head = self.head.next

        if self.isEmpty():
            self.tail = None

        return x

    def peek(self):
        if self.head == None:
            return None

        return self.head.dato

    def isEmpty(self):
        return self.head == None
