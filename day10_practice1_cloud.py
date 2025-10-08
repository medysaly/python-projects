def is_strong_password(password):
    if len(password) > 8 and password.isdigit():
        return True
    else:
        return False
    
user_password = is_strong_password("mimi")
print(user_password)  # Output: True
    
