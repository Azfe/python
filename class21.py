# Recursividad en Python: Factoriales y Serie de Fibonacci

def factorial(n):
    # Caso base: si n es 0 o 1, el factorial es 1
    if n == 0 or n == 1:
        return 1
    # Caso recursivo: n * factorial de (n-1)
    else:
        return n * factorial(n - 1)

n = 5
factorial_result = factorial(n)
print(f"El factorial de {n} es: {factorial_result}")

# Serie de Fibonacci: F(n) = F(n-1) + F(n-2)
def fibonacci(n):
    # Caso base: si n es 0, la suma es 0
    if n <= 0:
        return "Debe ser un número entero positivo"
    elif n == 1:
        return 0
    # Caso base: si n es 2, la suma es 1
    elif n == 2:
        return 1
     
    a, b = 0, 1
    for _ in range(n - 2):
        a, b = b, a + b
    return b

# Llamada a la función
n = 5
result = fibonacci(n)
print(f"El número Fibonacci de {n} es: {result}")
