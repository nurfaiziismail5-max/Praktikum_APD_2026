"""Program utama: Sistem Pemantauan Perawatan Tanaman."""
import data
from tampilan import bersihkan_layar, tampil_menu, tampil_pesan, pesan_sukses, pesan_error, pesan_info
from auth import minta_login
from tanaman import menu_kelola_tanaman
from catatan import menu_catatan, tambah_kondisi, tambah_perawatan, tambah_hama, tambah_panen, cek_status_perawatan
from laporan import menu_laporan_program


def menu_utama_program(role):
    while True:
        tampil_menu("MENU UTAMA", data.menu_utama)
        pilihan = input("Pilih menu: ")
        if pilihan == "1":
            menu_kelola_tanaman(role)
        elif pilihan == "2":
            menu_catatan("PEMANTAUAN KONDISI TANAMAN", tambah_kondisi, data.data_kondisi, data.kolom_kondisi)
        elif pilihan == "3":
            menu_catatan("JADWAL DAN RIWAYAT PERAWATAN", tambah_perawatan, data.data_perawatan, data.kolom_perawatan)
        elif pilihan == "4":
            cek_status_perawatan()
        elif pilihan == "5":
            menu_catatan("PEMANTAUAN HAMA DAN PENYAKIT", tambah_hama, data.data_hama, data.kolom_hama)
        elif pilihan == "6":
            menu_catatan("DATA PANEN DAN HASIL PRODUKSI", tambah_panen, data.data_panen, data.kolom_panen)
        elif pilihan == "7":
            menu_laporan_program()
        elif pilihan == "8":
            pesan_info("Anda sudah logout.")
            break
        else:
            pesan_error("Pilihan tidak valid!")


def main():
    bersihkan_layar()
    while True:
        print("")
        tampil_pesan("SISTEM PEMANTAUAN PERAWATAN TANAMAN",
                     ["Ketik 0 pada username untuk keluar program"])
        username, role = minta_login()
        if username == "0":
            break
        if role is None:
            pesan_error("Username atau password salah!")
            continue
        pesan_sukses("Login berhasil. Selamat datang, " + username + " (" + role + ")")
        menu_utama_program(role)


try:
    main()
except (KeyboardInterrupt, EOFError):
    print("Program dihentikan paksa.")
finally:
    print("Program selesai.")
