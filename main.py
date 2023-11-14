import os
import yaml

def load_credentials():
    if os.path.exists("data.yml"):
        with open("data.yml", "r") as data_file:
            credentials = yaml.load(data_file, Loader=yaml.FullLoader)
            if credentials is None:
                return []
            print("Credenziali caricate con successo:")
            return credentials
    else:
        return []
def save_credentials(credentials):
    with open("data.yml", "w") as data_file:
        yaml.dump(credentials, data_file, default_flow_style=False)
def edit_credential(credentials, credential_id):
    for credential in credentials:
        if credential["id"] == credential_id:
            label = input(f"Nuovo label ({credential['label']}): ")
            username = input(f"Nuovo username ({credential['username']}): ")
            password = input(f"Nuova password ({credential['password']}): ")
            note = input(f"Nuova nota ({credential['note']}): ")

            credential["label"] = label or credential["label"]
            credential["username"] = username or credential["username"]
            credential["password"] = password or credential["password"]
            credential["note"] = note
            save_credentials(credentials)
            print("Credenziale modificata con successo")
            return

    print("Credenziale con ID {credential_id} non trovata")

def main():
    credentials = load_credentials()

    credential_id = int(input("Inserisci l'ID della credenziale da modificare: "))
    edit_credential(credentials, credential_id)

if __name__ == "__main__":
    main()