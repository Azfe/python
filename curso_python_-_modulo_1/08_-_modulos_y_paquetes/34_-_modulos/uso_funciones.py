# Dos formas de importar módulos

import funciones_matematicas

funciones_matematicas.sumar(7,5)
funciones_matematicas.restar(7,5)
funciones_matematicas.multiplicar(7,5)

from funciones_matematicas import sumar
sumar(7,5)

# Incluir todas las funciones
from funciones_matematicas import *