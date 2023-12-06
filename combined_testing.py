import requests
from db_connection import init_sql_connection, close_sql_connection
import json
import helpers
import queries
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import configs

# RESET DATA_BASE
import initial_data

# CREATE USER
users_url = f"http://{configs.API_HOST}:{configs.API_PORT}/users"

payload = {"user_name": "Ana Kirstein"}
headers = {"Content-Type": "application/json"}

create_response = requests.request(method="POST", url=users_url, json=payload)
status_code = create_response.status_code
created_user_result = create_response.text
created_user = json.loads(created_user_result)

if (create_response.status_code == 200):
    print(f"User {created_user["user_name"]} created successfully")
else:
    raise Exception("User hasn't created successfully")

# TRY TO GET NEW CREATED USER FROM API
get_user_by_id_url = f"{users_url}/{created_user["id"]}"
get_user_response = requests.request(method="GET", url=get_user_by_id_url)
received_user_by_id = json.loads(get_user_response.text)

if (created_user["id"] == received_user_by_id["id"] and
        created_user["user_name"] == received_user_by_id["user_name"]):
    print("New created user - ", received_user_by_id["user_name"], "returned from API successfully.")
else:
    raise Exception("Created user doesn't exist by create response ID")

# CHECK CREATED USER EXISTS IN DATA-BASE
cursor = init_sql_connection()
cursor.execute(queries.get_user_by_id(created_user["id"]))
result = cursor.fetchall()

user_from_data_base = json.loads(helpers.db_users_to_json(result))

if (user_from_data_base["id"] == created_user["id"] and
        user_from_data_base["user_name"] == created_user["user_name"]):
    print("New created user - ", created_user["user_name"], "exists in data-base.")
else:
    raise Exception("New created user for some reasons doesn't exist in data-base")


# CHECK USER SHOWN IN UI
chromeDriver = webdriver.Chrome()

print(f"http://{configs.FRONT_END_URL}/users/{created_user["id"]}")

chromeDriver.get(f"{configs.FRONT_END_URL}/edit-user/{created_user["id"]}")
chromeDriver.implicitly_wait(1)

user_name_from_UI = chromeDriver.find_element(By.ID, value="edit-user-input").get_attribute("value")

if (user_name_from_UI == created_user["user_name"]):
    print("Created user shown in UI")
else:
    raise Exception("Created user isn't shown if UI")