import sqlite3

#CREAR BASE DE DATOS

#PASO 1 CONEXION y CREAR EL CURSOR



miConexion=sqlite3.connect("primerabase")  # Se crea el objeto
#PASO 1.1 - crear un cursor
cursor=miConexion.cursor()
"""
cursor.execute(
   "CREATE TABLE PRODUCTOS (ID INTEGER PRIMARY KEY AUTOINCREMENT, NOMBRE VARCHAR(25), CANTIDAD INTEGER)")
"""

#cursor.execute("INSERT INTO PRODUCTOS VALUES(NULL, 'PCP', 5, 'NO HAY OBSERVACION')")
"""
productos=[
     ('pc',5,'NO HAY OBSERVACION'),
     ('MOUSE',78,'NO HSY OBSERVACION'),
     ('PANTALLA',9,'NO HAY OBSERVACION'),
     ('FILAS',10,'NO HAY OBSERVACION'),
]


cursor.executemany("INSERT INTO PRODUCTOS VALUES(NULL,?,?,?)", productos)
"""
"""
cursor.execute("SELECT * FROM PRODUCTOS")

listaproductos=cursor.fetchall()
for producto in listaproductos:
    print("ID: ", producto[0], "Nombre: ",producto[1],"Cantidad: ")
"""

miConexion.commit()
miConexion.close()
