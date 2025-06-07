import bcrypt

def generate_hash(password):
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return hashed.decode()

if __name__ == '__main__':
    pwd = input("Enter password to hash: ")
    print("Hashed password:", generate_hash(pwd))
