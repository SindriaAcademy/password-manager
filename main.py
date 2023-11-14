#!/usr/bin/env python3
import yaml


def aggiungi_credenziale(path, newCred, new_id):
    with open(path, "r") as file:
        dati: list
        dati = yaml.safe_load(file)
        dati.append(newCred)
        with open(path, "w") as file:
            yaml.dump(dati, file)


def assegnaId(path):
    with open(path, "r") as file:
        dati: list
        dati = yaml.safe_load(file)
        newid:int
        newid = dati[len(dati)-1]["id"] + 1
        return newid
# Main


def main():
    pass



# Execute

if __name__ == '__main__':

    main()


