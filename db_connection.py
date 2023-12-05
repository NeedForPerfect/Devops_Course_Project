import pymysql

schema_name = "my_db"
table_name = "users"
conn = None

def init_sql_connection():
    global conn
    try:
        conn = pymysql.connect(host='127.0.0.1', port=6033, user='volodymyr', password='12345', db=schema_name)
        conn.autocommit(True)
        return conn.cursor()
    except:
        print("Cannot connect to database")


def close_sql_connection():
    global conn
    try:
        conn.close()
    except Exception as e:
        print("Already closed - ", e)