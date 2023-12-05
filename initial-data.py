from db_connection import init_sql_connection, close_sql_connection

schema_name = "my_db"
table_name = "users"
user_names = ["Ritta", "Rebeca", "Elizabeth", "David", "Shmuel", "Abraham"]

cursor = init_sql_connection()

def add_table(table_name):
    statement_to_execute = (f"CREATE TABLE `{table_name}`"
                            f"("
                            f"`id` INT NOT NULL AUTO_INCREMENT, "
                            f"`user_name` VARCHAR(45) NOT NULL, "
                            f"`created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,"
                            f"PRIMARY KEY (`id`));"
                            f"")
    cursor.execute(statement_to_execute)

def add_user(user_name):
    statement_to_execute = f"INSERT INTO {schema_name}.{table_name} (user_name) VALUES ('{user_name}');"
    cursor.execute(statement_to_execute)


add_table(table_name)

for user_name in user_names:
    add_user(user_name)


close_sql_connection()
