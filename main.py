from hashlib import sha256
import yaml


def hash_password(password):
    hash_password = sha256(password.encode('utf-8')).hexdigest()
    return hash_password


def check_password(hashPassword):
    with open("app.yml") as file:
        print("utente2 " + hashPassword)
        data = yaml.safe_load(file)
        return hashPassword == data["password"]


def main():
    pass


if __name__ == "__main__":
    main()