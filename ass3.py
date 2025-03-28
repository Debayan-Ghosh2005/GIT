def is_valid_password(password):
    # Condition 1: Check length
    if 8 <= len(password) <= 32:
        # Condition 2: Check if it starts with an uppercase or lowercase letter
        if password[0].isalpha():
            # Condition 3: Check for disallowed characters
            disallowed_chars = "/\\='\" "
            if not any(char in disallowed_chars for char in password):
                # Condition 4: Check for spaces
                if ' ' not in password:
                    # All conditions satisfied, return True
                    return True

    # If any condition is not satisfied, return False
    return False

# Taking user input for the password
password = input("")

# Checking and printing the result
result = is_valid_password(password)
print(result)
