# Función para calcular la bicondicional
def bicondicional(p, q):
    return p == q

# Generar la tabla de verdad
print("p\tq\tp <=> q")
print("-------------------")
for p in [False, True]:
    for q in [False, True]:
        resultado = bicondicional(p, q)
        print(f"{p}\t{q}\t{resultado}")
