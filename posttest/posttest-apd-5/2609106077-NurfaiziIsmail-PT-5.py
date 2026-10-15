import os
os.system("cls" if os.name == "nt" else "clear")

data_user = [
    {"username": "admin", "password": "admin1", "role": "admin"},
    {"username": "petugas", "password": "petugas1", "role": "petugas"}
]

data_tanaman = [
    {"id": 1, "nama": "Mangga", "jenis": "Buah", "tanggal_tanam": "01-01-2026", "jumlah": 15, "lokasi": "Kebun A", "media": "Tanah", "tahap": "Vegetatif"},
    {"id": 2, "nama": "Apel", "jenis": "Buah", "tanggal_tanam": "01-01-2026", "jumlah": 10, "lokasi": "Kebun B", "media": "Tanah", "tahap": "Vegetatif"},
    {"id": 3, "nama": "Anggur", "jenis": "Buah", "tanggal_tanam": "01-01-2026", "jumlah": 10, "lokasi": "Kebun C", "media": "Tanah", "tahap": "Berbunga"}
]
id_terakhir = 3

data_kondisi = []
data_perawatan = []
data_hama = []
data_panen = []

menu_utama = [
    "Kelola Data Tanaman",
    "Pemantauan Kondisi Tanaman",
    "Jadwal dan Riwayat Perawatan",
    "Pengecekan Status Perawatan",
    "Pemantauan Hama dan Penyakit",
    "Data Panen dan Hasil Produksi",
    "Laporan dan Rekapitulasi",
    "Logout"
]
menu_kelola = ["Tambah Tanaman", "Lihat Tanaman", "Ubah Tanaman", "Hapus Tanaman", "Kembali"]
menu_catat = ["Tambah Catatan", "Lihat Catatan", "Kembali"]
menu_laporan = [
    "Laporan Data Tanaman",
    "Laporan Kondisi Tanaman",
    "Laporan Perawatan",
    "Laporan Hama dan Penyakit",
    "Laporan Hasil Panen",
    "Kembali"
]
daftar_tahap = ["Bibit", "Vegetatif", "Berbunga", "Berbuah"]
daftar_perawatan = ["Penyiraman", "Pemberian pupuk", "Pemangkasan", "Pembersihan gulma", "Pemeriksaan kondisi", "Lainnya"]
daftar_kualitas = ["Baik", "Cukup", "Kurang"]

nama_kondisi = ["daun", "batang", "tanah", "akar"]
pilihan_kondisi = [
    ["hijau", "kuning", "layu"],
    ["normal", "rusak"],
    ["lembap", "normal", "kering"],
    ["normal", "bermasalah"]
]

# Daftar nomor pilihan yang valid (pengganti len)
nomor_tahap = ["1", "2", "3", "4"]
nomor_perawatan = ["1", "2", "3", "4", "5", "6"]
nomor_kualitas = ["1", "2", "3"]
nomor_kondisi = [["1", "2", "3"], ["1", "2"], ["1", "2", "3"], ["1", "2"]]


