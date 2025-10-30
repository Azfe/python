def get_ciudades(*ciudades):
    for elemento in ciudades:
        # for subElemento in elemento:
            yield from elemento
        
ciudades = get_ciudades("Madrid", "Barcelona", "Bilbao", "Valencia")

print(next(ciudades))
print(next(ciudades))
print(next(ciudades))
        