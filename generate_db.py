from faker import Faker
from sqlalchemy import create_engine, MetaData, Column, Numeric, Integer, Date, VARCHAR, ForeignKey
from psycopg2 import connect, sql
import sys
def establish_connection():
    try:
        connection = connect(
            dbname = "course",
            user="postgres",
            host="localhost",
            password="postgres",
            port=8014
        )
        cursor = connection.cursor()
    except Exception as err:
        cursor = None
        print ("\npsycopg2 error:", err)
    if(cursor != None):
        print ("\nconnection successful:", connection, "\n")
        return connection, cursor
    if len(sys.argv) <= 1:
            print ("Please pass a SQL string as an argument")
            
def init_db():
    connection, cursor = establish_connection()
    with open("init.sql", 'r') as file:
        try:
            cursor.execute(file.read())
            print("init.sql executed successfully")
        except: 
            print("cannot execute script")

if __name__ == "__main__":
    init_db()
