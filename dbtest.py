import psycopg2
import os

conn = psycopg2.connect(os.environ['DATABASE_URL'])
with conn.cursor() as curs:
    curs.execute('SELECT * FROM color')
    for row in curs:
        print(row)
conn.close()