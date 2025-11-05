import re

lista_nombres = [
    "Ana María Gómez",
    "Juan Carlos Pérez",
    "María-José Rodríguez",
    "Luis Alberto Martínez",
    "Sandra Fernández",
]

# Buscar nombres que comiencen con "Sandra"
for elemento in lista_nombres:
    if re.findall('^Sandra', elemento):
        print(f'Encontrado: {elemento}')
        
# Buscar nombres que terminen con "Martínez"
for elemento in lista_nombres:
    if re.findall('Martínez$', elemento):
        print(f'Encontrado: {elemento}')
        
lista_dominios = [
    "http://www.ejemplo.com",
    "https://subdominio.ejemplo.org",
    "ftp://ftp.ejemplo.net",
    "http://ejemplo.edu",
    "https://www.ejemplo.co.uk",
]

# Buscar dominios que sean "http" o "https" y terminen en ".com", ".org" o ".net"
for elemento in lista_dominios:
    if re.findall(r'^https?://(www\.)?ejemplo\.(com|org|net)$', elemento):
        print(f'Encontrado: {elemento}')
        
lista_personas_genero = [
    "Adulto masculino",
    "Niña",
    "Adolescente femenino",
    "Niño",
    "Mujer adulta",
    "Hombre joven",
]

# Buscar palabras que indiquen género masculino (considerar mayúsculas y minúsculas)
for elemento in lista_personas_genero:
    if re.findall(r'\b(masculino|hombre|niño)\b', elemento, re.IGNORECASE):
        print(f'Género masculino encontrado en: {elemento}')

# ===============================================
# Buscar palabras que sean "niño" o "niña" (considerar mayúsculas y minúsculas)
for elemento in lista_personas_genero:
    if re.findall(r'niñ[oa]', elemento, re.IGNORECASE):
        print(f'Encontrado: {elemento}')
    