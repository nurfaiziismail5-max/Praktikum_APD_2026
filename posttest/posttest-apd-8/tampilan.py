"""Semua yang berhubungan dengan tampilan (PrettyTable) dan layar."""
import os
from prettytable import PrettyTable


# Warna memakai kode ANSI bawaan terminal (tidak perlu install library)
os.system("")  # mengaktifkan kode ANSI di CMD/PowerShell Windows

HIJAU = "\033[92m"
MERAH = "\033[91m"
KUNING = "\033[93m"
RESET = "\033[0m"


def beri_warna(teks, warna):
    return warna + str(teks) + RESET


def pesan_sukses(teks):
    print(beri_warna(teks, HIJAU))


def pesan_error(teks):
    print(beri_warna(teks, MERAH))


def pesan_info(teks):
    print(beri_warna(teks, KUNING))


def bersihkan_layar():
    os.system("cls" if os.name == "nt" else "clear")


def tampil_menu(judul, menu):
    tabel = PrettyTable(["No", "Menu"])
    tabel.title = judul
    tabel.align = "l"
    for nomor in menu:
        tabel.add_row([nomor, menu[nomor]])
    print("")
    print(tabel)


def tampil_tabel(judul, kolom, data, label_no="No"):
    """Menampilkan dictionary data sebagai tabel. kolom = [(judul, kunci, satuan), ...]"""
    tabel = PrettyTable()
    tabel.title = judul
    nama_kolom = [label_no]
    for label, kunci, satuan in kolom:
        nama_kolom.append(label)
    tabel.field_names = nama_kolom
    tabel.align = "l"
    for no in data:
        baris = [no]
        for label, kunci, satuan in kolom:
            baris.append(str(data[no][kunci]) + satuan)
        tabel.add_row(baris)
    print("")
    if not data:
        print("Belum ada data.")
    else:
        print(tabel)


def tampil_pesan(judul, daftar_baris):
    """Tabel satu kolom untuk pesan/ringkasan, daftar_baris berupa list teks."""
    tabel = PrettyTable([judul])
    tabel.align = "l"
    for teks in daftar_baris:
        tabel.add_row([teks])
    print(tabel)
