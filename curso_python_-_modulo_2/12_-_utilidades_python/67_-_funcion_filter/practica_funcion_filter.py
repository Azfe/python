def num_par(num):
    if num % 2 == 0:
        return True
    
numeros = [17, 24, 7, 39, 8, 51, 92, 11, 6]

numeros_pares = list(filter(num_par, numeros))

print(numeros_pares)  # Salida: [24, 8, 92, 6]

# Usando una función lambda
numeros_pares = list(filter(lambda numero_par: numero_par % 2 == 0, numeros))

print(numeros_pares)  # Salida: [24, 8, 92, 6]