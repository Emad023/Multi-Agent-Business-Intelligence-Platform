import psycopg2

conn = psycopg2.connect(
    host="127.0.0.1",
    port=5433,
    dbname="business_intelligence",
    user="admin",
    password="admin123"
)

print("Connected successfully!")
conn.close()