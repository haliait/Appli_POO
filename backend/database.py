import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='UM6SS',
        database='hopital_bd'
    )