import psycopg2
from config_handler import get_property
import pandas as pd


def get_all_posts_at_forum(params):
    forum_id_param = params['forum_id'][0]
    connection = psycopg2.connect(user=get_property('db', 'user'),
                                  password=get_property('db', 'pass'),
                                  host=get_property('db', 'host'),
                                  port=get_property('db', 'port'),
                                  database=get_property('db', 'db_name'))
    print("Database connect successfully")
    cursor = connection.cursor()

    sql = """select * from posts where forum_id = %s;"""
    cursor.execute(sql, [forum_id_param])
    res = cursor.fetchall()
    results = pd.DataFrame(res, columns=['post_id', 'user_id',
                                         'forum_id', 'post_content'])

    return results
