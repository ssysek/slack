import json

import psycopg2

from config_handler import get_property


def create_chat(body):
    connection = psycopg2.connect(user=get_property('db', 'user'),
                                  password=get_property('db', 'pass'),
                                  host=get_property('db', 'host'),
                                  port=get_property('db', 'port'),
                                  database=get_property('db', 'db_name'))
    print("Database connect successfully")
    cursor = connection.cursor()
    cursor.execute("""select MAX(chat_id) from chats;""")
    max_id = cursor.fetchall()
    chat_id = max_id[0][0] + 1

    loaded_json = json.loads(body)
    sql = """insert into chats values (%s, %s, %s, %s)"""
    new_chat = (chat_id, loaded_json['upper_forum_id'],
                loaded_json['chat_name'], loaded_json['image'])
    cursor.execute(sql, new_chat)
    connection.commit()
    return chat_id