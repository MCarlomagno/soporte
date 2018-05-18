import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='MySQL', db='tp3')
cur = conn.cursor()
con = """INSERT INTO personas
          VALUES (4, "Marcos", "1996-01-01", 39750186, 175)"""
cur.execute(con)
conn.commit()
conn.close()
