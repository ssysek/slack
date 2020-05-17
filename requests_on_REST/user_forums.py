import psycopg2
from config_handler import get_property
import pandas as pd


def user_forums(params):
    user_id_param = params['permitted_user'][0]
    connection = psycopg2.connect(user=get_property('db', 'user'),
                                  password=get_property('db', 'pass'),
                                  host=get_property('db', 'host'),
                                  port=get_property('db', 'port'),
                                  database=get_property('db', 'db_name'))
    print("Database connect successfully")
    cursor = connection.cursor()

    sql = """select k.* from forum_names k \
    inner join permissions l on k.forum_id = l.forum_id \
    where l.permitted_user = %s;"""
    cursor.execute(sql, [user_id_param])
    res = cursor.fetchall()
    results = pd.DataFrame(res, columns=['forum_id', 'forum_name', 'image'])

    return results
