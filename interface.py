from faker import Faker
from rich.console import Console
from rich.table import Table
from generate_db import DBWorker

class Interface:
    def __init__(self) -> None:
        self.console = Console()
    def input_value(self,text):
        console = Console()
        console.print("[cyan] enter {}".format(text))
        return input()

    def settings(self):
        console = Console()
        
        console.print("1 - generate countries")
        console.print("2 - generate emploees")
        console.print("3 - generate items")
        console.print("4 - generate stocks")
        console.print("5 - generate organizations")
        console.print("6 - generate places")
        console.print("7 - generate positions")
        console.print("8 - generate priorities")
        console.print("9 - generate types")
        console.print("[cyan]empty[/cyan] - generate all")
        console.print("0 - exit")
    
    def inputed_values(self, db_name, host, port, user, password):
        table = Table(title="Setup:")
        table.add_column("Database name:")
        table.add_column("Host:")
        table.add_column("Port:")
        table.add_column("Username:")
        table.add_column("Password:")
        obscured = ""
        for i in password:
            obscured += "*"
        table.add_row(db_name, host, port, user, obscured)
        Console().print(table)
        
    def what_to_do(self,worker: DBWorker): 
        fake_ru, fake_en = Faker(locale="ru_RU"), Faker(locale="en_US")
        while True:
            self.settings()
            value = self.input_value("your input")
            if value == "" : 
                worker.generate()
            if value == "1":
                worker.gen_countries(fake=fake_en)
            if value == "2":
                worker.gen_emploees(fake_en=fake_en, fake_ru=fake_ru)
            if value == "3":
                worker.gen_items(fake=fake_en)
            if value == "4":
                worker.gen_stocks(fake=fake_en)
            if value == "5":
                worker.gen_organizations(fake=fake_ru)
            if value == "6":
                worker.gen_places(fake=fake_en)
            if value == "7":
                worker.gen_positions(fake_ru)
            if value == "8":
                worker.gen_priorities()
            if value == "9":
                worker.gen_types()
            if value == "0": 
                break
    def run(self):
        try:
            with open("config.txt", 'r') as config: 
                config = config.readlines()
                db_name = config[0].strip("\n")
                host = config[1].strip("\n")
                port = config[2].strip("\n")
                user = config[3].strip("\n")
                password = config[4].strip("\n")
                self.inputed_values(db_name, host, port,user,password)
                Console().print("do you want to change data? y/n")
                if input().capitalize() == "Y":
                    db_name = self.input_value("database name")
                    host = self.input_value("host name")
                    port = self.input_value("port")
                    user = self.input_value("username")
                    password = self.input_value("password")
                    with open("config.txt", "w") as config:
                        config.writelines([db_name + "\n", host + "\n", port + "\n", user + "\n", password + "\n"])
                        config.close()
                    
        except: 
            db_name = self.input_value("database name")
            host = self.input_value("host name")
            port = self.input_value("port")
            user = self.input_value("username")
            password = self.input_value("passowrd")
            with open("config.txt", "w") as config:
                config.writelines([db_name + "\n", host + "\n", port + "\n", user + "\n", password + "\n"])
                config.close()

        self.inputed_values(db_name, host, port,user,password)
    
        worker = DBWorker(db_name=db_name, user=user, host=host, port=port, password=password)
        self.what_to_do(worker=worker)
        worker.close()

        