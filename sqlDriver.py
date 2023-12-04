import pymysql

schema_name = "my_db"
table_name = "users"


def init_sql_connection():
    # Establishing a connection to DB
    conn = pymysql.connect(host='127.0.0.1', port=6033, user='volodymyr', password='12345', db=schema_name)
    conn.autocommit(True)

    # Getting a cursor from Database
    return conn.cursor()