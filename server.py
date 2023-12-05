from flask import Flask, request, jsonify
from db_connection import init_sql_connection, close_sql_connection
import queries
import helpers

app = Flask(__name__)


@app.route("/users")
def users():
    cursor = init_sql_connection()
    cursor.execute(queries.get_all_users())
    result = helpers.db_users_to_json(cursor.fetchall())
    return result, 200


@app.route("/users/<id>")
def users_by_id(id=0):
    try:
        cursor = init_sql_connection()
        cursor.execute(queries.get_user_by_id(id))
        result = cursor.fetchall()
        if len(result) != 0:
            return helpers.db_users_to_json(result)
        else:
            return 'User not found', 404
    except Exception as e:
        print('Error - ', e)
        return e, 400


@app.route("/users", methods=['POST'])
def create_user():
    try:
        cursor = init_sql_connection()
        user_name = request.get_json()['user_name']
        create_sql_query = queries.create_user(user_name)
        cursor.execute(create_sql_query)
        cursor.execute(queries.last_added_user())
        return helpers.db_users_to_json(cursor.fetchall()), 200
    except:
        return 'Something went wrong', 500


@app.route("/users/<id>", methods=['PUT'])
def update_user(id):
    try:
        cursor = init_sql_connection()
        cursor.execute(queries.get_user_by_id(id))
        result = cursor.fetchall()
        user_new_name = request.get_json()['user_name']
        if len(result) != 0 and len(user_new_name) > 0:
            cursor.execute(queries.update_user_by_id(id, user_new_name))
            cursor.fetchall()
            cursor.execute(queries.get_user_by_id(id))
            new_user_bd_result = cursor.fetchall()
            return helpers.db_users_to_json(new_user_bd_result), 200
        else:
            return 'User not found or Name empty', 404
    except:
        return 'Something went wrong', 500


@app.route("/users/<id>", methods=['DELETE'])
def delete_user(id):
    try:
        cursor = init_sql_connection()
        cursor.execute(queries.get_user_by_id(id))
        result = cursor.fetchall()
        if len(result) != 0:
            cursor.execute(queries.delete_user_by_id(id))
            return id, 200
        else:
            return 'User not found', 404
    except:
        return 'Something went wrong', 500


@app.after_request
def after_request(response):
    close_sql_connection()
    return response


app.run(host='127.0.0.1', debug=True, port=3000)
