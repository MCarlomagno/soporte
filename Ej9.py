import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='MySQL', db='tp3')
cur = conn.cursor()
con = """SELECT p.IdPersonas, p.Nombre, p.DNI, p.FechaNacimiento, p.Altura, pp.Peso, pp.Fecha
    FROM personas p
    INNER JOIN personaPeso pp ON p.IdPersonas = pp.IdPersona
    WHERE p.DNI = 39120675"""
cur.execute(con)
for row in cur:
    print(row)
conn.close()
