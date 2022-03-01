# Exercise 1 - recursion


def recur_factorial(n):
    if n == 1:
        return n
    return n * recur_factorial(n - 1)


# Testing with 5 = 5 * 4 * 3 * 2 * 1 = 120
print(f"5! = {recur_factorial(5)}")


# Exercise 2 - Hash functions
# a
def truncation_hash(key):
    key_to_string = str(key)
    hash_value = ""
    count = 1
    for char in key_to_string:
        if count % 3 == 0 or count % 5 == 0:
            hash_value += char
        count += 1
    return hash_value


my_key = 94283641911
hashed_key = truncation_hash(my_key)
print(f"{my_key} hashed to {hashed_key}")


# b
def string_hash(key):
    hash_value = 1
    for char in key:
        hash_value *= ord(char)

    return hash_value


my_key = "hello"
hashed_key = string_hash(my_key)
print(f"{my_key} string hashed to {hashed_key}")

# Exercise 3
import hashlib as h1


class PasswordDatabase:
    def __init__(self):
        self.passwords = {}

    def get_login(self):
        username = input("Enter username: ")
        password = h1.sha1(input("Enter password: ").encode()).hexdigest()
        return username, password

    def create_user(self):
        username, password = self.get_login()
        self.passwords[username] = password
        print(f"User {username} created!")

    def check_password(self, username, password):
        if self.passwords[username] == password:
            return True
        return False

    def update_password(self):
        username, password = self.get_login()
        login_is_correct = self.check_password(username, password)
        if login_is_correct:
            password = h1.sha1(input("Enter new password: ").encode()).hexdigest()
            self.passwords[username] = password
        else:
            print("Incorrect login...")


db = PasswordDatabase()
db.create_user()
print(db.passwords)
db.update_password()
print(db.passwords)
