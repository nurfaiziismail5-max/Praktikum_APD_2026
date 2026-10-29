import os

data_user = {
    "admin": {"password": "admin1", "role": "admin"},
    "pengguna": {"password": "pengguna1", "role": "pengguna"}
}

data_tanaman = {
    1: {"nama": "Mangga", "jenis": "Buah", "tanggal_tanam": "01-01-2026", "jumlah": 15, "lokasi": "Kebun A", "media": "Tanah", "tahap": "Vegetatif"},
    2: {"nama": "Apel", "jenis": "Buah", "tanggal_tanam": "01-01-2026", "jumlah": 10, "lokasi": "Kebun B", "media": "Tanah", "tahap": "Vegetatif"},
    3: {"nama": "Anggur", "jenis": "Buah", "tanggal_tanam": "01-01-2026", "jumlah": 10, "lokasi": "Kebun C", "media": "Tanah", "tahap": "Berbunga"}
}
id_terakhir = 3

data_kondisi = {}
data_perawatan = {}
data_hama = {}
data_panen = {}
id_kondisi = 0
id_perawatan = 0
id_hama = 0
id_panen = 0

menu_utama = {
    "1": "Kelola Data Tanaman",
    "2": "Pemantauan Kondisi Tanaman",
    "3": "Jadwal dan Riwayat Perawatan",
    "4": "Pengecekan Status Perawatan",
    "5": "Pemantauan Hama dan Penyakit",
    "6": "Data Panen dan Hasil Produksi",
    "7": "Laporan dan Rekapitulasi",
    "8": "Logout"
}
menu_kelola = {
    "1": "Tambah Tanaman",
    "2": "Lihat Tanaman",
    "3": "Ubah Tanaman",
    "4": "Hapus Tanaman",
    "5": "Kembali"
}
menu_catat = {
    "1": "Tambah Catatan",
    "2": "Lihat Catatan",
    "3": "Kembali"
}
menu_laporan = {
    "1": "Laporan Data Tanaman",
    "2": "Laporan Kondisi Tanaman",
    "3": "Laporan Perawatan",
    "4": "Laporan Hama dan Penyakit",
    "5": "Laporan Hasil Panen",
    "6": "Kembali"
}

daftar_tahap = {"1": "Bibit", "2": "Vegetatif", "3": "Berbunga", "4": "Berbuah"}
daftar_perawatan = {
    "1": "Penyiraman",
    "2": "Pemberian pupuk",
    "3": "Pemangkasan",
    "4": "Pembersihan gulma",
    "5": "Pemeriksaan kondisi",
    "6": "Lainnya"
}
daftar_kualitas = {"1": "Baik", "2": "Cukup", "3": "Kurang"}
pilihan_kondisi = {
    "daun": {"1": "hijau", "2": "kuning", "3": "layu"},
    "batang": {"1": "normal", "2": "rusak"},
    "tanah": {"1": "lembap", "2": "normal", "3": "kering"},
    "akar": {"1": "normal", "2": "bermasalah"}
}

kolom_kondisi = [("ID tanaman", "id", ""), ("Tanggal", "tanggal", ""), ("Daun", "daun", ""),
                 ("Batang", "batang", ""), ("Tanah", "tanah", ""), ("Akar", "akar", ""),
                 ("Tahap", "tahap", "")]
kolom_perawatan = [("ID tanaman", "id", ""), ("Jenis perawatan", "jenis", ""), ("Tanggal", "tanggal", ""),
                   ("Jadwal berikutnya", "jadwal", ""), ("Keterangan", "keterangan", "")]
kolom_hama = [("ID tanaman", "id", ""), ("Tanggal", "tanggal", ""), ("Gejala", "gejala", ""),
              ("Dugaan", "dugaan", ""), ("Penanganan", "penanganan", ""),
              ("Pencegahan", "pencegahan", ""), ("Hasil lanjut", "hasil", "")]
kolom_panen = [("ID tanaman", "id", ""), ("Nama", "nama", ""), ("Tanggal", "tanggal", ""),
               ("Jumlah", "jumlah", ""), ("Berat", "berat", " kg"), ("Kualitas", "kualitas", ""),
               ("Keterangan", "keterangan", "")]

