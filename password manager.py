import hashlib
import getpass

password_manager = {}

def create_account():
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")
    hashed_password = hashlib.md5(password.encode()).hexdigest()
    password_manager[username] = password
    print("Account created successfully")

    def login():
        username = input("Enter your username: ")
        password = getpass.getpass("Enter your password: ")
        hashed_passwordpassword = hashlib.md5(password.encode()).hexdigest()
        if password_manager[username] == password:
            print("Login successful")
        else:
            print("Login failed")




def main():
    while True:
        print("1. Create account")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            create_account()
        elif choice == "2":
            login()
        elif choice == "3":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()

    