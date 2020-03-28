import json
from config_handler import get_property
import psycopg2
import logging


def get_all():

    try:
        connection = psycopg2.connect(user=get_property('db', 'user'),
                                      password=get_property('db', 'pass'),
                                      host=get_property('db', 'host'),
                                      port=get_property('db', 'port'),
                                      database=get_property('db', 'users_dbname'))
        cursor = connection.cursor()
        sql = "SELECT * FROM slack.users;"
        cursor.execute(sql)
        res = cursor.fetchall()
        slack_users = []

        for r in res:
            users = {'user_id': r[0], 'user_name': r[1], 'user_surname': r[2]}
            slack_users.append(users)

        return json.dumps(slack_users)

    except:
        logging.error("Database error during getting users")
