from io import open

archivo_texto = open("archivo.txt", "w")

frase = "Estupendo día para estudiar Python \n el miércoles"

archivo_texto.write(frase)

archivo_texto.close()