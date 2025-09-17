# Recursividad en Python: Factoriales y Serie de Fibonacci

# Factorial: n! = n * (n-1)! | 5! = 5 x 4 x 3 x 2 x 1
num = int(input("Ingrese un número para calcular su factorial: \n"))

def factorial(n):
    # Caso base: si n es 0 o 1, el factorial es 1
    if n == 0 or n == 1:
        return 1
    # Caso recursivo: n * factorial de (n-1)
    else:
        return n * factorial(n - 1)

factorial_result = factorial(num)
print(f"El factorial de {num} es: {factorial_result}")

# Serie de Fibonacci: F(n) = F(n-1) + F(n-2)
num = int(input("Ingrese un número para calcular su Fibonacci: \n"))

def fibonacci(n):
    # Caso base: si n es 0, la suma es 0
    if n <= 0:
        return 0
    elif n == 1:
        return 1    
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Llamada a la función
result = fibonacci(num)
print(f"El número Fibonacci de {num} es: {result}")

# Sumatoria de números naturales: S(n) = n + S(n-1)
num = int(input("Ingrese un número para calcular la sumatoria: \n"))

def sumatoria(n):
    if n == 1:
        return 1
    else:
        return n + sumatoria(n -1)
    
sumatoria_result = sumatoria(num)
print(f"La sumatoria de {num} es: {sumatoria_result}")

