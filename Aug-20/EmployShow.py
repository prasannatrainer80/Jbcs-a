import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="crt"
)

cur = con.cursor()
print("Connected")
cur.execute("select * from Employ")
rows = cur.fetchall()
for row in rows:
    print(row)

con.close()