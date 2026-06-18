# =========================
# 7. Pila usando lista enlazada
# Push y pop
# =========================
from nodo import Nodo

class PilaListaEnlazada:
    def __init__(self):
        self.tope = None

    def push(self, dato):
        nuevo = Nodo(dato)
        nuevo.siguiente = self.tope
        self.tope = nuevo

    def pop(self):
        if self.esta_vacia():
            return None

        dato = self.tope.dato
        self.tope = self.tope.siguiente
        return dato

    def esta_vacia(self):
        return self.tope is None

    def mostrar(self):
        actual = self.tope

        while actual:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente

        print("None")


# Ejemplo
pila_lista = PilaListaEnlazada()
pila_lista.push("A")
pila_lista.push("B")
pila_lista.push("C")

pila_lista.mostrar()
print(pila_lista.pop())
pila_lista.mostrar()