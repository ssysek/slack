import json

import psycopg2

from config_handler import get_property


def create_note(body):
    connection = psycopg2.connect(user=get_property('db', 'user'),
                                  password=get_property('db', 'pass'),
                                  host=get_property('db', 'host'),
                                  port=get_property('db', 'port'),
                                  database=get_property('db', 'db_name'))
    print("Database connect successfully")
    cursor = connection.cursor()
    cursor.execute("""select MAX(note_id) from notes;""")
    max_id = cursor.fetchall()
    new_id = max_id[0][0] + 1

    loaded_json = json.loads(body)
    sql = """insert into notes values (%s, %s, %s, %s)"""
    new_note = (new_id, loaded_json['title'], loaded_json['notes_content'],
                loaded_json['owner_id'])
    cursor.execute(sql, new_note)
    connection.commit()
    return_new_id = str(new_id)
    return return_new_id
