import os
import yaml

"""
questa funzione carica tutte le credenziali dal file data.yml,
non richiede nessun parametro in ingresso, mentre come parametro di ritorno
restituisce una lista contenente tutte le credenziali
"""

def load_data():
    if os.path.exists("data.yml"):
        with open("data.yml", "r") as data_file:
            credentials = yaml.load(data_file, Loader=yaml.FullLoader)
            if credentials is None:
                return []
            print("Credenziali caricate con successo:")
            return credentials
    else:
        return []

"""
questa funzione consente di salvare e sovrascrivere le credenziali
# nel file data.yml, apre il file in modalità scrittura e scrive su di esso
# la credenziale che viene richiesta come parametro, questa funzione non restituisce nulla
"""
def save_credentials(credentials):
    with open("data.yml", "w") as data_file:
        yaml.dump(credentials, data_file, default_flow_style=False)

"""
questa funzione permette di modificare una credenziale, richiede come parametro 
la lista di tutte le credenziali, e l'id di quella in cui si vogliono effettuare
le modifiche, per prima cosa scorre tutta la lista fino a trovare la credenziale
corrispondente all'id dato, in seguito chiede la modifica dei campi, infine
richiama la funzione save_credentials per salvarle sul file
"""
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

    print(f"Credenziale con ID {credential_id} non trovata")

def main():

    credentials = load_data()
    print(type(credentials))

    while True:
        credential_id = input("Inserisci l'ID della credenziale da modificare (o 'exit' per uscire): ")

        if credential_id.lower() == 'exit':
            break

        try:
            credential_id = int(credential_id)
        except ValueError:
            print("L'ID deve essere un numero intero, riprova")
            continue

        edit_credential(credentials, credential_id)

if __name__ == "__main__":
    main()