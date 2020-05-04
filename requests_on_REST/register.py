import psycopg2
from config_handler import get_property
import pandas as pd
import json


def register(body):
    connection = psycopg2.connect(user=get_property('db', 'user'),
                                  password=get_property('db', 'pass'),
                                  host=get_property('db', 'host'),
                                  port=get_property('db', 'port'),
                                  database=get_property('db', 'db_name'))
    print("Database connect successfully")
    cursor = connection.cursor()
    cursor.execute("""select MAX(user_id) from users;""")
    max_id = cursor.fetchall()
    new_id=max_id[0][0]+1

    loaded_json = json.loads(body)
    sql= """insert into users (user_id, user_name, user_surname, login, password) values (%s,%s,%s,%s,%s)"""
    new_user=(new_id,loaded_json[0]['user_name'],loaded_json[0]['user_surname'],loaded_json[0]['login'],loaded_json[0]['password'])
    cursor.execute(sql,new_user)
    connection.commit()