password = input("Enter your password: ")

score = 0

# Check password length
if len(password) >= 8:
    score += 1

# Check uppercase letters
if any(char.isupper() for char in password):
    score += 1

# Check lowercase letters
if any(char.islower() for char in password):
    score += 1

# Check numbers
if any(char.isdigit() for char in password):
    score += 1

# Check special characters
if any(not char.isalnum() for char in password):
    score += 1

# Display password strength
if score <= 2:
    print("Password Strength: WEAK")
elif score <= 4:
    print("Password Strength: MEDIUM")
else:
    print("Password Strength: STRONG")