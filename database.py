import psycopg2

# Estableciendo la conexión
database = psycopg2.connect(
    host='localhost',
    user='postgres',
    password='12345',
    dbname='ArquiDisti'
)
