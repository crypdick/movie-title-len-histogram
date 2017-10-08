import psycopg2
from secret_open_connection import secret_connection
conn = secret_connection()
cur = conn.cursor()

cur.execute("select length(title) from movies limit 5;")
t = cur.fetchall()
for m in t :
    print( m )
