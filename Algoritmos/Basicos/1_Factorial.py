# Metodo Factorial
# n! = n * ( n - 1 ) * ( n - 2 ) ....1
# Multiplicar numeros que hay entre n y el 1

# Consiste en repetir un bloque usando un bucle hasta alcanzar una condicion de alto.

def factorial(n):
    resultado = 1
    for i in range(1, n+1 ): # ciclo que multiplica desde 1 hasta n
        resultado*=i  # resultado = resultado * i
    return resultado

#Output de ejemplo 5

#resultado = 1
#resultado = 1*1 = 1
#resultado = 1*2 = 2
#resultado = 2*3 = 6
#resultado = 6*4 = 24
#resultado = 24*5 = 120

# exec
numero = 5
print(f"Factorial de {numero}: ", factorial(numero))
