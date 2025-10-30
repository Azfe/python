def evaluaEdad(edad):
    if edad<0:            
            raise ValueError("La edad no puede ser negativa")
    if edad<20:
        return "Eres joven"        
    elif edad<40:
        return "Eres joven adulto"
    elif edad<65:
        return "Eres adulto"
    elif edad<100:
        return "Eres anciano"
    
print(evaluaEdad(-15))
print(evaluaEdad(35))