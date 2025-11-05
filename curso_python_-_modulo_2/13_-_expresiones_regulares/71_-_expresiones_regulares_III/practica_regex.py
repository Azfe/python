import re

lista_nombres = [
    "Ana María",
    "Juan Carlos",
    "María-José",
    "Luis Alberto",
    "Sandra",
    "Alex",
]

# Buscar nombres que contengan letras entre la 'o' y la 't'
for elemento in lista_nombres:
    if re.findall('[o-t]', elemento):
        print(f'Encontrado: {elemento}')
        
print('=' * 40)
# Buscar nombres que comiencen con letras entre la 'o' y la 't' (considerar mayúsculas y minúsculas)
for elemento in lista_nombres:
    if re.findall('^[o-t]', elemento, re.IGNORECASE):
        print(f'Encontrado: {elemento}')
        

    