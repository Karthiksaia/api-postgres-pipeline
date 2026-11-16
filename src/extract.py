import requests


API_URL = "https://jsonplaceholder.typicode.com/users"

def extract_users():

    response = requests.get(
        API_URL,
        timeout=30
    )

    response.raise_for_status()

    users = response.json()

    return users


if __name__ == "__main__":

    users = extract_users()

    print(f"Extracted {len(users)} users")

    print(users)