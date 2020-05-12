from config_handler import get_property
import pandas as pd
import psycopg2


def chats_for_user_without_forums(params):
    user_id_param = params['user_id'][0]
    connection = psycopg2.connect(user=get_property('db', 'user'),
                                  password=get_property('db', 'pass'),
                                  host=get_property('db', 'host'),
                                  port=get_property('db', 'port'),
                                  database=get_property('db', 'db_name'))
    print("Database connect successfully")
    cursor = connection.cursor()

    sql = ("""select l.permitted_user, k.chat_id from chats k \
              inner join chat_permissions l \
              on k.chat_id = l.chat_id \
              where k.upper_forum_id is null and l.permitted_user = %s;;""")
    cursor.execute(sql, [user_id_param])
    res = cursor.fetchall()

    results = pd.DataFrame(res, columns=['permitted_user', 'chat_id'])

    return results

