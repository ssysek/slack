import json

import psycopg2

from config_handler import get_property


def send_message(body):
    connection = psycopg2.connect(user=get_property('db', 'user'),
                                  password=get_property('db', 'pass'),
                                  host=get_property('db', 'host'),
                                  port=get_property('db', 'port'),
                                  database=get_property('db', 'db_name'))
    print("Database connect successfully")
    cursor = connection.cursor()
    cursor.execute("""select MAX(mail_id) from mails;""")
    max_id = cursor.fetchall()
    new_id = max_id[0][0] + 1

    loaded_json = json.loads(body)
    sql = """insert into mails values (%s,%s,%s,%s,%s,%s)"""
    new_post = (new_id, loaded_json['fname'], loaded_json['lname'],
                loaded_json['email'], loaded_json['subject'],
                loaded_json['message'])
    cursor.execute(sql, new_post)
    connection.commit()