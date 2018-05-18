import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='MySQL', db='tp3')
cur = conn.cursor()
con = """DELETE FROM personas WHERE DNI = 11"""
cur.execute(con)
conn.commit()
conn.close()