def ambil_id_tanaman():
    """Meminta ID tanaman dan memvalidasinya. Mengembalikan ID, atau None jika tidak valid."""
    try:
        id_cari = int(input("Masukkan ID tanaman: "))
        if id_cari not in data_tanaman:
            raise KeyError(id_cari)
        return id_cari
    except ValueError:
        print("ID harus berupa angka!")
    except KeyError:
        print("ID tanaman tidak ditemukan!")
    return None


def hitung_total_tanaman():
    """Menghitung total jenis dan total jumlah tanaman (memakai fungsi rekursif)."""
    daftar_jumlah = []
    for id_t in data_tanaman:
        daftar_jumlah.append(data_tanaman[id_t]["jumlah"])
    jenis = len(daftar_jumlah)
    total = jumlah_rekursif(daftar_jumlah)
    return jenis, total

def cek_login(username, password):
    """Mengembalikan role jika login benar, None jika salah."""
    try:
        if data_user[username]["password"] == password:
            return data_user[username]["role"]
    except KeyError:
        pass
    return None


def input_angka(pesan, boleh_kosong=False):
    """Meminta angka bulat >= 0 sampai input benar. Jika boleh_kosong, Enter mengembalikan None."""
    while True:
        teks = input(pesan)
        if boleh_kosong and teks == "":
            return None
        try:
            nilai = int(teks)
            if nilai < 0:
                raise ValueError("negatif")
            return nilai
        except ValueError:
            print("Input harus berupa angka bulat positif!")


def pilih_dari_menu(judul, pilihan, pesan, boleh_kosong=False):
    """Menampilkan pilihan bernomor dan mengembalikan nilai yang dipilih."""
    print(judul)
    for nomor in pilihan:
        print(nomor, ".", pilihan[nomor])
    while True:
        nomor_pilih = input(pesan)
        if boleh_kosong and nomor_pilih == "":
            return None
        try:
            return pilihan[nomor_pilih]
        except KeyError:
            print("Pilihan tidak valid!")


def status_tanaman(id_t):
    """Menentukan status perawatan tanaman dari catatan kondisi terakhir."""
    kondisi = None
    jadwal = "-"
    for no in data_kondisi:
        if data_kondisi[no]["id"] == id_t:
            kondisi = data_kondisi[no]
    for no in data_perawatan:
        if data_perawatan[no]["id"] == id_t and data_perawatan[no]["jadwal"] != "-":
            jadwal = data_perawatan[no]["jadwal"]

    if kondisi is None:
        status = "Perlu Pemeriksaan (belum ada data kondisi)"
    elif kondisi["daun"] == "kuning" and kondisi["tanah"] == "kering":
        status = "Perlu Perawatan"
    elif kondisi["daun"] == "hijau" and kondisi["tanah"] != "kering" and kondisi["batang"] == "normal" and kondisi["akar"] == "normal":
        status = "Sehat"
    else:
        status = "Perlu Pemeriksaan"
    return status, jadwal

def jumlah_rekursif(daftar, indeks=0):
    """Menjumlahkan isi list secara rekursif."""
    if indeks >= len(daftar):
        return 0
    return daftar[indeks] + jumlah_rekursif(daftar, indeks + 1)

def tampil_menu(judul, menu):
    print("")
    print("---", judul, "---")
    for nomor in menu:
        print(nomor, ".", menu[nomor])


def tampil_daftar_tanaman():
    print("")
    print("--- DAFTAR TANAMAN ---")
    if not data_tanaman:
        print("Belum ada data tanaman.")
    for id_t in data_tanaman:
        t = data_tanaman[id_t]
        print("ID           :", id_t)
        print("Nama         :", t["nama"])
        print("Jenis        :", t["jenis"])
        print("Tanggal tanam:", t["tanggal_tanam"])
        print("Jumlah       :", t["jumlah"])
        print("Lokasi       :", t["lokasi"])
        print("Media tanam  :", t["media"])
        print("Tahap        :", t["tahap"])
        print("-------------------------")
    jenis, total = hitung_total_tanaman()
    print("Total:", jenis, "jenis,", total, "tanaman")


