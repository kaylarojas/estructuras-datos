# =========================
# Lista doblemente enlazada
# =========================
from nodo_doble import NodoDoble

class ListaDoblementeEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, dato):
        nuevo = NodoDoble(dato)

        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente

            actual.siguiente = nuevo
            nuevo.anterior = actual

    def buscar(self, dato):
        actual = self.cabeza

        while actual:
            if actual.dato == dato:
                return True
            actual = actual.siguiente

        return False

    def eliminar(self, dato):
        actual = self.cabeza

        while actual:
            if actual.dato == dato:
                if actual.anterior:
                    actual.anterior.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente

                if actual.siguiente:
                    actual.siguiente.anterior = actual.anterior

                return True

            actual = actual.siguiente

        return False

    def mostrar_adelante(self):
        actual = self.cabeza

        while actual:
            print(actual.dato, end=" <-> ")
            actual = actual.siguiente

        print("None")


# Ejemplo
lista_doble = ListaDoblementeEnlazada()
lista_doble.agregar(5)
lista_doble.agregar(15)
lista_doble.agregar(25)

lista_doble.mostrar_adelante()
lista_doble.eliminar(15)
lista_doble.mostrar_adelante()