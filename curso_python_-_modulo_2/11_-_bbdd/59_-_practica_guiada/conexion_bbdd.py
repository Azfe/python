import sqlite3

miConexion = sqlite3.connect("gestionProductos.db")

miCursor = miConexion.cursor()

miCursor.execute('''
        CREATE TABLE IF NOT EXISTS PRODUCTOS (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NOMBRE_ARTICULO VARCHAR(50) UNIQUE,
            PRECIO INTEGER, 
            SECCION VARCHAR(20)
        )
''')

productos = [
    ("Camiseta", 10, "Deportes"),
    ("Camión", 20, "Juguetería"),
    ("Destornillador", 20, "Ferretería"),
    ("Jarrón", 90, "Decoración")
]

# miCursor.executemany("INSERT INTO PRODUCTOS VALUES (NULL,?,?,?)", productos)

miCursor.execute("SELECT * FROM PRODUCTOS WHERE SECCION = 'Deportes'")

lista_productos = miCursor.fetchall()

# Actualizar registros
miCursor.execute("UPDATE PRODUCTOS SET PRECIO = 15 WHERE NOMBRE_ARTICULO = 'Camiseta'")

# Eliminar registros
# miCursor.execute("DELETE FROM PRODUCTOS WHERE ID = 2")

miCursor.execute("SELECT * FROM PRODUCTOS")

lista_productos = miCursor.fetchall()

for p in lista_productos:
    print(p)


miConexion.commit() # Verifica los cambios de registros que se realizan en la tabla

miConexion.close()