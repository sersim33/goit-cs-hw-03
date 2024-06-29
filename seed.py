
import os
from faker import Faker
import psycopg2

# Function to seed users table
def seed_users(cursor, faker, num_records):
    cursor.execute("DELETE FROM tasks WHERE user_id IN (SELECT id FROM users);")
    cursor.execute("DELETE FROM users;")
    for _ in range(num_records):
        fullname = faker.name()
        email = faker.email()
        cursor.execute("INSERT INTO users (fullname, email) VALUES (%s, %s)", (fullname, email))

# Function to seed status table
def seed_status(cursor):
    cursor.execute("DELETE FROM status;")
    statuses = ['new', 'in progress', 'completed']
    for status in statuses:
        cursor.execute("INSERT INTO status (name) VALUES (%s)", (status,))

# Function to seed tasks table
def seed_tasks(cursor, faker, num_records):
    cursor.execute("SELECT id FROM users")
    user_ids = [row[0] for row in cursor.fetchall()]

    cursor.execute("SELECT id FROM status")
    status_ids = [row[0] for row in cursor.fetchall()]

    for _ in range(num_records):
        title = faker.text(max_nb_chars=100)
        description = faker.text()
        user_id = faker.random.choice(user_ids)
        status_id = faker.random.choice(status_ids)
        cursor.execute("INSERT INTO tasks (title, description, status_id, user_id) VALUES (%s, %s, %s, %s)",
                       (title, description, status_id, user_id))

try:
    # Establish database connection using environment variables
    conn = psycopg2.connect(
        host=os.getenv('DB_HOST'),
        dbname=os.getenv('DB_NAME'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD')
    )
    cursor = conn.cursor()

    # Initialize Faker for generating random data
    faker = Faker()

    # Number of records to create
    num_users = 5
    num_tasks = 10

    # Call functions to seed tables
    seed_users(cursor, faker, num_users)
    seed_status(cursor)
    seed_tasks(cursor, faker, num_tasks)

    # Commit changes to the database
    conn.commit()
    print("Tables seeded successfully!")

except psycopg2.Error as e:
    print("Error seeding tables:", e)

finally:
    if 'conn' in locals() or 'conn' in globals():
        conn.close()



