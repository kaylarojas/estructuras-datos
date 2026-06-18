# =========================
# 11. Cola de prioridad
# enqueue, dequeue, isEmpty y front
# Menor número = mayor prioridad
# =========================
from nodo_prioridad import NodoPrioridad

class ColaPrioridad:
    def __init__(self):
        self.cabeza = None

    def enqueue(self, dato, prioridad):
        nuevo = NodoPrioridad(dato, prioridad)

        if self.cabeza is None:
            self.cabeza = nuevo

        elif prioridad < self.cabeza.prioridad:
            nuevo.siguiente = self.cabeza
            self.cabeza = nuevo

        else:
            actual = self.cabeza

            while actual.siguiente and actual.siguiente.prioridad <= prioridad:
                actual = actual.siguiente

            nuevo.siguiente = actual.siguiente
            actual.siguiente = nuevo

    def dequeue(self):
        if self.isEmpty():
            return None

        dato = self.cabeza.dato
        self.cabeza = self.cabeza.siguiente
        return dato

    def isEmpty(self):
        return self.cabeza is None

    def front(self):
        if self.isEmpty():
            return None
        return self.cabeza.dato

    def mostrar(self):
        actual = self.cabeza

        while actual:
            print(f"{actual.dato}({actual.prioridad})", end=" -> ")
            actual = actual.siguiente

        print("None")


# Ejemplo
cola_prioridad = ColaPrioridad()
cola_prioridad.enqueue("Paciente leve", 3)
cola_prioridad.enqueue("Paciente grave", 1)
cola_prioridad.enqueue("Paciente medio", 2)

cola_prioridad.mostrar()
print("Frente:", cola_prioridad.front())
print("Sale:", cola_prioridad.dequeue())
cola_prioridad.mostrar()