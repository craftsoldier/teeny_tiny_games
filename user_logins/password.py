import hashlib
import sqlite3

def is_valid_credentials(cursor, u, pw):
    cursor.execute("SELECT password_hash FROM users WHERE username = ?", (u,))

    passwords = cursor.fetchone()
    return bool(passwords and passwords[0] == pw)
    
def main():
    db_file = "ppab6-test.db"

    with sqlite3.connect(db_file) as conn:
        cursor = conn.cursor()

        username = input("Enter username: ")
        password = input("Enter password: ")

        password_sha = hashlib.sha256(password.encode('utf-8')).hexdigest()

        if is_valid_credentials(cursor, username, password_sha):
            print("a dark secret")
        else:
            print("nope")

if __name__ == "__main__":
    main()