def tambah_tanaman():
    global id_terakhir
    print("")
    print("--- TAMBAH TANAMAN ---")
    nama = input("Nama tanaman: ")
    jenis = input("Jenis tanaman: ")
    tanggal = input("Tanggal tanam (contoh 10-10-2026): ")
    jumlah = input_angka("Jumlah tanaman: ")
    lokasi = input("Lokasi tanaman: ")
    media = input("Media tanam: ")
    tahap = pilih_dari_menu("Tahap pertumbuhan:", daftar_tahap, "Pilih tahap: ")

    id_terakhir = id_terakhir + 1
    data_tanaman[id_terakhir] = {
        "nama": nama, "jenis": jenis, "tanggal_tanam": tanggal,
        "jumlah": jumlah, "lokasi": lokasi, "media": media, "tahap": tahap
    }
    print("Tanaman berhasil ditambahkan dengan ID", id_terakhir)


def ubah_tanaman():
    id_cari = ambil_id_tanaman()
    if id_cari is None:
        return
    tanaman = data_tanaman[id_cari]

    print("Kosongkan (tekan Enter) jika tidak ingin mengubah.")
    baru = input("Nama [" + tanaman["nama"] + "]: ")
    if baru != "":
        tanaman["nama"] = baru
    baru = input("Jenis [" + tanaman["jenis"] + "]: ")
    if baru != "":
        tanaman["jenis"] = baru
    baru = input_angka("Jumlah [" + str(tanaman["jumlah"]) + "]: ", True)
    if baru is not None:
        tanaman["jumlah"] = baru
    baru = input("Lokasi [" + tanaman["lokasi"] + "]: ")
    if baru != "":
        tanaman["lokasi"] = baru
    baru = input("Media tanam [" + tanaman["media"] + "]: ")
    if baru != "":
        tanaman["media"] = baru
    baru = pilih_dari_menu("Tahap pertumbuhan:", daftar_tahap,
                           "Tahap [" + tanaman["tahap"] + "] (nomor): ", True)
    if baru is not None:
        tanaman["tahap"] = baru
    print("Data tanaman berhasil diubah.")


def hapus_terkait(data, id_cari):
    """Menghapus semua catatan milik tanaman tertentu dari sebuah dictionary."""
    for no in list(data):
        if data[no]["id"] == id_cari:
            del data[no]


def hapus_tanaman():
    id_cari = ambil_id_tanaman()
    if id_cari is None:
        return
    yakin = input("Yakin ingin menghapus " + data_tanaman[id_cari]["nama"] + "? (ya/tidak): ")
    if yakin == "ya":
        del data_tanaman[id_cari]
        hapus_terkait(data_kondisi, id_cari)
        hapus_terkait(data_perawatan, id_cari)
        hapus_terkait(data_hama, id_cari)
        hapus_terkait(data_panen, id_cari)
        print("Tanaman berhasil dihapus.")
    else:
        print("Penghapusan dibatalkan.")


def menu_kelola_tanaman(role):
    while True:
        tampil_menu("KELOLA DATA TANAMAN", menu_kelola)
        pilih = input("Pilih: ")
        if pilih == "1":
            if role != "admin":
                print("Maaf, hanya admin yang boleh menambah tanaman!")
            else:
                tambah_tanaman()
        elif pilih == "2":
            tampil_daftar_tanaman()
        elif pilih == "3":
            ubah_tanaman()
        elif pilih == "4":
            if role != "admin":
                print("Maaf, hanya admin yang boleh menghapus tanaman!")
            else:
                hapus_tanaman()
        elif pilih == "5":
            break
        else:
            print("Pilihan tidak valid!")


