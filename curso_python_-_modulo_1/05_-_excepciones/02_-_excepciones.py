def divide():
    try:        
        num1 = (float(input("Introduce el primer número: ")))
        num2 = (float(input("Introduce el segundo número: ")))
    
        print("El resultado de la división es: " + str(num1 / num2))
    except ValueError:
        print("Error: Debes introducir un número válido.")
    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero.")        
    finally:
        print("Cálculo finalizado.")  
    
divide()