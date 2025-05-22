correct_password = "admin123"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    password = input("Enter password: ")
    if password == correct_password:
        print("Login successful")
        break
    attempts += 1

if attempts == max_attempts:
    print("Access denied")
