from sqlDriver import init_sql_connection

schema_name = "my_db"
table_name = "users"
user_names = ["Ritta", "Rebeca", "Elizabeth", "David", "Shmuel", "Abraham"]

cursor = init_sql_connection()

def add_table(table_name):
    statement_to_execute = f"CREATE TABLE `{table_name}` (`id` INT NOT NULL AUTO_INCREMENT, `user_name` VARCHAR(45) NOT NULL, PRIMARY KEY (`id`));"
    cursor.execute(statement_to_execute)

def add_user(user_name):
    statement_to_execute = f"INSERT INTO {schema_name}.{table_name} (user_name) VALUES ('{user_name}');"
    cursor.execute(statement_to_execute)


add_table(table_name)

for user_name in user_names:
    add_user(user_name)


cursor.close()
