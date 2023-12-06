import requests
from db_connection import init_sql_connection, close_sql_connection
import json
import helpers
import queries

# Creates DB with initial data
import initial_data

users_url = "http://127.0.0.1:3000/users"

payload = {"user_name": "Ana Kirstein"}
headers = {"Content-Type": "application/json"}

create_response = requests.request(method="POST", url=users_url, json=payload)
status_code = create_response.status_code
created_user_result = create_response.text
created_user = json.loads(created_user_result)

print(f"User {created_user["user_name"]} created successfully")

get_user_by_id_url = f"{users_url}/{created_user["id"]}"
get_user_response = requests.request(method="GET", url=get_user_by_id_url)
received_user_by_id = json.loads(get_user_response.text)



if (created_user["id"] == received_user_by_id["id"] and
        created_user["user_name"] == received_user_by_id["user_name"]):
    print("New created user - ", received_user_by_id["user_name"], "returned from API successfully.")
else:
    print("Created user doesn't exist by create response ID")


cursor = init_sql_connection()
cursor.execute(queries.get_user_by_id(created_user["id"]))
result = cursor.fetchall()

user_from_data_base = json.loads(helpers.db_users_to_json(result))

if (user_from_data_base["id"] == created_user["id"] and
        user_from_data_base["user_name"] == created_user["user_name"]):
    print("New created user - ", created_user["user_name"], "exists in data-base.")
else:
    print("New created user for some reasons doesn't exist in data-base")







