# Función para la compuerta AND
def and_gate(a, b):
    return a and b

# Imprimir tabla de verdad
def print_truth_table():
    print("A | B | A AND B")
    print("--|---|--------")
    for a in [0, 1]:
        for b in [0, 1]:
            result = and_gate(a, b)
            print(f"{a} | {b} |   {result}")

# Llamar a la función para imprimir la tabla de verdad
print_truth_table()