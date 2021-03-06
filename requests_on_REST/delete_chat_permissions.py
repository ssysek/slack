import json

import psycopg2

from config_handler import get_property


def delete_chat_permissions(body):
    connection = psycopg2.connect(user=get_property('db', 'user'),
                                  password=get_property('db', 'pass'),
                                  host=get_property('db', 'host'),
                                  port=get_property('db', 'port'),
                                  database=get_property('db', 'db_name'))
    print("Database connect successfully")
    cursor = connection.cursor()
    sql = """delete from chat_permissions where chat_id = %s \
             and permitted_user = %s;"""

    loaded_json = json.loads(body)
    del_id = [loaded_json['chat_id'], loaded_json['permitted_user']]
    cursor.execute(sql, del_id)
    connection.commit()
    return str(del_id)