def tambah_kondisi():
    global id_kondisi
    id_cari = ambil_id_tanaman()
    if id_cari is None:
        return
    catatan = {"id": id_cari}
    for nama_k in pilihan_kondisi:
        print("")
        catatan[nama_k] = pilih_dari_menu("Kondisi " + nama_k + ":", pilihan_kondisi[nama_k], "Pilih: ")
    catatan["tahap"] = data_tanaman[id_cari]["tahap"]
    catatan["tanggal"] = input("Tanggal pemeriksaan (contoh 10-10-2026): ")
    id_kondisi = id_kondisi + 1
    data_kondisi[id_kondisi] = catatan
    print("Catatan kondisi berhasil disimpan.")
    if catatan["daun"] == "kuning" and catatan["tanah"] == "kering":
        print("Keterangan: tanaman perlu diperiksa dan mungkin membutuhkan perawatan.")


def tambah_perawatan():
    global id_perawatan
    id_cari = ambil_id_tanaman()
    if id_cari is None:
        return
    jenis = pilih_dari_menu("Jenis perawatan:", daftar_perawatan, "Pilih: ")
    tanggal = input("Tanggal perawatan (contoh 10-10-2026): ")
    jadwal = input("Jadwal berikutnya (kosongkan jika tidak ada): ")
    if jadwal == "":
        jadwal = "-"
    keterangan = input("Keterangan/hasil perawatan: ")
    if keterangan == "":
        keterangan = "-"
    id_perawatan = id_perawatan + 1
    data_perawatan[id_perawatan] = {"id": id_cari, "jenis": jenis, "tanggal": tanggal,
                                    "jadwal": jadwal, "keterangan": keterangan}
    print("Catatan perawatan berhasil disimpan.")


def tambah_hama():
    global id_hama
    id_cari = ambil_id_tanaman()
    if id_cari is None:
        return
    tanggal = input("Tanggal pemeriksaan (contoh 10-10-2026): ")
    gejala = input("Gejala yang ditemukan: ")
    dugaan = input("Hama/penyakit yang dicurigai: ")
    if dugaan == "":
        dugaan = "Belum diketahui"
    penanganan = input("Tindakan penanganan: ")
    if penanganan == "":
        penanganan = "-"
    pencegahan = input("Tindakan pencegahan: ")
    if pencegahan == "":
        pencegahan = "-"
    hasil = input("Hasil pemeriksaan berikutnya: ")
    if hasil == "":
        hasil = "-"
    id_hama = id_hama + 1
    data_hama[id_hama] = {"id": id_cari, "tanggal": tanggal, "gejala": gejala, "dugaan": dugaan,
                          "penanganan": penanganan, "pencegahan": pencegahan, "hasil": hasil}
    print("Catatan berhasil disimpan.")
    print("Saran: lakukan pemeriksaan lebih lanjut, karena gejala belum tentu menunjukkan satu jenis hama/penyakit.")


def tambah_panen():
    global id_panen
    id_cari = ambil_id_tanaman()
    if id_cari is None:
        return
    tanggal = input("Tanggal panen (contoh 10-10-2026): ")
    jumlah = input_angka("Jumlah hasil panen: ")
    berat = input_angka("Berat hasil panen (kg, angka bulat): ")
    kualitas = pilih_dari_menu("Kualitas hasil panen:", daftar_kualitas, "Pilih: ")
    keterangan = input("Keterangan tambahan: ")
    if keterangan == "":
        keterangan = "-"
    id_panen = id_panen + 1
    data_panen[id_panen] = {"id": id_cari, "nama": data_tanaman[id_cari]["nama"], "tanggal": tanggal,
                            "jumlah": jumlah, "berat": berat, "kualitas": kualitas,
                            "keterangan": keterangan}
    print("Data panen berhasil disimpan.")


def tampil_catatan(data, kolom):
    print("")
    if not data:
        print("Belum ada catatan.")
    for no in data:
        for label, kunci, satuan in kolom:
            print(label.ljust(18) + ":", str(data[no][kunci]) + satuan)
        print("-------------------------")


def menu_catatan(judul, fungsi_tambah, data, kolom):
    while True:
        tampil_menu(judul, menu_catat)
        pilih = input("Pilih: ")
        if pilih == "1":
            fungsi_tambah()
        elif pilih == "2":
            tampil_catatan(data, kolom)
        elif pilih == "3":
            break
        else:
            print("Pilihan tidak valid!")


