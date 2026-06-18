# =========================
# 9. Cola
# enqueue, dequeue, isEmpty y front
# =========================

class Cola:
    def __init__(self):
        self.elementos = []

    def enqueue(self, dato):
        self.elementos.append(dato)

    def dequeue(self):
        if self.isEmpty():
            return None
        return self.elementos.pop(0)

    def isEmpty(self):
        return len(self.elementos) == 0

    def front(self):
        if self.isEmpty():
            return None
        return self.elementos[0]

    def mostrar(self):
        print(self.elementos)


# Ejemplo
cola = Cola()
cola.enqueue("Ana")
cola.enqueue("Luis")
cola.enqueue("Carlos")

cola.mostrar()
print("Frente:", cola.front())
print("Sale:", cola.dequeue())
cola.mostrar()