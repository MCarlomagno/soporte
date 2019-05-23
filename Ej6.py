import pymysql
import json

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='MySQL', db='tp3')
cur = conn.cursor()
con = "SELECT * FROM personas"
cur.execute(con)
for row in cur:
    print (json.dumps(row[0]))
    print (json.dumps(row[1]))
    #print (json.dumps(row[2])) --> da error porque date no puede convertirse a JSON
    #print (json.dumps(row[3])) --> da error porque decimal no puede convertirse a JSON
    print (json.dumps(row[4]))
    print ()
conn.close()
