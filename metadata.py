import mysql.connector

from config import *

conn = mysql.connector.connect(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASSWORD,
    database=DB_NAME
)

cursor = conn.cursor()

cursor.execute("SHOW TABLES")

tables = cursor.fetchall()

for table in tables:

    table_name = table[0]

    print("\nTABULA:", table_name)

    cursor.execute(f"DESCRIBE {table_name}")

    columns = cursor.fetchall()

    for col in columns:

        print(col)

conn.close()