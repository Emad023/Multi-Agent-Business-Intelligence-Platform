from database.connection import engine

with open("database/schema.sql", "r") as f:
    sql = f.read()

statements = [
    stmt.strip()
    for stmt in sql.split(";")
    if stmt.strip()
]

with engine.begin() as conn:
    for stmt in statements:
        conn.exec_driver_sql(stmt)

print("Tables created successfully!")