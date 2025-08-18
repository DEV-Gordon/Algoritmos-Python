# Encontrar Maximo comun Divisor
# es el numero mas grande que divide ambos numeros ( a y b) sin dejar residuo.

def mcd(a, b):
    while b != 0:  # Mientras el divisor no sea cero
        a, b = b, a % b  # El divisor pasa a ser el nuevo número y el residuo el nuevo divisor
    return a  # Cuando b sea 0, a es el MCD

# exec
n1, n2 = 48, 18
print(f"MCD de 48 y 18: {mcd(n1, n2)}")
