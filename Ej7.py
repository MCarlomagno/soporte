import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='MySQL', db='tp3')
cur = conn.cursor()
con = """CREATE TABLE personaPeso
    (IdPeso INT NOT NULL,
    IdPersona INT NOT NULL,
    Fecha DATE NOT NULL,
    Peso INT NOT NULL,
    PRIMARY KEY (IdPeso),
    FOREIGN KEY (IdPersona) REFERENCES personas (IdPersonas));"""
cur.execute(con)
conn.commit()
conn.close()
