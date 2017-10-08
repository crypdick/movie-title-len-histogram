import psycopg2
from secret_open_connection import secret_connection
conn = secret_connection()
cur = conn.cursor()

cur.execute("select * from movies limit 5;")
t = cur.fetchall()
for m in t :
    print( m[1] )
