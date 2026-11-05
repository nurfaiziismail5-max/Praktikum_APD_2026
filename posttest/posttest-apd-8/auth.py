"""Login dan pengecekan hak akses."""
from getpass import getpass
import data


def cek_login(username, password):
    """Mengembalikan role jika login benar, None jika salah."""
    try:
        if data.data_user[username]["password"] == data.buat_hash(password):
            return data.data_user[username]["role"]
    except KeyError:
        pass
    return None


def minta_login():
    """Meminta username dan password (password disembunyikan). Mengembalikan (username, role)."""
    username = input("Username: ")
    if username == "0":
        return "0", None
    password = input("Password: ")
    return username, cek_login(username, password)
