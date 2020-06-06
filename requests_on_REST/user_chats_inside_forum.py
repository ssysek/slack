import pandas as pd
import psycopg2
import json

from config_handler import get_property


def user_chats_inside_forum(params):
    upper_forum_id = params['forum'][0]
    permitted_user = params['user'][0]
    connection = psycopg2.connect(user=get_property('db', 'user'),
                                  password=get_property('db', 'pass'),
                                  host=get_property('db', 'host'),
                                  port=get_property('db', 'port'),
                                  database=get_property('db', 'db_name'))
    print("Database connect successfully")
    cursor = connection.cursor()

    sql = ("""select k.chat_id, k.chat_name, k.image from chats k \
              inner join chat_permissions l \
              on k.chat_id = l.chat_id \
              where k.upper_forum_id = %s and l.permitted_user = %s;""")
    cursor.execute(sql, [upper_forum_id, permitted_user])
    res = cursor.fetchall()

    results = pd.DataFrame(res, columns=['chat_id', 'chat_name', 'image'])
    print(results)
    return results
