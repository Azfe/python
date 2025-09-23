nombre = input("Introduce tu nombre: \n")
print(nombre.capitalize())

edad = input("Introduce tu edad: \n")

while(edad.isdigit() == False):
    print("Por favor, introduce un valor numérico")
    
    edad = input("Introduce la edad: ")

if(int(edad) < 18):
    print("No puedes pasar")
else:
    print("Puedes pasar")
    
# upper() sube todo en mayúsculas
# lower() baja todo en minúscula
# capitalize() todas la primera letra en mayúscula
# count() contar una y cuantas aparecen dentro de una cadena
# find() representa el índice donde aparece un carácter dentro de un texto
# isdigit() devuelve un booleano si es un valor numérico o no
# isalum() comprueba si es alfanuméricos
# isalpha si es alpha comprueba si son solo letras
# split()  separa por palabras utilizando espacios
# strip() borra los espacios sobrante al principio y al final
# replace() cambia una palabra o una letra por otra
# rfind() representa el índice de un carácter contando desde atrás