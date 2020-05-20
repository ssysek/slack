import psycopg2
from config_handler import get_property
import json


def add_user_to_forum(body):
    connection = psycopg2.connect(user=get_property('db', 'user'),
                                  password=get_property('db', 'pass'),
                                  host=get_property('db', 'host'),
                                  port=get_property('db', 'port'),
                                  database=get_property('db', 'db_name'))
    print("Database connect successfully")
    cursor = connection.cursor()

    loaded_json = json.loads(body)
    sql = """insert into permissions values (%s,%s)"""
    new_post = (loaded_json['forum_id'], loaded_json['permitted_user'])
    cursor.execute(sql, new_post)
    connection.commit()
