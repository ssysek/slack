import json
import logging

import psycopg2

from config_handler import get_property


def get_all_users():
    try:
        conn = psycopg2.connect(database=get_property('db', 'db_name'),
                                user=get_property('db', 'user'),
                                password=get_property('db', 'pass'),
                                host=get_property('db', 'host'),
                                port=get_property('db', 'port'))
        print("Database connect successfully")

        cur = conn.cursor()
        cur.execute("""select * from users;""")
        rows = cur.fetchall()

        users = []

        for data in rows:
            user = {'user_id': data[0], 'user_name': data[1],
                    'user_surname': data[2], 'login': data[4],
                    'password': data[3], 'email': data[4]}
            users.append(user)

        conn.close()
        return json.dumps(users)

    except:
        print(logging.error("Failure"))
