# =========================
# Lista enlazada simple
# =========================
from nodo import Nodo

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, dato):
        nuevo = Nodo(dato)

        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo

    def buscar(self, dato):
        actual = self.cabeza

        while actual:
            if actual.dato == dato:
                return True
            actual = actual.siguiente

        return False

    def eliminar(self, dato):
        actual = self.cabeza
        anterior = None

        while actual:
            if actual.dato == dato:
                if anterior is None:
                    self.cabeza = actual.siguiente
                else:
                    anterior.siguiente = actual.siguiente
                return True

            anterior = actual
            actual = actual.siguiente

        return False

    def mostrar(self):
        actual = self.cabeza

        while actual:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente

        print("None")


# Ejemplo
lista = ListaEnlazada()
lista.agregar(10)
lista.agregar(20)
lista.agregar(30)

lista.mostrar()
print(lista.buscar(20))
lista.eliminar(20)
lista.mostrar()