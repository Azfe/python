import sqlite3

# 1.- Crear-Abrir una conexión
# 2.- Crear puntero o cursor
# 3.- Ejecutar query(consulta SQL)
# 4.- Manejar los resultados de la query.
#     - CRUD
# 5.- Cerrar puntero o cursor
# 6.- Cerrar conexión

miConexion = sqlite3.connect("nombreBBDD.db")

miCursor = miConexion.cursor()

miCursor.execute("CREATE TABLE IF NOT EXISTS PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")

# miCursor.execute("INSERT INTO PRODUCTOS VALUES('BALON', 5, 'DEPORTES')")

variosProductos = [
    ("Camiseta", 10, "Deportes"),
    ("Jarrón", 90, "Decoración"),
    ("Camión", 20, "Juguetería"),
]

# miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)", variosProductos)

miCursor.execute("SELECT * FROM PRODUCTOS")

lista_productos = miCursor.fetchall()

# print(variosProductos)

for p in lista_productos:
    print(p)

for p in lista_productos:
    print(p[0])
    
for p in lista_productos:
    print(f"Nombre artículo: {p[0]}, sección: {p[2]}")

miConexion.commit() # Verifica los cambios de registros que se realizan en la tabla

miConexion.close()