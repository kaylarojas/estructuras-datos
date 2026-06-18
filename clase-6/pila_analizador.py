# =========================
# Analizador de expresiones matemáticas con pilas
# =========================

def parentesis_balanceados(expresion):
    pila = []

    for caracter in expresion:
        if caracter == "(":
            pila.append(caracter)
        elif caracter == ")":
            if len(pila) == 0:
                return False
            pila.pop()

    return len(pila) == 0


# Ejemplo
print(parentesis_balanceados("(5 + 3) * (2 + 1)"))  # True
print(parentesis_balanceados("(5 + 3 * (2 + 1)"))   # False