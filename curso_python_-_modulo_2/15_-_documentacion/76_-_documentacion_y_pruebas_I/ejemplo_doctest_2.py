import doctest

def validar_email(email):
    """
    Valida si el email proporcionado es válido.
    Si tiene una @ es correcto.
    Si tiene más de una @ es incorrecto.
    Si la @ está al final es incorrecto.
    
    >>> validar_email('azfe@email.com')
    True
    
    >>> validar_email('azfeemail.com')
    False
    
    >>> validar_email('azfe@@email.com')
    False
    
    """
    arroba = email.count('@')
    
    if arroba != 1 or email.endswith('@') == (len(email) - 1) or arroba == 0:
        return False
    else:
        return True

doctest.testmod()



