from db_connection import init_sql_connection, close_sql_connection
import configs

schema_name = configs.DB_SCHEMA_NAME
table_name = configs.DB_TABLE_NAME
user_names = ["Ritta", "Rebeca", "Elizabeth", "David", "Shmuel", "Abraham"]

cursor = init_sql_connection()

def clear_database():
    statement_to_execute = f"DROP TABLE IF EXISTS {table_name}"
    cursor.execute(statement_to_execute)

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



clear_database()

print('Database cleared')

add_table(table_name)

print(f"Table \"{table_name}\" creates")

for user_name in user_names:
    add_user(user_name)

print(len(user_names), " - Users created")


close_sql_connection()
