import json

import psycopg2

from config_handler import get_property


def create_forum(body):
    connection = psycopg2.connect(user=get_property('db', 'user'),
                                  password=get_property('db', 'pass'),
                                  host=get_property('db', 'host'),
                                  port=get_property('db', 'port'),
                                  database=get_property('db', 'db_name'))
    print("Database connect successfully")
    cursor = connection.cursor()
    cursor.execute("""select MAX(forum_id) from forum_names;""")
    max_id = cursor.fetchall()
    forum_id = max_id[0][0] + 1

    loaded_json = json.loads(body)
    sql = """insert into forum_names values (%s, %s, %s)"""
    new_forum = (forum_id, loaded_json['forum_name'],
                 loaded_json['image'])
    cursor.execute(sql, new_forum)
    connection.commit()
    return forum_id