while True:

    print("")
    print("=========================================")
    print("  SISTEM PEMANTAUAN PERAWATAN TANAMAN")
    print("=========================================")
    print("Ketik 0 pada username untuk keluar program")
    username = input("Username: ")
    if username == "0":
        print("Program selesai.")
        break
    password = input("Password: ")

    login_berhasil = False
    role = ""
    for u in data_user:
        if u["username"] == username and u["password"] == password:
            login_berhasil = True
            role = u["role"]

    if login_berhasil == False:
        print("Username atau password salah!")
        continue

    print("Login berhasil. Selamat datang,", username, "(" + role + ")")

    while True:
        print("")
        print("======= MENU UTAMA =======")
        for nomor, item in enumerate(menu_utama, 1):
            print(nomor, ".", item)
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            while True:
                print("")
                print("--- KELOLA DATA TANAMAN ---")
                for nomor, item in enumerate(menu_kelola, 1):
                    print(nomor, ".", item)
                pilih_kelola = input("Pilih: ")

                if pilih_kelola == "1":
                    if role != "admin":
                        print("Maaf, hanya admin yang boleh menambah tanaman!")
                        continue

                    print("")
                    print("--- TAMBAH TANAMAN ---")
                    nama = input("Nama tanaman: ")
                    jenis = input("Jenis tanaman: ")
                    tanggal = input("Tanggal tanam (contoh 10-10-2026): ")

                    jumlah = input("Jumlah tanaman: ")
                    while jumlah.isdigit() == False:
                        print("Jumlah harus berupa angka!")
                        jumlah = input("Jumlah tanaman: ")

                    lokasi = input("Lokasi tanaman: ")
                    media = input("Media tanam: ")

                    print("Tahap pertumbuhan:")
                    for nomor, item in enumerate(daftar_tahap, 1):
                        print(nomor, ".", item)
                    pilih_tahap = input("Pilih tahap: ")
                    while pilih_tahap not in nomor_tahap:
                        print("Pilihan tidak valid!")
                        pilih_tahap = input("Pilih tahap: ")

                    id_terakhir = id_terakhir + 1
                    tanaman_baru = {
                        "id": id_terakhir,
                        "nama": nama,
                        "jenis": jenis,
                        "tanggal_tanam": tanggal,
                        "jumlah": int(jumlah),
                        "lokasi": lokasi,
                        "media": media,
                        "tahap": daftar_tahap[int(pilih_tahap) - 1]
                    }
                    data_tanaman.append(tanaman_baru)
                    print("Tanaman berhasil ditambahkan dengan ID", id_terakhir)

                elif pilih_kelola == "2":
                    print("")
                    print("--- DAFTAR TANAMAN ---")
                    if not data_tanaman:
                        print("Belum ada data tanaman.")
                    total = 0
                    jenis_total = 0
                    for t in data_tanaman:
                        print("ID           :", t["id"])
                        print("Nama         :", t["nama"])
                        print("Jenis        :", t["jenis"])
                        print("Tanggal tanam:", t["tanggal_tanam"])
                        print("Jumlah       :", t["jumlah"])
                        print("Lokasi       :", t["lokasi"])
                        print("Media tanam  :", t["media"])
                        print("Tahap        :", t["tahap"])
                        print("-------------------------")
                        total = total + t["jumlah"]
                        jenis_total = jenis_total + 1
                    print("Total:", jenis_total, "jenis,", total, "tanaman")

                elif pilih_kelola == "3":
                    id_input = input("Masukkan ID tanaman yang diubah: ")
                    if id_input.isdigit() == False:
                        print("ID harus berupa angka!")
                        continue
                    id_cari = int(id_input)

                    ketemu = False
                    for t in data_tanaman:
                        if t["id"] == id_cari:
                            ketemu = True
                            tanaman = t
                    if ketemu == False:
                        print("ID tanaman tidak ditemukan!")
                        continue

                    print("Kosongkan (tekan Enter) jika tidak ingin mengubah.")
                    baru = input("Nama [" + tanaman["nama"] + "]: ")
                    if baru != "":
                        tanaman["nama"] = baru
                    baru = input("Jenis [" + tanaman["jenis"] + "]: ")
                    if baru != "":
                        tanaman["jenis"] = baru
                    baru = input("Jumlah [" + str(tanaman["jumlah"]) + "]: ")
                    while baru != "" and baru.isdigit() == False:
                        print("Jumlah harus berupa angka!")
                        baru = input("Jumlah [" + str(tanaman["jumlah"]) + "]: ")
                    if baru != "":
                        tanaman["jumlah"] = int(baru)
                    baru = input("Lokasi [" + tanaman["lokasi"] + "]: ")
                    if baru != "":
                        tanaman["lokasi"] = baru
                    baru = input("Media tanam [" + tanaman["media"] + "]: ")
                    if baru != "":
                        tanaman["media"] = baru

                    print("Tahap pertumbuhan:")
                    for nomor, item in enumerate(daftar_tahap, 1):
                        print(nomor, ".", item)
                    baru = input("Tahap [" + tanaman["tahap"] + "] (nomor): ")
                    while baru != "" and baru not in nomor_tahap:
                        print("Pilihan tidak valid!")
                        baru = input("Tahap [" + tanaman["tahap"] + "] (nomor): ")
                    if baru != "":
                        tanaman["tahap"] = daftar_tahap[int(baru) - 1]

                    print("Data tanaman berhasil diubah.")

                elif pilih_kelola == "4":
                    if role != "admin":
                        print("Maaf, hanya admin yang boleh menghapus tanaman!")
                        continue

                    id_input = input("Masukkan ID tanaman yang dihapus: ")
                    if id_input.isdigit() == False:
                        print("ID harus berupa angka!")
                        continue
                    id_cari = int(id_input)

                    ketemu = False
                    for t in data_tanaman:
                        if t["id"] == id_cari:
                            ketemu = True
                            tanaman = t
                    if ketemu == False:
                        print("ID tanaman tidak ditemukan!")
                        continue

                    yakin = input("Yakin ingin menghapus " + tanaman["nama"] + "? (ya/tidak): ")
                    if yakin == "ya":
                        data_tanaman.remove(tanaman)

                        kondisi_baru = []
                        for k in data_kondisi:
                            if k["id"] != id_cari:
                                kondisi_baru.append(k)
                        data_kondisi = kondisi_baru

                        perawatan_baru = []
                        for p in data_perawatan:
                            if p["id"] != id_cari:
                                perawatan_baru.append(p)
                        data_perawatan = perawatan_baru

                        hama_baru = []
                        for h in data_hama:
                            if h["id"] != id_cari:
                                hama_baru.append(h)
                        data_hama = hama_baru

                        panen_baru = []
                        for p in data_panen:
                            if p["id"] != id_cari:
                                panen_baru.append(p)
                        data_panen = panen_baru

                        print("Tanaman berhasil dihapus.")
                    else:
                        print("Penghapusan dibatalkan.")

                elif pilih_kelola == "5":
                    break

                else:
                    print("Pilihan tidak valid!")

        elif pilihan == "2":
            while True:
                print("")
                print("--- PEMANTAUAN KONDISI TANAMAN ---")
                for nomor, item in enumerate(menu_catat, 1):
                    print(nomor, ".", item)
                pilih_catat = input("Pilih: ")

                if pilih_catat == "1":
                    id_input = input("Masukkan ID tanaman: ")
                    if id_input.isdigit() == False:
                        print("ID harus berupa angka!")
                        continue
                    id_cari = int(id_input)

                    ketemu = False
                    for t in data_tanaman:
                        if t["id"] == id_cari:
                            ketemu = True
                            tanaman = t
                    if ketemu == False:
                        print("ID tanaman tidak ditemukan!")
                        continue

                    catatan = {"id": id_cari}

                    for i, nama_k in enumerate(nama_kondisi):
                        print("")
                        print("Kondisi", nama_k, ":")
                        for j, opsi in enumerate(pilihan_kondisi[i], 1):
                            print(j, ".", opsi)
                        pilih = input("Pilih: ")
                        while pilih not in nomor_kondisi[i]:
                            print("Pilihan tidak valid!")
                            pilih = input("Pilih: ")
                        catatan[nama_k] = pilihan_kondisi[i][int(pilih) - 1]

                    catatan["tahap"] = tanaman["tahap"]
                    catatan["tanggal"] = input("Tanggal pemeriksaan (contoh 10-10-2026): ")
                    data_kondisi.append(catatan)
                    print("Catatan kondisi berhasil disimpan.")

                    if catatan["daun"] == "kuning" and catatan["tanah"] == "kering":
                        print("Keterangan: tanaman perlu diperiksa dan mungkin membutuhkan perawatan.")

                elif pilih_catat == "2":
                    print("")
                    if not data_kondisi:
                        print("Belum ada catatan kondisi.")
                    for k in data_kondisi:
                        print("ID tanaman :", k["id"])
                        print("Tanggal    :", k["tanggal"])
                        print("Daun       :", k["daun"])
                        print("Batang     :", k["batang"])
                        print("Tanah      :", k["tanah"])
                        print("Akar       :", k["akar"])
                        print("Tahap      :", k["tahap"])
                        print("-------------------------")

                elif pilih_catat == "3":
                    break

                else:
                    print("Pilihan tidak valid!")

        elif pilihan == "3":
            while True:
                print("")
                print("--- JADWAL DAN RIWAYAT PERAWATAN ---")
                for nomor, item in enumerate(menu_catat, 1):
                    print(nomor, ".", item)
                pilih_catat = input("Pilih: ")

                if pilih_catat == "1":
                    id_input = input("Masukkan ID tanaman: ")
                    if id_input.isdigit() == False:
                        print("ID harus berupa angka!")
                        continue
                    id_cari = int(id_input)

                    ketemu = False
                    for t in data_tanaman:
                        if t["id"] == id_cari:
                            ketemu = True
                    if ketemu == False:
                        print("ID tanaman tidak ditemukan!")
                        continue

                    print("Jenis perawatan:")
                    for nomor, item in enumerate(daftar_perawatan, 1):
                        print(nomor, ".", item)
                    pilih = input("Pilih: ")
                    while pilih not in nomor_perawatan:
                        print("Pilihan tidak valid!")
                        pilih = input("Pilih: ")

                    tanggal = input("Tanggal perawatan (contoh 10-10-2026): ")
                    jadwal = input("Jadwal berikutnya (kosongkan jika tidak ada): ")
                    if jadwal == "":
                        jadwal = "-"
                    keterangan = input("Keterangan/hasil perawatan: ")
                    if keterangan == "":
                        keterangan = "-"

                    catatan = {
                        "id": id_cari,
                        "jenis": daftar_perawatan[int(pilih) - 1],
                        "tanggal": tanggal,
                        "jadwal": jadwal,
                        "keterangan": keterangan
                    }
                    data_perawatan.append(catatan)
                    print("Catatan perawatan berhasil disimpan.")

                elif pilih_catat == "2":
                    print("")
                    if not data_perawatan:
                        print("Belum ada riwayat perawatan.")
                    for p in data_perawatan:
                        print("ID tanaman        :", p["id"])
                        print("Jenis perawatan   :", p["jenis"])
                        print("Tanggal           :", p["tanggal"])
                        print("Jadwal berikutnya :", p["jadwal"])
                        print("Keterangan        :", p["keterangan"])
                        print("-------------------------")

                elif pilih_catat == "3":
                    break

                else:
                    print("Pilihan tidak valid!")

        elif pilihan == "4":
            print("")
            print("--- PENGECEKAN STATUS PERAWATAN ---")
            if not data_tanaman:
                print("Belum ada data tanaman.")

            for t in data_tanaman:
                ada_kondisi = False
                for k in data_kondisi:
                    if k["id"] == t["id"]:
                        ada_kondisi = True
                        kondisi = k

                ada_jadwal = False
                for p in data_perawatan:
                    if p["id"] == t["id"] and p["jadwal"] != "-":
                        ada_jadwal = True
                        jadwal = p["jadwal"]

                if ada_kondisi == False:
                    status = "Perlu Pemeriksaan (belum ada data kondisi)"
                elif kondisi["daun"] == "kuning" and kondisi["tanah"] == "kering":
                    status = "Perlu Perawatan"
                elif kondisi["daun"] == "hijau" and kondisi["tanah"] != "kering" and kondisi["batang"] == "normal" and kondisi["akar"] == "normal":
                    status = "Sehat"
                else:
                    status = "Perlu Pemeriksaan"

                print("ID", t["id"], "-", t["nama"], ":", status)
                if ada_jadwal == True:
                    print("    Perawatan Terjadwal:", jadwal)

        elif pilihan == "5":
            while True:
                print("")
                print("--- PEMANTAUAN HAMA DAN PENYAKIT ---")
                for nomor, item in enumerate(menu_catat, 1):
                    print(nomor, ".", item)
                pilih_catat = input("Pilih: ")

                if pilih_catat == "1":
                    id_input = input("Masukkan ID tanaman: ")
                    if id_input.isdigit() == False:
                        print("ID harus berupa angka!")
                        continue
                    id_cari = int(id_input)

                    ketemu = False
                    for t in data_tanaman:
                        if t["id"] == id_cari:
                            ketemu = True
                    if ketemu == False:
                        print("ID tanaman tidak ditemukan!")
                        continue

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

                    catatan = {
                        "id": id_cari,
                        "tanggal": tanggal,
                        "gejala": gejala,
                        "dugaan": dugaan,
                        "penanganan": penanganan,
                        "pencegahan": pencegahan,
                        "hasil": hasil
                    }
                    data_hama.append(catatan)
                    print("Catatan berhasil disimpan.")
                    print("Saran: lakukan pemeriksaan lebih lanjut, karena gejala belum tentu menunjukkan satu jenis hama/penyakit.")

                elif pilih_catat == "2":
                    print("")
                    if not data_hama:
                        print("Belum ada catatan hama dan penyakit.")
                    for h in data_hama:
                        print("ID tanaman   :", h["id"])
                        print("Tanggal      :", h["tanggal"])
                        print("Gejala       :", h["gejala"])
                        print("Dugaan       :", h["dugaan"])
                        print("Penanganan   :", h["penanganan"])
                        print("Pencegahan   :", h["pencegahan"])
                        print("Hasil lanjut :", h["hasil"])
                        print("-------------------------")

                elif pilih_catat == "3":
                    break

                else:
                    print("Pilihan tidak valid!")

        elif pilihan == "6":
            while True:
                print("")
                print("--- DATA PANEN DAN HASIL PRODUKSI ---")
                for nomor, item in enumerate(menu_catat, 1):
                    print(nomor, ".", item)
                pilih_catat = input("Pilih: ")

                if pilih_catat == "1":
                    id_input = input("Masukkan ID tanaman yang dipanen: ")
                    if id_input.isdigit() == False:
                        print("ID harus berupa angka!")
                        continue
                    id_cari = int(id_input)

                    ketemu = False
                    for t in data_tanaman:
                        if t["id"] == id_cari:
                            ketemu = True
                            tanaman = t
                    if ketemu == False:
                        print("ID tanaman tidak ditemukan!")
                        continue

                    tanggal = input("Tanggal panen (contoh 10-10-2026): ")

                    jumlah = input("Jumlah hasil panen: ")
                    while jumlah.isdigit() == False:
                        print("Jumlah harus berupa angka!")
                        jumlah = input("Jumlah hasil panen: ")

                    berat = input("Berat hasil panen (kg, angka bulat): ")
                    while berat.isdigit() == False:
                        print("Berat harus berupa angka!")
                        berat = input("Berat hasil panen (kg, angka bulat): ")

                    print("Kualitas hasil panen:")
                    for nomor, item in enumerate(daftar_kualitas, 1):
                        print(nomor, ".", item)
                    pilih = input("Pilih: ")
                    while pilih not in nomor_kualitas:
                        print("Pilihan tidak valid!")
                        pilih = input("Pilih: ")

                    keterangan = input("Keterangan tambahan: ")
                    if keterangan == "":
                        keterangan = "-"

                    catatan = {
                        "id": id_cari,
                        "nama": tanaman["nama"],
                        "tanggal": tanggal,
                        "jumlah": int(jumlah),
                        "berat": int(berat),
                        "kualitas": daftar_kualitas[int(pilih) - 1],
                        "keterangan": keterangan
                    }
                    data_panen.append(catatan)
                    print("Data panen berhasil disimpan.")

                elif pilih_catat == "2":
                    print("")
                    if not data_panen:
                        print("Belum ada data panen.")
                    for h in data_panen:
                        print("ID tanaman :", h["id"])
                        print("Nama       :", h["nama"])
                        print("Tanggal    :", h["tanggal"])
                        print("Jumlah     :", h["jumlah"])
                        print("Berat      :", h["berat"], "kg")
                        print("Kualitas   :", h["kualitas"])
                        print("Keterangan :", h["keterangan"])
                        print("-------------------------")

                elif pilih_catat == "3":
                    break

                else:
                    print("Pilihan tidak valid!")

        elif pilihan == "7":
            while True:
                print("")
                print("--- LAPORAN DAN REKAPITULASI ---")
                for nomor, item in enumerate(menu_laporan, 1):
                    print(nomor, ".", item)
                pilih_laporan = input("Pilih: ")

                if pilih_laporan == "1":
                    print("")
                    print("=== LAPORAN DATA TANAMAN ===")
                    total = 0
                    jenis_total = 0
                    for t in data_tanaman:
                        print("ID", t["id"], "|", t["nama"], "| Jumlah:", t["jumlah"], "| Lokasi:", t["lokasi"], "| Tanam:", t["tanggal_tanam"])
                        total = total + t["jumlah"]
                        jenis_total = jenis_total + 1
                    print("Total:", jenis_total, "jenis,", total, "tanaman")

                elif pilih_laporan == "2":
                    print("")
                    print("=== LAPORAN KONDISI TANAMAN ===")
                    if not data_kondisi:
                        print("Belum ada data.")
                    for k in data_kondisi:
                        print("ID", k["id"], "|", k["tanggal"], "| daun:", k["daun"], "| batang:", k["batang"], "| tanah:", k["tanah"], "| akar:", k["akar"])

                elif pilih_laporan == "3":
                    print("")
                    print("=== LAPORAN PERAWATAN ===")
                    if not data_perawatan:
                        print("Belum ada data.")
                    jumlah_catatan = 0
                    for p in data_perawatan:
                        print("ID", p["id"], "|", p["jenis"], "|", p["tanggal"], "| berikutnya:", p["jadwal"])
                        jumlah_catatan = jumlah_catatan + 1
                    print("Jumlah catatan perawatan:", jumlah_catatan)

                elif pilih_laporan == "4":
                    print("")
                    print("=== LAPORAN HAMA DAN PENYAKIT ===")
                    if not data_hama:
                        print("Belum ada data.")
                    for h in data_hama:
                        print("ID", h["id"], "|", h["tanggal"], "| gejala:", h["gejala"], "| penanganan:", h["penanganan"])

                elif pilih_laporan == "5":
                    print("")
                    print("=== LAPORAN HASIL PANEN ===")
                    total_berat = 0
                    if not data_panen:
                        print("Belum ada data.")
                    for h in data_panen:
                        print("ID", h["id"], "|", h["nama"], "|", h["tanggal"], "|", h["jumlah"], "|", h["berat"], "kg |", h["kualitas"])
                        total_berat = total_berat + h["berat"]
                    print("Total berat panen:", total_berat, "kg")

                elif pilih_laporan == "6":
                    break

                else:
                    print("Pilihan tidak valid!")

        elif pilihan == "8":
            print("Anda sudah logout.")
            break

        else:
            print("Pilihan tidak valid!")