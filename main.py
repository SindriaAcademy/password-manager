#!/user/bin/env python3

import base64
# genera un salt casuale
import yaml
import os
from cryptography.fernet import Fernet

DATA_FILE = "data.yml"


# Genera una chiave segreta per la crittografia
def generate_key():
    return Fernet.generate_key()


# Cifra una stringa con la chiave segreta
def encrypt_password(password, key):
    # oggetto che useremo per la cifratura
    cipher_suite = Fernet(key)
    encrypted_password = cipher_suite.encrypt(password.encode('utf-8'))
    return encrypted_password


# Decifra una stringa con la chiave segreta
def decrypt_password(encrypted_password, key):
    # oggetto che useremo per la cifratura

    cipher_suite = Fernet(key)
    decrypted_password = cipher_suite.decrypt(encrypted_password).decode('utf-8')
    return decrypted_password


def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            data = yaml.safe_load(file)
            return data
    else:
        return []


# Main
def main():
    # Cifratura
    # Il messaggio da cifrare è all'interno di un file:
    messaggio = load_data()

    for credential in messaggio:
        #genera key
        secret_key = generate_key()
        #prendi password
        password = credential['password']

        # cifratura
        encrypted_password = encrypt_password(password, secret_key)
        print("Password cifrata:", encrypted_password)

        # decifratura
        decrypted_password = decrypt_password(encrypted_password, secret_key)
        print("Password decifrata:", decrypted_password)

    return


# Execute
if __name__ == '__main__':
    main()
