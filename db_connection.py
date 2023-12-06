import pymysql
import configs

conn = None

def init_sql_connection():
    global conn
    try:
        conn = pymysql.connect(
            host=configs.DB_HOST,
            port=configs.DB_PORT,
            user=configs.DB_USER,
            password=configs.DB_PASSWORD,
            db=configs.DB_SCHEMA_NAME
        )
        conn.autocommit(True)
        return conn.cursor()
    except:
        print("Cannot connect to database")


def close_sql_connection():
    global conn
    try:
        conn.close()
    except Exception as e:
        print("DB connection closed - ", e)