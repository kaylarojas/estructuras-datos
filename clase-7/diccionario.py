estudiantes = {
    "Ana":95,
    "Luis":80,
    "Carlos":100
}

print(estudiantes["Ana"])

# agregar un nuevo estudiante
estudiantes["Maria"] = 90

#modificar
estudiantes["Ana"] = 98

# eliminar
del estudiantes["Luis"]

#buscar
if "Ana" in estudiantes:
    print("Existe")