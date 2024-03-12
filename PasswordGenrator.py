#Programmer: Ezinna Nwokenta
#Date 3.12.2024
# Program: Password Genrator
#resources: https://www.youtube.com/watch?v=jRAAaDll34Q

import hashlib

# Function to hash the password with a salt
def hash_password(password, salt):
    # Combine password and salt
    salted_password = password.encode() + salt.encode()
    # Use hashlib to create a SHA-256 hash
    hashed_password = hashlib.sha256(salted_password).hexdigest()
    return hashed_password

# Prompt the user to enter a password
password = input("Enter your password: ")

# Generate a random salt (you might want to use a different method to generate a salt)
salt = "random_salt"  # Replace "random_salt" with your actual salt

# Hash the password using the salt
hashed_password = hash_password(password, salt)

# Print the hashed password
print("Hashed password:", hashed_password)