def cek_status_perawatan():
    print("")
    print("--- PENGECEKAN STATUS PERAWATAN ---")
    if not data_tanaman:
        print("Belum ada data tanaman.")
    for id_t in data_tanaman:
        status, jadwal = status_tanaman(id_t)
        print("ID", id_t, "-", data_tanaman[id_t]["nama"], ":", status)
        if jadwal != "-":
            print("    Perawatan Terjadwal:", jadwal)


def tampil_laporan(judul, data, kolom):
    print("")
    print("===", judul, "===")
    if not data:
        print("Belum ada data.")
    for no in data:
        baris = []
        for label, kunci, satuan in kolom:
            baris.append(label + ": " + str(data[no][kunci]) + satuan)
        print(" | ".join(baris))


def laporan_tanaman():
    print("")
    print("=== LAPORAN DATA TANAMAN ===")
    for id_t in data_tanaman:
        t = data_tanaman[id_t]
        print("ID", id_t, "|", t["nama"], "| Jumlah:", t["jumlah"], "| Lokasi:", t["lokasi"], "| Tanam:", t["tanggal_tanam"])
    jenis, total = hitung_total_tanaman()
    print("Total:", jenis, "jenis,", total, "tanaman")


def laporan_panen():
    tampil_laporan("LAPORAN HASIL PANEN", data_panen, kolom_panen)
    daftar_berat = []
    for no in data_panen:
        daftar_berat.append(data_panen[no]["berat"])
    print("Total berat panen:", jumlah_rekursif(daftar_berat), "kg")


def menu_laporan_program():
    while True:
        tampil_menu("LAPORAN DAN REKAPITULASI", menu_laporan)
        pilih = input("Pilih: ")
        if pilih == "1":
            laporan_tanaman()
        elif pilih == "2":
            tampil_laporan("LAPORAN KONDISI TANAMAN", data_kondisi, kolom_kondisi)
        elif pilih == "3":
            tampil_laporan("LAPORAN PERAWATAN", data_perawatan, kolom_perawatan)
            print("Jumlah catatan perawatan:", len(data_perawatan))
        elif pilih == "4":
            tampil_laporan("LAPORAN HAMA DAN PENYAKIT", data_hama, kolom_hama)
        elif pilih == "5":
            laporan_panen()
        elif pilih == "6":
            break
        else:
            print("Pilihan tidak valid!")


def menu_utama_program(role):
    while True:
        tampil_menu("MENU UTAMA", menu_utama)
        pilihan = input("Pilih menu: ")
        if pilihan == "1":
            menu_kelola_tanaman(role)
        elif pilihan == "2":
            menu_catatan("PEMANTAUAN KONDISI TANAMAN", tambah_kondisi, data_kondisi, kolom_kondisi)
        elif pilihan == "3":
            menu_catatan("JADWAL DAN RIWAYAT PERAWATAN", tambah_perawatan, data_perawatan, kolom_perawatan)
        elif pilihan == "4":
            cek_status_perawatan()
        elif pilihan == "5":
            menu_catatan("PEMANTAUAN HAMA DAN PENYAKIT", tambah_hama, data_hama, kolom_hama)
        elif pilihan == "6":
            menu_catatan("DATA PANEN DAN HASIL PRODUKSI", tambah_panen, data_panen, kolom_panen)
        elif pilihan == "7":
            menu_laporan_program()
        elif pilihan == "8":
            print("Anda sudah logout.")
            break
        else:
            print("Pilihan tidak valid!")


def main():
    os.system("cls" if os.name == "nt" else "clear")
    while True:
        print("")
        print("=========================================")
        print("  SISTEM PEMANTAUAN PERAWATAN TANAMAN")
        print("=========================================")
        print("Ketik 0 pada username untuk keluar program")
        username = input("Username: ")
        if username == "0":
            break
        password = input("Password: ")

        role = cek_login(username, password)
        if role is None:
            print("Username atau password salah!")
            continue
        print("Login berhasil. Selamat datang,", username, "(" + role + ")")
        menu_utama_program(role)


try:
    main()
except (KeyboardInterrupt, EOFError):
    print("\nProgram dihentikan paksa.")
finally:
    print("Program selesai.")
