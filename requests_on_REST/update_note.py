import json

import psycopg2

from config_handler import get_property


def update_note(body):
    connection = psycopg2.connect(user=get_property('db', 'user'),
                                  password=get_property('db', 'pass'),
                                  host=get_property('db', 'host'),
                                  port=get_property('db', 'port'),
                                  database=get_property('db', 'db_name'))
    print("Database connect successfully")
    cursor = connection.cursor()
    sql = """update notes set title = %s, notes_content = %s \
    where note_id=%s;"""

    loaded_json = json.loads(body)
    updated_note = [loaded_json['title'], loaded_json['notes_content'],
                    loaded_json['note_id']]
    print(updated_note)
    cursor.execute(sql, updated_note)
    connection.commit()
