import os

import psycopg2
from dotenv import load_dotenv


load_dotenv()


def get_connection():

    connection = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )

    return connection


def load_users(users):

    connection = get_connection()

    cursor = connection.cursor()

    query = """
        INSERT INTO api_users (
            id,
            name,
            username,
            email,
            phone,
            website,
            city,
            company_name
        )
        VALUES (
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s
        )
        ON CONFLICT (id)
        DO UPDATE SET
            name = EXCLUDED.name,
            username = EXCLUDED.username,
            email = EXCLUDED.email,
            phone = EXCLUDED.phone,
            website = EXCLUDED.website,
            city = EXCLUDED.city,
            company_name = EXCLUDED.company_name,
            updated_at = CURRENT_TIMESTAMP;
    """

    for user in users:

        cursor.execute(
            query,
            (
                user["id"],
                user["name"],
                user["username"],
                user["email"],
                user["phone"],
                user["website"],
                user["city"],
                user["company_name"]
            )
        )

    connection.commit()

    cursor.close()

    connection.close()