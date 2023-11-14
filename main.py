import yaml

def aggiungi_credenziale(path, newCred):
    with open(path, "r") as file:
        dati: list
        dati = yaml.safe_load(file)
        print (dati)
        dati["credenziali"].append(newCred)

        with open(path, "w") as file:
            yaml.dump(dati, file)

def main():
    file_path = "data.yml"
    nuova_credenziale = {
        "username"
    }
    aggiungi_credenziale()
# new_id
# new_label = input("scrivi un nuovo label")
# new_username = input("scrivi un nuovo username")
# new_password = input("scrivi una nuova password")
# new_note = input("scrivi nuove note")
# path = "data.yml"
# newCred = {
#     "id" : ""
#     "label" : "new_label"
#     "username": "new_username"
#     "password": "new_password"
#     "note": "new_note"
# }