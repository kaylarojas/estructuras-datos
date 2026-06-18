# =========================
# 6. Pila usando array/lista
# Push y pop
# =========================

class PilaArray:
    def __init__(self):
        self.elementos = []

    def push(self, dato):
        self.elementos.append(dato)

    def pop(self):
        if self.esta_vacia():
            return None
        return self.elementos.pop()

    def esta_vacia(self):
        return len(self.elementos) == 0

    def mostrar(self):
        print(self.elementos)


# Ejemplo
pila = PilaArray()
pila.push(10)
pila.push(20)
pila.push(30)

pila.mostrar()
print(pila.pop())
pila.mostrar()