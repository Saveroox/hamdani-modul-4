def login():
    # User credentials
    username = "mahasiswa"
    password = "12345"

    # Authentication
    input_username = input("Masukkan username: ")
    input_password = input("Masukkan password: ")

    return input_username == username and input_password == password

def input_mata_kuliah():
    # Data mata kuliah dan dosen pengampuh
    mata_kuliah = input("Masukkan nama mata kuliah: ")
    dosen = input("Masukkan nama dosen pengampuh: ")

    print("Mata kuliah", mata_kuliah, "diampu oleh", dosen)

def main():
    # Authentication
    if login():
        # Input mata kuliah
        input_mata_kuliah()
    else:
        print("Login gagal.")

if __name__ == "__main__":
    main()
