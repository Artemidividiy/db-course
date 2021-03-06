from rich.console import Console
from sqlalchemy import column
import streamlit as st
import psycopg2
import pandas as pd

select_items = "SELECT * FROM public.items;"
def select_colums(table:str):
    return f"SELECT column_name FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = N'{table}'"
class DB:
    def __init__(self) -> None:
        self.console = Console()
        self.connection, self.cursor = self.check_working()
        
    def request(self, query:str) :
        self.cursor.execute(query)
        return self.cursor.fetchall(), self.cursor.description

    def check_working(self):
        try:
            with open("config.txt", 'r') as config: 
                config = config.readlines()
                db_name = config[0].strip("\n")
                host = config[1].strip("\n")
                port = config[2].strip("\n")
                user = config[3].strip("\n")
                password = config[4].strip("\n")
                self.console.log(db_name, host, port, user, password)
                
            connection = psycopg2.connect(
                database=db_name,
                host=host, 
                port=port,
                user=user,
                password=password
            )
            cursor = connection.cursor()
                
            self.console.print("[green][\u2713][/]connection established")    
            return connection, cursor
        except Exception as e: 
            
            self.console.log("something went wrong")
            self.console.log(e)
            return "database not active or existing"

class Interface :
    def __init__(self) -> None:
        self.db = DB()
        self.console = Console()

    def gen_dict(self, keys, items):
        print("keys[0]" + str(keys[0][0]))
        print("keys[1]" + str(keys[1][0]))
        column_names = tuple([str(keys[i][0]) for i in range(len(keys))])
        for i in column_names: 
            new_item = ""
            for j in i:
                if j == "_" : new_item += " "
                else: new_item += j
            i = new_item
        target = [column_names] + items
        self.console.log(target[:20:])
        # for i in range(len(items)):
        #     for j in range(len(items[i])):
        #         target[list(target.keys())[j]].append(items[i][j])
        # self.console.log(target)
        return target

    def get_items(self, query):
        # rows = self.db.request(select_colums("items"))
        # st.write([rows[i][0] for i in range(len(rows))])
        data, columns = self.db.request(query=query)
        print(columns)
        data = self.gen_dict(columns, data)
        self.console.log(data[0])
        self.console.log(data[:20:])
        data = pd.DataFrame(data[1::], columns=data[0])
        st.dataframe(data)

    def run(self):
        st.write("# generated database:")
        query = st.text_area(label="query",value=select_items)
        st.write("result table")
        self.get_items(query)

if __name__ == "__main__":
    interface = Interface()
    interface.run()