from io import open

archivo_texto = open("archivo.txt", "r")

# texto = archivo_texto.read()

lista_lineas_texto = archivo_texto.readlines()

archivo_texto.close()

# print("Leyendo texto...", texto)

print(lista_lineas_texto)

print(lista_lineas_texto[0])