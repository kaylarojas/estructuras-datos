from nodo_map import NodoMap
class LinkedMap:

    def __init__(self):
        self.cabeza = None
        self._size = 0

    def is_empty(self):
        return self.cabeza is None

    def size(self):
        return self._size

    def put(self, clave, valor):
        """
        Inserta una nueva clave o actualiza su valor.
        """

        actual = self.cabeza

        while actual is not None:

            if actual.clave == clave:
                actual.valor = valor
                return

            actual = actual.siguiente

        nuevo = NodoMap(clave, valor)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo
        self._size += 1

    def get(self, clave):

        actual = self.cabeza

        while actual is not None:

            if actual.clave == clave:
                return actual.valor

            actual = actual.siguiente

        return None

    def contains_key(self, clave):

        return self.get(clave) is not None

    def remove(self, clave):

        actual = self.cabeza
        anterior = None

        while actual is not None:

            if actual.clave == clave:

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

        print("{")

        while actual is not None:
            print(f"   {actual.clave} : {actual.valor}")
            actual = actual.siguiente

        print("}")

agenda = LinkedMap()

agenda.put("Ana", "8888-1111")
agenda.put("Luis", "7777-2222")
agenda.put("Carlos", "6666-3333")

agenda.display()

print()

print("Teléfono de Ana:", agenda.get("Ana"))

agenda.put("Ana", "8888-9999")

print()

agenda.display()

agenda.remove("Luis")

print()

agenda.display()