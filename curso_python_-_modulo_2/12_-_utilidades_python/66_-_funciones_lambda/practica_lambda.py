def area_triangulo(base, altura):
    """Calcula el área de un triángulo dado su base y altura."""
    return (base * altura) / 2

t1 = area_triangulo(10, 5)  # Salida: 25.0
t2 = area_triangulo(7, 3)   # Salida: 10.5

print(f"Área del triángulo 1: {t1}")
print(f"Área del triángulo 2: {t2}")

# Uso de función lambda (Función anónima) para calcular el área del triángulo
area_triangulo_lambda = lambda base, altura: (base * altura) / 2

t3 = area_triangulo_lambda(10, 5)  # Salida: 25.0
print(f"Área del triángulo 3 (lambda): {t3}")

# Función lambda para elevar un número al cubo
al_cubo = lambda x: pow(x, 3)
alcubo1 = al_cubo(3)
print(f"3 al cubo es: {alcubo1}")

# Función lambda para formatear una comisión con signos de exclamación y símbolo de euro
destacar_valor = lambda comision:"¡{}! €".format(comision)

comision_Ana = destacar_valor(300)
comision_Pedro = destacar_valor(150)

print(f"Comisión de Ana: {comision_Ana}")
print(f"Comisión de Pedro: {comision_Pedro}")
