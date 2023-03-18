import sqlite3
import csv

# Crear conexión

conn = sqlite3.connect('BBDD.sqlite')

# Obtener cursor
cursor = conn.cursor()

# Ejecutar sentencia de creación de tabla
cursor.execute("CREATE TABLE APARTAMENTOS(ID INTEGER(10), RESUMEN VARCHAR(50), DESCRIPCION VARCHAR(200), LOCALIZACION VARCHAR(50), FOTO VARCHAR(50), RECOMENDADO VARCHAR(50), PRECIO_EUR INTEGER(20), SUPERFICIE INTEGER(20), HABITACIONES INTEGER(10), PRECIO_M2 INTEGER(20), BANIOS INTEGER(10), NUM_FOTOS INTEGER(20), TIPO VARCHAR(50), REGION VARCHAR(50))")

with open('8_Apartments.csv', 'r', encoding='utf-8') as archivo:
    contenido = csv.reader(archivo, delimiter=',')
    next(contenido)

    for row in contenido:
        cursor.execute("INSERT INTO APARTAMENTOS VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13]))
conn.commit()

cursor.execute('SELECT ID, RESUMEN, PRECIO_EUR, NUM_FOTOS FROM APARTAMENTOS WHERE NUM_FOTOS > 20 And ID > 4 And ID < 21')
rows = cursor.fetchall()
print("Apartamentos con mas de 20 fotos:")
for row in rows:
    print(' | '.join(map(str, row)))

cursor.execute('UPDATE APARTAMENTOS SET NUM_FOTOS = 20   WHERE NUM_FOTOS < 20 And ID > 4 And ID < 21')
conn.commit()

cursor.execute('SELECT MAX(NUM_FOTOS) FROM APARTAMENTOS')
rows = cursor.fetchall()
for row in rows:
    print("Apartamento con el máximo numero de fotos: " + str(row[0]))


conn.close()
