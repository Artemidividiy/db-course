from datetime import date, datetime
from random import randint
import random
import time
from faker import Faker
from psycopg2 import connect, sql
from rich.progress import track
from rich.console import Console
from parser import Client

class DBWorker():
    def __init__(self, db_name, user, password, host, port=5432) -> None:
        self.console = Console()
        self.connection, self.cursor = self.establish_connection(db_name=db_name, user=user, password=password, host=host, port=port)
        self.init_db()
    
    def str_time_prop(self,start, end, time_format, prop):
        stime = time.mktime(time.strptime(start, time_format))
        etime = time.mktime(time.strptime(end, time_format))
        ptime = stime + prop * (etime - stime)
        return time.strftime(time_format, time.localtime(ptime))

    def random_datetime(self,start, end, prop):
        return self.str_time_prop(start, end, '%m/%d/%Y %I:%M %p', prop)

    def random_time(self, start, end, prop):
        return self.str_time_prop(start, end, '%H:%M', prop)

    def random_date(self, start, end, prop):
        return self.str_time_prop(start, end, '%Y-%m-%d', prop)

    def establish_connection(self, db_name, user, host, password, port):
        try:
            connection = connect(
                dbname = db_name,
                user=user,
                host=host,
                password=password,
                port=port
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

    def gen_countries(self, fake: Faker()):
        start_time = datetime.now()
        countries = {fake.country() for _ in range(20)}
        for i in countries:
            if "'" in i: 
                countries.discard(i)
        while len(countries) != 20 :
            added = fake.country()
            if "'" not in added:
                countries.add(added)
        for country in track(countries, description="generating countries"):
            country = "'" + country + "'"
    
            self.cursor.execute(sql.SQL('INSERT INTO public.countries("name") VALUES ({});'.format(country)))
            self.connection.commit()
            
        self.console.log("countries generated successfully\n")
        self.console.log(f"time taken: {datetime.now() - start_time}")
    
    def gen_positions(self, fake:Faker) :
        start_time = datetime.now()
        positions = [fake.job() for i in range(15)]
        for position in track(positions, description="generating positions"):
            position = "'" + position + "'"
            self.cursor.execute(sql.SQL('INSERT INTO public.positions("name") VALUES ({});'.format(position)))
            self.connection.commit()
        self.console.log("positions generated successfully\n")
        self.console.log(f"time taken: {datetime.now() - start_time}")

    def gen_priorities(self):
        start_time = datetime.now()
        priorities = range(20)
        for priority in track(priorities, description="generating priorities"):
            self.cursor.execute(sql.SQL('insert into public.priorities("number") values ({});'.format(str(priority))))
            self.connection.commit()
        self.console.log("priorities generated successfully\n")
        self.console.log(f"time taken: {datetime.now() - start_time}")

    def gen_organizations(self, fake: Faker):
        start_time = datetime.now()
        orgs = [fake.company() for _ in range(30)]
        for org in track(orgs, description="generating organizations"):
            self.cursor.execute(sql.SQL('insert into public.organizations("name") values ({});'.format("'" + org + "'")))
            self.connection.commit()
        self.console.log("organizations generated successfully\n")
        self.console.log(f"time taken: {datetime.now() - start_time}")
    
    def gen_emploees(self, fake_en: Faker, fake_ru: Faker):
        start_time = datetime.now()
        for emploee in track(range(1000), description="generating emploees"):
            name = "'" + fake_ru.name() + "'"
            birth_year = "'" + str(self.random_datetime("1/1/2008 1:30 PM", "1/1/2009 4:50 AM", random.random())) + "'"
            position = str(randint(1,15))
            priority = str(randint(1,20))
            self.cursor.execute(sql.SQL('insert into public.emploees("name", "birth year", "position", "priority") values ({0}, {1}, {2}, {3});'.format(name, birth_year, position, priority)))
            self.connection.commit()
        self.console.log("emploees generated successfully\n")
        self.console.log(f"time taken: {datetime.now() - start_time}")
    
    def gen_places(self, fake:Faker):
        start_time = datetime.now()
        for place in track(range(40), description="generating places"):
            name = "'" + fake.company() + "'" 
            organization = randint(1, 30)
            latitude, longitude = fake.latlng()
            country = randint(1,20)
            self.cursor.execute(sql.SQL('insert into public.places("Name", "Organization", "longitude", "latitude", "Country") values ({0}, {1}, {2}, {3}, {4});'.format(name, str(organization), str(longitude), str(latitude), str(country))))
            self.connection.commit()
        self.console.log("places generated successfully\n")
        self.console.log(f"time taken: {datetime.now() - start_time}")
    
    def gen_stocks(self, fake:Faker):
        start_time = datetime.now()
        for stock in track(range(1000), description="generating stocks"):
            name = "'" + fake.company() + "'" if random.random() >= 0.5 else None
            latitude, longitude = fake.latlng()
            country = randint(1,20)
            self.cursor.execute(sql.SQL('insert into public.stocks("name", "longitude", "latitude", "country") values ({0}, {1}, {2}, {3});'.format(name if name != None else "'None'", str(longitude), str(latitude), str(country))))
            self.connection.commit()
        self.console.log("stocks generated successfully\n")
        self.console.log(f"time taken: {datetime.now() - start_time}")
    
    def gen_types(self):
        start_time = datetime.now()
        parsed_names = Client().run()
        for type in track(parsed_names, description="generating types"):
            self.cursor.execute(sql.SQL('insert into public.types("name") values ({});'.format("'" + type + "'")))
            self.connection.commit()
        self.console.log("types generated successfully\n")
        self.console.log(f"time taken: {datetime.now() - start_time}")


    def gen_items(self, fake:Faker):
        start_time = datetime.now()
        parsed_names = Client().run()
        for item in track(range(10000), description="generating items"):
            name = "'" + fake.bothify(text="Item by code: ???????-#########-?-##-??") + "'"
            arrival_time = "'" + self.random_time("0:01", "23:59", random.random()) + "'"
            arrival_date = "'" + self.random_date("2001-01-01", datetime.today().strftime('%Y-%m-%d'), random.random()) + "'"
            type = randint(1, len(parsed_names))
            stock = randint(1, 1000)
            point_of_departure = randint(1, 20)
            self.cursor.execute(sql.SQL('insert into public.items("name", "arrival_time", "arrival_date", "type", "stock", "point of departure") values ({0},{1},{2},{3},{4},{5});'.format(name, arrival_time, arrival_date, str(type), str(stock), str(point_of_departure))))
            self.connection.commit()
        self.console.log("types generated successfully\n")
        self.console.log(f"time taken: {datetime.now() - start_time}")


    def gen_emploees_stocks(self):
        start_time = datetime.now()
        for conns in track(range(1000), description="generating connections"):
            stock_id = randint(1, 1000) 
            emploee_id = randint(1, 1000)
            self.cursor.execute(sql.SQL('insert into public.emploees_stocks("stock_id", "emploee_id") values ({0}, {1});'.format(str(stock_id), str(emploee_id))))
            self.connection.commit()
        self.console.log("connections between emploees and stocks generated successfully\n")
        self.console.log(f"time taken: {datetime.now() - start_time}")

    def generate(self):
        fake_en = Faker(locale="en_US")
        fake_ru = Faker(locale="ru_RU")
        start_time = datetime.now()
        try:
            self.gen_countries(fake=fake_en)
            self.gen_positions(fake=fake_ru)
            self.gen_priorities()
            self.gen_organizations(fake=fake_ru)
            self.gen_emploees(fake_en=fake_en, fake_ru=fake_ru)
            self.gen_places(fake=fake_en)
            self.gen_stocks(fake=fake_en)
            self.gen_types()
            self.gen_items(fake=fake_en)
            self.gen_emploees_stocks()
            self.console.log("completed✅")
        except: 
            self.console.log("[bold red] something went wrong.\nPlease restart the script")
        self.console.log(f"time taken: {datetime.now() - start_time}")


    def close(self):
        self.cursor.close()
        self.connection.close()
