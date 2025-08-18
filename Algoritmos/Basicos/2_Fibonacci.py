# Secuencia Fibonacci
# 0,1,1,2,3,5,8,13...
# Cada numero es la suma de los dos anteriores

def fibonacci(n):
    a = 0
    b = 1 
    # dos primeros numeros de la secuencia
    secuencia = [] # array para guardar numeros generados

    for i in range (n): # el for se repetira las veces que n diga
        secuencia.append(a) # se guarda el numero actual
        a, b = b, a+b # a pasa a tener el valor de b y b, la suma de a y b. es un intercambio en la misma linea para que b reciba el valor viejo de a
    return secuencia # trae la lista de numeros

# exec
numero = 10
print(f"Los primeros {numero} numeros de secuencia fibonnaci son: ", fibonacci(numero))
