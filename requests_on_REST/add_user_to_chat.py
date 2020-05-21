import json

import psycopg2

from config_handler import get_property


def add_user_to_chat(body):
    connection = psycopg2.connect(user=get_property('db', 'user'),
                                  password=get_property('db', 'pass'),
                                  host=get_property('db', 'host'),
                                  port=get_property('db', 'port'),
                                  database=get_property('db', 'db_name'))
    print("Database connect successfully")
    cursor = connection.cursor()

    loaded_json = json.loads(body)
    sql = """insert into chat_permissions values (%s,%s)"""
    new_post = (loaded_json['chat_id'], loaded_json['permitted_user'])
    cursor.execute(sql, new_post)
    connection.commit()
