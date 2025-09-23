from io import open

# Crear y escribir en el archivo
archivo_texto = open("archivo.txt", "w", encoding="utf-8")
archivo_texto.write("Este es el contenido del archivo.")
archivo_texto.close()

# Leer el archivo
archivo_texto = open("archivo.txt", "r", encoding="utf-8")
texto = archivo_texto.read()

# Volver al inicio del archivo para leer otra vez
archivo_texto.seek(0)
texto_segunda_vez = archivo_texto.read()

archivo_texto.close()

print("Leyendo texto...", texto)
print("Leyendo texto segunda vez...", texto_segunda_vez)