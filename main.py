#!/usr/bin/env python3

import yaml
import os

DATA_FILE = "data.yml"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            data = yaml.safe_load(file)
            return data
    else:
        return []

def find_entity(data, field, value):
    for entity in data:
        if entity.get(field) == value:
            return entity
    raise ValueError("Entità non trovata")

def view_specific_credential():
    try:
        credential_id = int(input("Inserisci l'ID della credenziale da visualizzare: "))
        data = load_data()

        credential = find_entity(data, 'id', credential_id)
        print(f"ID: {credential['id']}, Label: {credential['label']}, Username: {credential['username']}, Password: {credential['password']}, Note: {credential['note']}")
    except ValueError as ve:
        print(ve)
    except Exception as e:
        print(f"Errore sconosciuto durante la visualizzazione della credenziale: {e}")

# Main
def main():
    while True:
        print("\nMenu:")
        print("1. Visualizza una credenziale specifica")
        print("0. Esci")

        choice = input("Inserisci la tua scelta: ")

        if choice == '1':
            view_specific_credential()
        elif choice == '0':
            print("Arrivederci!")
            break
        else:
            print("Scelta non valida. Riprova.")

# Execute

if __name__ == "__main__":
    main()
