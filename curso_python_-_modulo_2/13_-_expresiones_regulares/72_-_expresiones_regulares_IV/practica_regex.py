import re

nombre1 = "Juan Pérez"
nombre2 = "Ana Gómez"
nombre3 = "Pilar Rodríguez"
nombre4 = "ana maria lopez"
nombre5 = "Ena Sánchez"
nombre6 = "Carlos Pérez"

# .match() - Busca al inicio de la cadena
if re.match("Ana", nombre4, re.IGNORECASE):
    print('Hemos encontrado el nombre.')
else:
    print('No hemos encontrado el nombre.')
    
# Buscar nombres que empiecen con "na"
if re.match(".na", nombre5, re.IGNORECASE):
    print('Hemos encontrado el nombre.')
else:
    print('No hemos encontrado el nombre.')
    
print('=' * 40)

cadena1 = "La casa es grande"
cadena2 = "455667789"
cadena3 = "a454576457"

if re.match("\d", cadena3, re.IGNORECASE):
    print('La cadena comienza con un dígito.')
else:
    print('La cadena no comienza con un dígito.')
    
# .search() - Busca en toda la cadena
if re.search("Pérez", nombre1, re.IGNORECASE):
    print('Hemos encontrado el apellido.')
else:
    print('No hemos encontrado el apellido.')