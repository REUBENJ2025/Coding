import bcrypt

def hash_password(plain_password: str) -> str:
    """Hash a password for storing."""
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(plain_password.encode('utf-8'), salt)
    return hashed.decode('utf-8')

def check_password(plain_password: str, hashed_password: str) -> bool:
    """Check a plain password against the hashed version."""
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))

# Example usage
if __name__ == "__main__":

    password = "my_secure_password"
    hashed = hash_password(password)
    print(f"Hashed password: {hashed}")

    is_correct = check_password("my_secure_password", hashed)
    print(f"Password is correct: {is_correct}")

    is_incorrect = check_password("wrong_password", hashed)
    print(f"Password is correct: {is_incorrect}")

    