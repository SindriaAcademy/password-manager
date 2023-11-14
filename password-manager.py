import yaml
import getpass
import os


DATA_FILE = "data.yml"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            data = yaml.safe_load(file)
            return data
    else:
        return []
def view_specific_credential():
    credential_id = int(input("Inserisci l'ID della credenziale da visualizzare: "))
    data = load_data()

    for credential in data:
        if credential['id'] == credential_id:
            print(f"ID: {credential['id']}, Label: {credential['label']}, Username: {credential['username']}, Password: {credential['password']}, Note: {credential['note']}")
            return

    print("Credenziale non trovata.")


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


if __name__ == "__main__":
    main()
