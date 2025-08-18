# Verificar numero Primo.
# 2,3,5,7,11...
# Numero primo es aquel que se divide entre 1 y el mismo.

def es_primo(n):
    if n < 2: # se evitan los numeros menores a 2 porque no son primos
        return False
    
    for i in range(2, int(n**0.5) + 1): # revisamos solo hasta la raiz cuadrada de n
        if n % i == 0:  # si encontramos un divisor, no es primo
            return False
    return True

# exec
numero = 10
print(f"es {numero} un numero primo?:", es_primo(numero))
