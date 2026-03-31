from db import get_connection

# CREATE
def create_user(name, age):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO users (name, age) VALUES (%s, %s)",
        (name, age)
    )
    conn.commit()
    cur.close()
    conn.close()

# READ
def get_users():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users")
    rows = cur.fetchall()

    users = []
    for row in rows:
        user = {
            "id": row[0],
            "name": row[1],
            "age": row[2]
        }
        users.append(user)

    cur.close()
    conn.close()
    return users

#UPDATE
def update_user(user_id, name, age):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "UPDATE users SET name=%s, age=%s WHERE id=%s",
        (name, age, user_id)
    )
    conn.commit()
    cur.close()
    conn.close()

#DELETE
def delete_user(user_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "DELETE FROM users WHERE id=%s",
        (user_id,)
    )
    conn.commit()
    cur.close()
    conn.close()

# 👇 THIS MUST BE AT THE BOTTOM
if __name__ == "__main__":
    users = get_users()
    print("Before delete:")
    for user in users:
        print(user)

    delete_user(1)

    users = get_users()
    print("\nAfter delete:")
    for user in users:
        print(user)