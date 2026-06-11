def binarios(cadena, longitud):

    if len(cadena) == longitud:
        print(cadena)
        return

    binarios(cadena + "0", longitud)
    binarios(cadena + "1", longitud)

binarios("", 3)