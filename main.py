import sys
import yaml

# Costanti Globali
CREDENTIALS_FILE_PATH = "app.yml"
MAX_LOGIN_ATTEMPTS = 3

def load_credentials(filename):
    try:
        with open(filename, "r") as file:
            credentials = list(yaml.load_all(file, Loader=yaml.FullLoader))
        return credentials
    except FileNotFoundError:
        print(f"Errore: File '{filename}' non trovato.")
        sys.exit()
    except Exception as e:
        print(f"Errore durante il caricamento delle credenziali: {e}")
        sys.exit()

def login(username, password, credentials):
    for user_info in credentials:
        stored_username = str(user_info.get("username", "")).strip()
        stored_password = str(user_info.get("password", "")).strip()

        if stored_username == username.strip() and stored_password == password.strip():
            return True
    return False


def perform_login():
    credentials = load_credentials(CREDENTIALS_FILE_PATH)
    is_logged_in = False
    attempts = 0

    while not is_logged_in and attempts < MAX_LOGIN_ATTEMPTS:
        print(f"Attempt {attempts + 1}/{MAX_LOGIN_ATTEMPTS}")
        username = input("Inserisci username: ")
        password = input("Inserisci password: ")

        if login(username, password, credentials):
            full_name = next((user_info.get("fullname", "") for user_info in credentials if user_info.get("username") == username), "")
            print(f"Login avvenuto, Ciao {full_name}!")
            is_logged_in = True
        else:
            print("Login non effettuato, riprova")
            attempts += 1

    if not is_logged_in:
        print("Raggiunti tentativi massimi, Riprova piu tardi coglione.")
        sys.exit()

    return credentials,  is_logged_in


def menu():
    print("\nLista delle funzioni CRUD di credenziali:")
    print("1. Visualizza credenziali")
    print("2. Aggiungi nuova credenziale")
    print("3. Modifica credenziale esistente")
    print("4. Elimina credenziale")
    print("5. Esci")

    choice = input("Scegli un'opzione (1-5): ")

    if choice == "1":
        print("Visualizza credenziali: view_all_credentials()")
    elif choice == "2":
        print("Aggiungi nuova credenziale:  aggiungi_credenziale()")
    elif choice == "3":
        print("Modifica credenziale esistente: edit_credential()")
    elif choice == "4":
        print("Elimina credenziale: Implementazione di eliminazione")
    elif choice == "5":
        print("Uscita dal programma.")
        sys.exit()

    return True

def main():
    credentials, is_logged_in = perform_login()

    while is_logged_in:
        is_logged_in = menu()

if __name__ == '__main__':
    main()
