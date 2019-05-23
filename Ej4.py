import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='MySQL', db='tp3')
cur = conn.cursor()
con = "SELECT * FROM personas WHERE DNI = 39120675"
cur.execute(con)
for row in cur:
    print("DNI =", row[3], "\nNombre =", row[1],"\nFecha nacimiento =",row[2])
conn.commit()
conn.close()
