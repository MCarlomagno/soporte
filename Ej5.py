import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='MySQL', db='tp3')
cur = conn.cursor()
con1 = "UPDATE personas SET Nombre = 'Julio' WHERE DNI = 39120675"
con2 = "SELECT * FROM personas WHERE DNI = 39120675"
cur.execute(con1)
cur.execute(con2)
for row in cur:
    print("DNI =", row[3], "\nNombre =", row[1],"\nFecha nacimiento =",row[2])
conn.commit()
conn.close()
