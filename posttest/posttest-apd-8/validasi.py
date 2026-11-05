"""Fungsi input dan validasi."""
from datetime import datetime
import data
from tampilan import tampil_menu, pesan_error


def input_teks(pesan, boleh_kosong=False):
    """Meminta teks. Jika tidak boleh kosong, diulang sampai diisi."""
    while True:
        teks = input(pesan).strip()
        if teks != "" or boleh_kosong:
            return teks
        pesan_error("Input tidak boleh kosong!")


def input_angka(pesan, boleh_kosong=False):
    """Meminta angka bulat >= 0. Jika boleh_kosong, Enter mengembalikan None."""
    while True:
        teks = input(pesan).strip()
        if boleh_kosong and teks == "":
            return None
        try:
            nilai = int(teks)
            if nilai < 0:
                raise ValueError("negatif")
            return nilai
        except ValueError:
            pesan_error("Input harus berupa angka bulat positif!")


def input_tanggal(pesan, boleh_kosong=False, default_hari_ini=False):
    """Meminta tanggal format DD-MM-YYYY dan memvalidasinya dengan datetime."""
    while True:
        teks = input(pesan).strip()
        if teks == "":
            if default_hari_ini:
                return datetime.now().strftime("%d-%m-%Y")
            if boleh_kosong:
                return None
        try:
            datetime.strptime(teks, "%d-%m-%Y")
            return teks
        except ValueError:
            pesan_error("Format tanggal salah! Gunakan DD-MM-YYYY (contoh 10-10-2026).")


def pilih_dari_menu(judul, pilihan, pesan, boleh_kosong=False):
    """Menampilkan pilihan bernomor dan mengembalikan nilai yang dipilih."""
    tampil_menu(judul, pilihan)
    while True:
        nomor_pilih = input(pesan).strip()
        if boleh_kosong and nomor_pilih == "":
            return None
        try:
            return pilihan[nomor_pilih]
        except KeyError:
            pesan_error("Pilihan tidak valid!")


def ambil_id_tanaman():
    """Meminta ID tanaman dan memvalidasinya. Mengembalikan ID, atau None jika tidak valid."""
    try:
        id_cari = int(input("Masukkan ID tanaman: "))
        if id_cari not in data.data_tanaman:
            raise KeyError(id_cari)
        return id_cari
    except ValueError:
        pesan_error("ID harus berupa angka!")
    except KeyError:
        pesan_error("ID tanaman tidak ditemukan!")
    return None
