import math

def calcula_raiz_cuadrada(num):
    
    if num < 0:
        raise ValueError("El número no puede ser negativo")
    else:
        return math.sqrt(num)
    
op1 = int(input("Introduce un número para calcular su raíz cuadrada: "))

try:
    print(calcula_raiz_cuadrada(op1))
except ValueError as ErrorNumeroNegativo:
    print("Error:", ErrorNumeroNegativo)
finally:
    print("Cálculo de raíz cuadrada finalizado.")