def validate_user(user):

    required_fields = [
        "id",
        "name",
        "username",
        "email"
    ]

    for field in required_fields:

        if not user.get(field):
            return False

    return True


def transform_users(users):

    clean_users = []

    for user in users:

        if not validate_user(user):
            print(f"Skipping invalid user: {user}")
            continue

        clean_user = {
            "id": user["id"],
            "name": user["name"].strip(),
            "username": user["username"].strip(),
            "email": user["email"].lower().strip(),
            "phone": user.get("phone"),
            "website": user.get("website"),
            "city": user.get("address", {}).get("city"),
            "company_name": user.get("company", {}).get("name")
        }

        clean_users.append(clean_user)

    return clean_users

if __name__ == "__main__":

    from extract import extract_users

    users = extract_users()

    clean_users = transform_users(users)

    print(f"Transformed {len(clean_users)} users")

    for user in clean_users:
        print(user)