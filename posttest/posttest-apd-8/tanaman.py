"""CRUD data tanaman."""
import data
from tampilan import tampil_menu, tampil_tabel, pesan_sukses, pesan_error, pesan_info
from validasi import input_teks, input_angka, input_tanggal, pilih_dari_menu, ambil_id_tanaman
from hitung import hitung_total_tanaman


def tampil_daftar_tanaman():
    tampil_tabel("DAFTAR TANAMAN", data.kolom_tanaman, data.data_tanaman, "ID")
    jenis, total = hitung_total_tanaman()
    print("Total:", jenis, "jenis,", total, "tanaman")


def tambah_tanaman():
    print("")
    print("--- TAMBAH TANAMAN ---")
    nama = input_teks("Nama tanaman: ")
    jenis = input_teks("Jenis tanaman: ")
    tanggal = input_tanggal("Tanggal tanam (DD-MM-YYYY, Enter = hari ini): ", default_hari_ini=True)
    jumlah = input_angka("Jumlah tanaman: ")
    lokasi = input_teks("Lokasi tanaman: ")
    media = input_teks("Media tanam: ")
    tahap = pilih_dari_menu("Tahap pertumbuhan", data.daftar_tahap, "Pilih tahap: ")

    data.id_terakhir["tanaman"] += 1
    id_baru = data.id_terakhir["tanaman"]
    data.data_tanaman[id_baru] = {
        "nama": nama, "jenis": jenis, "tanggal_tanam": tanggal,
        "jumlah": jumlah, "lokasi": lokasi, "media": media, "tahap": tahap
    }
    pesan_sukses("Tanaman berhasil ditambahkan dengan ID " + str(id_baru))


def ubah_tanaman():
    tampil_daftar_tanaman()
    id_cari = ambil_id_tanaman()
    if id_cari is None:
        return
    tanaman = data.data_tanaman[id_cari]

    print("Kosongkan (tekan Enter) jika tidak ingin mengubah.")
    baru = input_teks("Nama [" + tanaman["nama"] + "]: ", True)
    if baru != "":
        tanaman["nama"] = baru
    baru = input_teks("Jenis [" + tanaman["jenis"] + "]: ", True)
    if baru != "":
        tanaman["jenis"] = baru
    baru = input_angka("Jumlah [" + str(tanaman["jumlah"]) + "]: ", True)
    if baru is not None:
        tanaman["jumlah"] = baru
    baru = input_teks("Lokasi [" + tanaman["lokasi"] + "]: ", True)
    if baru != "":
        tanaman["lokasi"] = baru
    baru = input_teks("Media tanam [" + tanaman["media"] + "]: ", True)
    if baru != "":
        tanaman["media"] = baru
    baru = pilih_dari_menu("Tahap pertumbuhan", data.daftar_tahap,
                           "Tahap [" + tanaman["tahap"] + "] (nomor, Enter = tetap): ", True)
    if baru is not None:
        tanaman["tahap"] = baru
    pesan_sukses("Data tanaman berhasil diubah.")


def hapus_terkait(data_catatan, id_cari):
    """Menghapus semua catatan milik tanaman tertentu dari sebuah dictionary."""
    for no in list(data_catatan):
        if data_catatan[no]["id"] == id_cari:
            del data_catatan[no]


def hapus_tanaman():
    tampil_daftar_tanaman()
    id_cari = ambil_id_tanaman()
    if id_cari is None:
        return
    yakin = input("Yakin ingin menghapus " + data.data_tanaman[id_cari]["nama"] + "? (ya/tidak): ")
    if yakin.lower() == "ya":
        del data.data_tanaman[id_cari]
        hapus_terkait(data.data_kondisi, id_cari)
        hapus_terkait(data.data_perawatan, id_cari)
        hapus_terkait(data.data_hama, id_cari)
        hapus_terkait(data.data_panen, id_cari)
        pesan_sukses("Tanaman berhasil dihapus.")
    else:
        pesan_info("Penghapusan dibatalkan.")


def menu_kelola_tanaman(role):
    while True:
        tampil_menu("KELOLA DATA TANAMAN", data.menu_kelola)
        pilih = input("Pilih: ")
        if pilih == "1":
            if role != "admin":
                pesan_info("Maaf, hanya admin yang boleh menambah tanaman!")
            else:
                tambah_tanaman()
        elif pilih == "2":
            tampil_daftar_tanaman()
        elif pilih == "3":
            ubah_tanaman()
        elif pilih == "4":
            if role != "admin":
                pesan_info("Maaf, hanya admin yang boleh menghapus tanaman!")
            else:
                hapus_tanaman()
        elif pilih == "5":
            break
        else:
            pesan_error("Pilihan tidak valid!")
