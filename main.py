#!/usr/bin/env python3

import os
import yaml
DATA_FILE = "data.yml"

def load_data():
    try:
        with open(DATA_FILE, 'r') as file:
            data = yaml.safe_load(file)
            return data if data else []
    except FileNotFoundError:
        raise FileNotFoundError(f"Il file {DATA_FILE} non è stato trovato.")

def view_all_credentials():
    data = load_data()
    for credential in data:
        print("ID:", credential["id"])
        print("Label:", credential["label"])
        print("Username:", credential["username"])
        print("Password:", credential["password"])
        print("Note:", credential["note"])
        print("-" * 20)

# Main
def main():
    view_all_credentials()


# Execute
if __name__ == "__main__":
    main()
