import configs

table_name = configs.DB_TABLE_NAME

def get_all_users():
    return f"SELECT * FROM `{table_name}`;"

def get_user_by_id(id):
    return f"SELECT * FROM `{table_name}` WHERE id = {id};"

def last_added_user():
    return f"SELECT * FROM `{table_name}` WHERE id = LAST_INSERT_ID();"

def create_user(name):
    return f"INSERT INTO {table_name} (user_name) VALUES ('{name}');"

def update_user_by_id(user_id, new_name):
    return f"UPDATE {table_name} SET user_name = '{new_name}' WHERE id = {user_id};"

def delete_user_by_id(user_id):
    return f"DELETE FROM {table_name} WHERE id = {user_id};"

