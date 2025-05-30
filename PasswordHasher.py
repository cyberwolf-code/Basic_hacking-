import hashlib

def hash_password(password):
    md5_hash = hashlib.md5(password.encode()).hexdigest()
    sha256_hash = hashlib.sha256(password.encode()).hexdigest()

    print(f"MD5:    {md5_hash}")
    print(f"SHA256: {sha256_hash}")

if __name__ == "__main__":
    pwd = input("Enter password to hash: ")
    hash_password(pwd)
