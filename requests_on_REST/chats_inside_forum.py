import pandas as pd
import psycopg2

from config_handler import get_property


def chats_inside_forum(params):
    forum_id_param = params['upper_forum_id'][0]
    connection = psycopg2.connect(user=get_property('db', 'user'),
                                  password=get_property('db', 'pass'),
                                  host=get_property('db', 'host'),
                                  port=get_property('db', 'port'),
                                  database=get_property('db', 'db_name'))
    print("Database connect successfully")
    cursor = connection.cursor()

    sql = """select chat_id from chats where upper_forum_id = %s;"""
    cursor.execute(sql, [forum_id_param])
    res = cursor.fetchall()
    results = pd.DataFrame(res, columns=['chat_id'])

    return results
