import sqlite3

miConexion = sqlite3.connect("gestionProductos.db")

miCursor = miConexion.cursor()

miCursor.execute('''
        CREATE TABLE IF NOT EXISTS PRODUCTOS (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NOMBRE_ARTICULO VARCHAR(50), 
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

miCursor.executemany("INSERT INTO PRODUCTOS VALUES (NULL,?,?,?)", productos)

miCursor.execute("SELECT * FROM PRODUCTOS")

lista_productos = miCursor.fetchall()

for p in lista_productos:
    print(p)

for p in lista_productos:
    print(p[0])
    
for p in lista_productos:
    print(f"Nombre artículo: {p[1]}, sección: {p[3]}")

miConexion.commit() # Verifica los cambios de registros que se realizan en la tabla

miConexion.close()