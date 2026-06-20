from db import connect_db, init_schema

conn = connect_db()
init_schema(conn)
conn.close()

print("Tables created successfully.")
