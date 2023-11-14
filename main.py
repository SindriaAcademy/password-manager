import yaml

def load_data(file_path):
    try:
        with open(file_path, "r") as data_file:
            data = yaml.safe_load(data_file)
    except FileNotFoundError:
        print(f"Il file {file_path} non è stato trovato.")
        data = []
    return data

def view_all_credentials(data):
    for credential in data:
        print("ID:", credential["id"])
        print("Label:", credential["label"])
        print("Username:", credential["username"])
        print("Password:", credential["password"])
        print("Note:", credential["note"])
        print("-" * 20)


def main():
    file_path = "data.yml"
    data = load_data(file_path)

    if data:
        view_all_credentials(data)


if __name__ == "__main__":
    main()
