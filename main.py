#!/usr/bin/env python3
import yaml

# Main
def main():

    idToRemove = 2
    with open('data.yml') as fileLoad:
        test_list: list
        test_list = yaml.safe_load(fileLoad)
        test_list.remove(test_list[idToRemove-1])
        #print(test_list)
        i = 0
        for i in range(len(test_list)):
            #print(test_list[i]["id"])
            #print(i)
            if test_list[i]["id"] != i+1:
                test_list[i]["id"] = i+1
        print(test_list)

        with open("data.yml", "w") as fileRead:
            documents = yaml.dump(test_list, fileRead)



# Execute
if __name__ == '__main__':

    main()

"""
Scrivere un programma python3 avente un solo file denominato main.py 
e un file di configurazione denominato app.yml. 
Questo programma dovra' permettere la gestione delle credenziali di un utente 
che dovra' prima essere autenticato.

Le funzionalita' richieste sono:

Autenticazione utente
Aggiungere una nuova credenziale
Modificare una credenziale
Eliminare una credenziale
Visualizzare tutte le credenziali
Visualizzare una credenziale specifica
Le credenziali dovranno essere storate dentro un altro file yml dedicato denominato data.yml.

Ogni credenziale dovra' avere questi campi:

id
label
username
password
note
Ricorda inoltre che le configurazioni dell utente (relative all'autenticazione) 
dovranno essere:

fullname
username
password

"""