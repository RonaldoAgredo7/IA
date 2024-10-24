# Función para calcular la implicación
def implicacion(p, q):
    return not p or q

# Generar la tabla de verdad
print("p\tq\tp => q")
print("-------------------")
for p in [False, True]:
    for q in [False, True]:
        resultado = implicacion(p, q)
        print(f"{p}\t{q}\t{resultado}")


