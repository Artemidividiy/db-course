import json
import datetime
from flask import Flask, make_response
from psycopg2 import connect
app = Flask(__name__)
from rich.console import Console
@app.route("/<param>/<int:id>", methods=["GET"])
def param_by_id(param: str, id: int): 
    try:
            with open("config.txt", 'r') as config: 
                config = config.readlines()
                db_name = config[0].strip("\n")
                host = config[1].strip("\n")
                port = config[2].strip("\n")
                user = config[3].strip("\n")
                password = config[4].strip("\n")
                Console().print(db_name, host, port)
                query = 'Select * from public.{0} where id = {1};'.format(param, id)
                connection, cursor = establish_connection(db_name=db_name, host=host, port=port, user=user, password=password)
                Console().print(cursor)
                cursor.execute(query)
                # Console().print(cursor.fetchall())
                data = cursor.fetchall()
                data = {"data": data, "requested_at": str(datetime.datetime.now())}
                Console().print(data)
                resp = make_response(json.dumps(data))
                resp.headers["Content-Type"] = "application/json"
                return resp
    except:
        return "Cannot access config file"
        

@app.route("/<param>", methods=["GET"])
def all_param_values(param: str):
    
    try:
            with open("config.txt", 'r') as config: 
                config = config.readlines()
                db_name = config[0].strip("\n")
                host = config[1].strip("\n")
                port = config[2].strip("\n")
                user = config[3].strip("\n")
                password = config[4].strip("\n")
                Console().print(db_name, host, port)
                query = 'Select * from public.{0};'.format(param, id)
                connection, cursor = establish_connection(db_name=db_name, host=host, port=port, user=user, password=password)
                Console().print(cursor)
                cursor.execute(query)
                # Console().print(cursor.fetchall())
                data = cursor.fetchall()
                Console().print(data)
                data = {"data": data, "requested_at": datetime.datetime.now()}
                resp = make_response(json.dumps(data))
                resp.headers["Content-Type"] = "application/json"
                return resp
    except: 
        return "Cannot access config file"

def establish_connection(db_name, user, host, password, port):
        try:
            connection = connect(
                dbname = db_name,
                user=user,
                host=host,
                password=password,
                port=port
            )
            cursor = connection.cursor()
            Console().print(cursor)
        except Exception as err:
            cursor = None
            Console().log ("\npsycopg2 error:", err)
        if(cursor != None):
            Console().log ("\nconnection successful:", connection, "\n")
            return connection, cursor

if __name__ == "__main__":
    app.run()
            