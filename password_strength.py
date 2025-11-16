def check_password(password):
    if len(password)<8:
        return False
    elif not any(char.isdigit() for char in password):
        return False
    elif not any(char.islower() for char in password):
        return False
    elif not any(char.isupper() for char in password):
        return False
    elif not any(char in '!@#$%^&*()_+' for char in password):
        return False
    return True

print(check_password("WEAK"))
print(check_password("Str0ngPwd!"))