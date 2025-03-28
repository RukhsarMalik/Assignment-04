import hashlib

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

def login(email: str, password_to_check: str, stored_logins: dict) -> bool:

    hashed_password = hash_password(password_to_check)
    
    return stored_logins.get(email) == hashed_password

# Example usage
stored_logins = {
    "user@example.com": hash_password("securepassword123"),
    "anotheruser@test.com": hash_password("mypassword456")
}

# Testing
print(login("user@example.com", "securepassword123", stored_logins))  # True
print(login("user@example.com", "wrongpassword", stored_logins))     # False
print(login("nonexistent@test.com", "somepassword", stored_logins))   # False
