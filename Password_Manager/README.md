# Password Manager

A simple Python-based password manager that allows users to securely create and store accounts with hashed passwords. This CLI-based application uses MD5 hashing to store passwords and supports user registration and login functionality.

## Features
- **Account Creation**: Allows the creation of a new account with a username and password.
- **Login**: Users can log in using their username and password.
- **Password Hashing**: Passwords are hashed using the MD5 algorithm for storage (Note: MD5 is considered insecure for real-world applications, but it's used here for educational purposes).

## How to Use

1. **Clone the Repository**:
   First, clone the repository to your local machine:
   ```bash
   git clone https://github.com/lutherdpage/Python_Projects.git

cd Python_Projects/Password_Manager

python password_manager.py

Enter your username: my_user
Enter your password: ********
Account created successfully!

Enter your username: my_user
Enter your password: ********
Login successful!

1. Create account
2. Login
3. Exit
Enter your choice: 1
Enter your username: test_user
Enter your password: my_secure_password
Account created successfully

1. Create account
2. Login
3. Exit
Enter your choice: 2
Enter your username: test_user
Enter your password: my_secure_password
Login successful!

