import json

import psycopg2

from config_handler import get_property


def add_new_post(body):
    connection = psycopg2.connect(user=get_property('db', 'user'),
                                  password=get_property('db', 'pass'),
                                  host=get_property('db', 'host'),
                                  port=get_property('db', 'port'),
                                  database=get_property('db', 'db_name'))
    print("Database connect successfully")
    cursor = connection.cursor()
    cursor.execute("""select MAX(post_id) from posts;""")
    max_id = cursor.fetchall()
    new_id = max_id[0][0] + 1

    loaded_json = json.loads(body)
    sql = """insert into posts values (%s,%s,%s,%s)"""
    new_post = (new_id, loaded_json['owner_id'], loaded_json['chat_id'],
                loaded_json['post_content'])
    cursor.execute(sql, new_post)
    connection.commit()
