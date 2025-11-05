import doctest

def areaTriangulo(base, altura):
    
    """
    Calcula el área de un triángulo.
    
    >>> areaTriangulo(5, 3)
    ('El área del triángula es', '7.5')
    
    >>> areaTriangulo(10, 4)
    ('El área del triángula es', '20.0')
    
    >>> areaTriangulo(7, 2)
    ('El área del triángula es', '7.0')
      
    """
    
    return "El área del triángula es", str((base * altura) / 2)

# print(areaTriangulo(5, 3))

doctest.testmod()



