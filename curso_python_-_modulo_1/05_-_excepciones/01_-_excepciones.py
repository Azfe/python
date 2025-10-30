def suma(num1, num2):
	return num1+num2

def resta(num1, num2):
	return num1-num2

def multiplica(num1, num2):
	return num1*num2

def divide(num1,num2):
    try:
        return num1/num2	
    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero")
        return "Operación no válida"	
while True:
    try:
        op1=(int(input("Introduce el primer número: ")))
        op2=(int(input("Introduce el segundo número: ")))        
        break # Salir del bucle si la conversión fue exitosa
    except ValueError as ve:
        print("Error: Debes introducir un número válido.", ve, "Inténtalo de nuevo.")        
	
operacion=input("Introduce la operación a realizar (suma,resta,multiplica,divide): ")

if operacion=="suma":
	print(suma(op1,op2))

elif operacion=="resta":
	print(resta(op1,op2))

elif operacion=="multiplica":
	print(multiplica(op1,op2))

elif operacion=="divide":
	print(divide(op1,op2))

else:
	print("Operación no contemplada")


print("Operación ejecutada. Continuación de ejecución del programa ")