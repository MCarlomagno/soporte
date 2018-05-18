import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='MySQL', db='tp3')
cur = conn.cursor()
con = "SELECT * FROM personas"
cur.execute(con)
columnas = [col[0] for col in cur.description]
print(columnas)
for row in cur:
    print(row)
conn.close()
