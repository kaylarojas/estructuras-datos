from nodo import Nodo
class LinkedSet:

    def __init__(self):
        self.cabeza = None
        self._size = 0

    def is_empty(self):
        return self.cabeza is None

    def size(self):
        return self._size

    def contains(self, elemento):
        actual = self.cabeza

        while actual is not None:
            if actual.dato == elemento:
                return True
            actual = actual.siguiente

        return False

    def add(self, elemento):
        # No insertar duplicados
        if self.contains(elemento):
            return False

        nuevo = Nodo(elemento)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo
        self._size += 1
        return True

    def remove(self, elemento):
        actual = self.cabeza
        anterior = None

        while actual is not None:

            if actual.dato == elemento:

                if anterior is None:
                    self.cabeza = actual.siguiente
                else:
                    anterior.siguiente = actual.siguiente

                self._size -= 1
                return True

            anterior = actual
            actual = actual.siguiente

        return False

    def display(self):
        actual = self.cabeza

        print("{ ", end="")

        while actual is not None:
            print(actual.dato, end=" ")
            actual = actual.siguiente

        print("}")

conjunto = LinkedSet()

conjunto.add(10)
conjunto.add(5)
conjunto.add(8)
conjunto.add(10)      # No se inserta

conjunto.display()

print(conjunto.contains(5))
print(conjunto.contains(20))

conjunto.remove(5)

conjunto.display()

print("Cantidad:", conjunto.size())