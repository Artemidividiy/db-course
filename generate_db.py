from datetime import datetime
from faker import Faker
from sqlalchemy import create_engine, MetaData, Column, Numeric, Integer, Date, VARCHAR, ForeignKey
from psycopg2 import connect, sql
from rich.progress import track
from rich.console import Console

class DBWorker():
    def __init__(self) -> None:
        self.console = Console()
        self.connection, self.cursor = self.establish_connection()
        self.init_db()

    def establish_connection(self):
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
            self.console.log ("\npsycopg2 error:", err)
        if(cursor != None):
            self.console.log ("\nconnection successful:", connection, "\n")
            return connection, cursor
        
    def init_db(self):
        with open("init.sql", 'r') as file:
            try:
                self.cursor.execute(sql.SQL(file.read()))
                self.console.log("init.sql executed successfully")
            except: 
                self.console.log("cannot execute script")

    def gen_countries(self, faker: Faker()):
        start_time = datetime.now()
        countries = {faker.country() for _ in range(20)}
        for i in countries:
            if "'" in i: 
                countries.discard(i)
        while len(countries) != 20 :
            added = faker.country()
            if "'" not in added:
                countries.add(added)
        for country in track(countries, description="generating countries"):
            country = "'" + country + "'"
    
            self.cursor.execute(sql.SQL('INSERT INTO public.countries("name") VALUES ({});'.format(country)))
            self.connection.commit()
            
        self.console.log("\ncountries generated successfully\n")
        self.console.log(f"time taken: {datetime.now() - start_time}")
    
    
    def close(self):
        self.cursor.close()
        self.connection.close()

if __name__ == "__main__":
    fake_en = Faker(locale="en_US")
    fake_ru = Faker(locale="ru_RU")
    worker = DBWorker()
    worker.gen_countries(faker=fake_en)
    worker.close()
