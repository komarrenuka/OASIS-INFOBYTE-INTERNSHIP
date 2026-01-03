import random
import string

# Characters to use in the password
letters = string.ascii_letters  # a-z, A-Z
digits = string.digits          # 0-9
symbols = string.punctuation    # special characters like !@#$%

# Combine all characters
all_chars = letters + digits + symbols

# Ask user for password length
length = int(input("Enter the length of the password: "))

# Generate random password
password = "".join(random.choice(all_chars) for _ in range(length))

print("Generated password:", password)
