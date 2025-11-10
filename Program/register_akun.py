import questionary as qs
from fungsi import clear_terminal


# Fungsi Register Yang Mengambilakan Nilai berupa hak user dan username
# Selain itu Keluar dari Program
def register(penyimpanan_akun: dict) -> dict:
    while True:
        pilihan = qs.select("", ["Register", "Login", "Keluar"]).ask()
        match pilihan:

            case "Register":
                username = input("Input Username : ")
                password = input("Input Password : ")
                if password == "" or username == "":
                    clear_terminal()
                    print("Password atau Username Tidak Boleh Kosong")
                    continue
                if username in penyimpanan_akun:
                    clear_terminal()
                    print(f"Username {username} Telah Terpakai")
                    continue
                else:
                    penyimpanan_akun[username] = [password, "user"]
                    print("Akun Berhasil Di Buat")
                    continue

            case "Login":
                username = input("Input Username : ")
                password = input("Input Password : ")
                if (
                    username in penyimpanan_akun
                    and password == penyimpanan_akun[username][0]
                ):
                    if penyimpanan_akun[username][1] == "admin":
                        return username
                    else:
                        return username

            case "Keluar":
                return "Keluar"
