from rich.console import Console
from sqlalchemy import column
import streamlit as st
import psycopg2
import pandas as pd
from matplotlib import pyplot as plt

select_items = open("./запросы/s2.sql", 'r').read()
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
        return target

    def get_items(self, query):
        data, columns = self.db.request(query=query)
        print(columns)
        data = self.gen_dict(columns, data)
        # self.console.log(data[0])
        # self.console.log(data[:20:])
        data = pd.DataFrame(data[1::], columns=data[0])
        st.dataframe(data)

    def run(self):
        st.write("# generated database:")
        query = st.text_area(label="query",value=select_items)
        st.write("result table")
        self.get_items(query)
        # self.display_plots(query=query)

    def display_plots(self, query):
        st.write("## displayed plots:")
        data, columns = self.db.request(query=query)
        target = dict()
        for i in data: 
            if i[3] not in target: target[i[3]] = 1
            else : target[i[3]] += 1 
        # self.console.log(list(target.keys()))
        fig1, ax1 = plt.subplots()
        self.console.log("target", target)
        ax1.pie(list(target.values()), labels=list(target.keys()), autopct='%1.1f%%')
        st.pyplot(fig1)
if __name__ == "__main__":
    interface = Interface()
    interface.run()