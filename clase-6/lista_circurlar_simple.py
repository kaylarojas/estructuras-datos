# =========================
# Lista circular simple
# =========================
from nodo import Nodo

class ListaCircular:
    def __init__(self):
        self.cabeza = None

    def agregar(self, dato):
        nuevo = Nodo(dato)

        if self.cabeza is None:
            self.cabeza = nuevo
            nuevo.siguiente = self.cabeza
        else:
            actual = self.cabeza

            while actual.siguiente != self.cabeza:
                actual = actual.siguiente

            actual.siguiente = nuevo
            nuevo.siguiente = self.cabeza

    def mostrar(self):
        if self.cabeza is None:
            print("Lista vacía")
            return

        actual = self.cabeza

        while True:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente

            if actual == self.cabeza:
                break

        print("(vuelve a la cabeza)")


# Ejemplo
circular = ListaCircular()
circular.agregar("A")
circular.agregar("B")
circular.agregar("C")

circular.mostrar()