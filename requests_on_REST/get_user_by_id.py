import psycopg2
from config_handler import get_property
import pandas as pd


def get_user_by_id_param(params):
    user_id_param = params['user_id'][0]
    connection = psycopg2.connect(user=get_property('db', 'user'),
                                  password=get_property('db', 'pass'),
                                  host=get_property('db', 'host'),
                                  port=get_property('db', 'port'),
                                  database=get_property('db', 'db_name'))
    print("Database connect successfully")
    cursor = connection.cursor()

    sql = """select * from users where user_id = %s;"""
    cursor.execute(sql, [user_id_param])
    res = cursor.fetchall()
    results = pd.DataFrame(res, columns=['user_id', 'user_name',
                                         'user_surname'])

    return results
