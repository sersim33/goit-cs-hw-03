
import os
import psycopg2

# SQL queries to create tables
create_users_table = """
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    fullname VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE
)
"""

create_status_table = """
CREATE TABLE IF NOT EXISTS status (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE
)
"""

create_tasks_table = """
CREATE TABLE IF NOT EXISTS tasks (
    id SERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    status_id INTEGER NOT NULL REFERENCES status(id),
    user_id INTEGER NOT NULL REFERENCES users(id)
)
"""

try:
    # Establish connection to PostgreSQL using environment variables
    conn = psycopg2.connect(
        host=os.getenv('DB_HOST'),
        dbname=os.getenv('DB_NAME'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD')
    )
    cursor = conn.cursor()

    # Execute SQL queries to create tables
    cursor.execute(create_users_table)
    cursor.execute(create_status_table)
    cursor.execute(create_tasks_table)

    # Commit changes
    conn.commit()
    print("Tables created successfully!")

except psycopg2.Error as e:
    print("Error creating tables:", e)

finally:
    # Close connection
    if conn is not None:
        conn.close()
