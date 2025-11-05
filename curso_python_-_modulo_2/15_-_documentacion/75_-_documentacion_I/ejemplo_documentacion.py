
class Areas:
    """Clase para calcular áreas de diferentes figuras geométricas."""
    
    
    def areaCuadrado(lado):
        """Calcula el área de un cuadrado.

        Parámetros:
        lado (float): La longitud de un lado del cuadrado.

        Retorna:
        float: El área del cuadrado.
        """
        return "El área del cuadrado es:", str(lado * lado)

    def areaTriangulo(base, altura):
        """Calcula el área de un triángulo.

        Parámetros:
        base (float): La longitud de la base del triángulo.
        altura (float): La altura del triángulo.

        Retorna:
        float: El área del triángulo.
        """
        return "El área del triángulo es:", str((base * altura) / 2)

print(Areas.areaCuadrado(5))
print(Areas.areaTriangulo(5, 3))
print(Areas.areaTriangulo.__doc__)
help(Areas.areaCuadrado)
help(Areas)