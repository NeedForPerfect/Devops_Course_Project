from flask import Flask
from sqlDriver import init_sql_connection
import dbQueries
import helpers

app = Flask(__name__)

cursor = init_sql_connection()

@app.route("/users")
def users():
    cursor.execute(dbQueries.get_all_users())
    result = helpers.db_users_to_json(cursor.fetchall())
    return result, 200

@app.route("/users/<id>")
def users_by_id(id = 0):
    try:
        cursor.execute(dbQueries.get_user_by_id(id))
        result = helpers.db_users_to_json(cursor.fetchall())
        if len(result) == 0:
            return 'User not found', 404
        else:
            return result, 200
    except Exception as e:
        return e, 400

@app.route("/users", methods=['POST'])
def create_user(id = 0):
    cursor.execute(dbQueries.get_user_by_id(id))
    result = helpers.db_users_to_json(cursor.fetchall())
    return result, 200

app.run(host='127.0.0.1', debug=True, port=3000)