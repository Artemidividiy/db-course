import time
from rich.console import Console
from rich.table import Table
from generate_db import DBWorker

def input_value(text):
    console = Console()
    console.print("[cyan] enter {}".format(text))
    return input()

def inputed_values(db_name, host, port, user, password):
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

if __name__ == "__main__" :
    try:
        with open("config.txt", 'r') as config: 
            config = config.readlines()
            db_name = config[0].strip("\n")
            host = config[1].strip("\n")
            port = config[2].strip("\n")
            user = config[3].strip("\n")
            password = config[4].strip("\n")
            inputed_values(db_name, host, port,user,password)
            Console().print("do you want to change data? y/n")
            if input().capitalize() == "Y":
                db_name = input_value("database name")
                host = input_value("host name")
                port = input_value("port")
                user = input_value("username")
                password = input_value("password")
                with open("config.txt", "w") as config:
                    config.writelines([db_name + "\n", host + "\n", port + "\n", user + "\n", password + "\n"])
                    config.close()
                
    except: 
        db_name = input_value("database name")
        host = input_value("host name")
        port = input_value("port")
        user = input_value("username")
        password = input_value("passowrd")
        with open("config.txt", "w") as config:
            config.writelines([db_name + "\n", host + "\n", port + "\n", user + "\n", password + "\n"])
            config.close()

    inputed_values(db_name, host, port,user,password)
    time.sleep(5)
    worker = DBWorker(db_name=db_name, user=user, host=host, port=port, password=password)
    worker.generate()
    worker.close()