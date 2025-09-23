# Crea un programa que pida introducir una dirección de email por teclado. 
# El programa debe imprimir en consola si la dirección de email es correcta o no en función de si esta 
# tiene el símbolo ‘@’. Si tiene una ‘@’ la dirección será correcta. Si tiene más de una o ninguna ‘@’ 
# la dirección será errónea. Si la ‘@’ está al comienzo de la dirección de email o al final, 
# la dirección también será errónea

email = input("Introduce tu email: ")

print("Email introducido:", email)

print(email.find('@'))

while(email.find('@') == -1 or email.find('@') == 0 or email.find('@') == (len(email)-1)):
    print("Tu email debe contener el siguiente formato: nombre@email.com")
    email = input("Introduce tu email: ")
    
    
print(f"{email} email correcto")