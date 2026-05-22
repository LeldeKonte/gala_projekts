import mysql.connector

from config import *

def get_connection():

    return mysql.connector.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )

def run_query(sql):

    conn = get_connection()

    cursor = conn.cursor(dictionary=True)

    cursor.execute(sql)

    result = cursor.fetchall()

    conn.close()

    return result