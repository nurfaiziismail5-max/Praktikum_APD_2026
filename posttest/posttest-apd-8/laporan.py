"""Laporan dan rekapitulasi."""
import data
from tampilan import tampil_menu, tampil_tabel, pesan_error
from hitung import jumlah_rekursif, hitung_total_tanaman


def laporan_tanaman():
    tampil_tabel("LAPORAN DATA TANAMAN", data.kolom_ringkas_tanaman, data.data_tanaman, "ID")
    jenis, total = hitung_total_tanaman()
    print("Total:", jenis, "jenis,", total, "tanaman")


def laporan_perawatan():
    tampil_tabel("LAPORAN PERAWATAN", data.kolom_perawatan, data.data_perawatan)
    print("Jumlah catatan perawatan:", len(data.data_perawatan))


def laporan_panen():
    tampil_tabel("LAPORAN HASIL PANEN", data.kolom_panen, data.data_panen)
    daftar_berat = []
    for no in data.data_panen:
        daftar_berat.append(data.data_panen[no]["berat"])
    print("Total berat panen:", jumlah_rekursif(daftar_berat), "kg")


def menu_laporan_program():
    while True:
        tampil_menu("LAPORAN DAN REKAPITULASI", data.menu_laporan)
        pilih = input("Pilih: ")
        if pilih == "1":
            laporan_tanaman()
        elif pilih == "2":
            tampil_tabel("LAPORAN KONDISI TANAMAN", data.kolom_kondisi, data.data_kondisi)
        elif pilih == "3":
            laporan_perawatan()
        elif pilih == "4":
            tampil_tabel("LAPORAN HAMA DAN PENYAKIT", data.kolom_hama, data.data_hama)
        elif pilih == "5":
            laporan_panen()
        elif pilih == "6":
            break
        else:
            pesan_error("Pilihan tidak valid!")
