import math
import doctest

def raiz_cuadrada(listaNumeros):
    """
    Calcula la raíz cuadrada de un número.
    La función devuelve una lista con la raíz cuadrada de los elementos numéricos pasados por parámetros en otra lista.
    
    >>> lista = []
    >>> for i in [9, 16, 25, 36, 49, 64, 81, 100]:
    ...     lista.append(i)
    >>> raiz_cuadrada(lista)
    [3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
    

    
    """
    return [math.sqrt(n) for n in listaNumeros]

doctest.testmod()

lista_numeros = [9, 16, 25, 36, 49, 64, 81, 100]

# print(raiz_cuadrada(lista_numeros))


