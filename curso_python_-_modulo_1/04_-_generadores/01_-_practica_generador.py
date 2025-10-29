# Generador de números pares usando una función tradicional
def genera_pares(limite):
    num = 1
    miLista = []
    
    while num <= limite:
        miLista.append(num * 2)
        num += 1
    
    return miLista

pares = genera_pares(10)
print(pares)

# Ahora con generador
def genera_pares_gen(limite):
    num = 1
    
    while num <= limite:
        yield num * 2 # yield convierte la función en un generador
        num += 1
        
pares_gen = genera_pares_gen(10)
# for numero in pares_gen:
#     print(numero)
    
# Imprime los 3 primeros elementos
print(next(pares_gen))

print("Aquí prodría ir más código...")

print(next(pares_gen))

print("Aquí prodría ir más código...")

print(next(pares_gen))
