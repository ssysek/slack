import pandas as pd
import psycopg2

from config_handler import get_property


def read_notes(params):
    user_id_param = params['owner_id'][0]
    connection = psycopg2.connect(user=get_property('db', 'user'),
                                  password=get_property('db', 'pass'),
                                  host=get_property('db', 'host'),
                                  port=get_property('db', 'port'),
                                  database=get_property('db', 'db_name'))
    print("Database connect successfully")
    cursor = connection.cursor()

    sql = """select * from notes where owner_id = %s;"""
    cursor.execute(sql, [user_id_param])
    res = cursor.fetchall()
    results = pd.DataFrame(res, columns=['note_id', 'title',
                                         'notes_content', 'owner_id'])

    return results
