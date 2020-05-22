import json

import psycopg2

from config_handler import get_property


def delete_note(body):
    connection = psycopg2.connect(user=get_property('db', 'user'),
                                  password=get_property('db', 'pass'),
                                  host=get_property('db', 'host'),
                                  port=get_property('db', 'port'),
                                  database=get_property('db', 'db_name'))
    print("Database connect successfully")
    cursor = connection.cursor()
    sql = """delete from notes where note_id=%s;"""

    loaded_json = json.loads(body)
    del_id = [loaded_json['note_id']]
    # print(del_id)
    cursor.execute(sql, del_id)
    connection.commit()
    return del_id
