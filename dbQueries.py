schema_name = "my_db"
table_name = "users"

def get_all_users():
    return f"SELECT * FROM `{table_name}`;"

def get_user_by_id(id):
    return f"SELECT id, user_name FROM `{table_name}` WHERE id = {id};"

