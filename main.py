import yaml

def load_credentials(filename):
    with open(filename, "r") as file:
        credentials = list(yaml.load_all(file, Loader=yaml.FullLoader))
    return credentials

def login(username, password, credentials):
    for user_info in credentials:
        stored_username = str(user_info.get("username", "")).strip()
        stored_password = str(user_info.get("password", "")).strip()

        if stored_username == username.strip() and stored_password == password.strip():
            return True
    return False

def main():
    max_attempts = 3
    filename = "app.yml"  # Cambia questo al nome corretto del tuo file YAML
    credentials = load_credentials(filename)
    is_logged_in = False  # Aggiunta della variabile di stato del login

    while not is_logged_in:
        for attempt in range(max_attempts):
            print(f"Attempt {attempt + 1}/{max_attempts}")
            username = input("Inserisci username: ")
            password = input("Inserisci password: ")

            if login(username, password, credentials):
                full_name = next((user_info.get("fullname", "") for user_info in credentials if user_info.get("username") == username), "")
                print(f"Login avvenuto, Ciao {full_name}!")
                is_logged_in = True  # Imposta la variabile di stato del login a True
                break
            else:
                print("Login non effettuato, riprova")

        else:
            print("Raggiunti tentativi massimi, riprovare tra un po'")

    # Se l'utente è loggato, mostra le opzioni CRUD
    while is_logged_in:
        print("\nLista delle funzioni CRUD di credenziali:")
        print("1. Visualizza credenziali")
        print("2. Aggiungi nuova credenziale")
        print("3. Modifica credenziale esistente")
        print("4. Elimina credenziale")
        print("5. Esci")

        choice = input("Scegli un'opzione (1-5): ")
        if choice == "1":
            print("Visualizza credenziali: Implementazione di visualizzazione")
        elif choice == "2":
            print("Aggiungi nuova credenziale: Implementazione di aggiunta")
        elif choice == "3":
            print("Modifica credenziale esistente: Implementazione di modifica")
        elif choice == "4":
            print("Elimina credenziale: Implementazione di eliminazione")
        elif choice == "5":
            print("Uscita dal programma.")
            is_logged_in = False  # Imposta la variabile di stato del login a False per uscire dalla sessione
        else:
            print("Scelta non valida. Riprova.")



if __name__ == "__main__":
    main()
