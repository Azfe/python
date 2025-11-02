import re

cadena = "Mi número de teléfono es 123-456-7890 y mi correo es pepito@email.com."

texto_a_buscar = "pepito"

texto_encontrado = re.search("pepito", cadena)  # Buscar la palabra "pepito"

print(re.findall(r'\d{3}-\d{3}-\d{4}', cadena))  # Buscar número de teléfono

print(texto_encontrado.start())  # Posición inicial de la coincidencia
print(texto_encontrado.end())    # Posición final de la coincidencia
print(texto_encontrado.span())   # Tupla con posición inicial y final

cadena2 = "Mi número de teléfono es 123-456-7890 y el correo de Pepito es pepito@email.com. Pepito es mi nombre."

texto_a_buscar2 = "pepito"

print(len(re.findall(r'Pepito', cadena2)))  # Buscar todas las ocurrencias de "Pepito"
# texto_encontrado2 = re.search("Pepito", cadena2, re.IGNORECASE)  # Buscar "Pepito" sin importar mayúsculas/minúsculas

