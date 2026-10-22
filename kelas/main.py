A. Data User dan Login
Bagian ini digunakan untuk menyimpan akun pengguna serta memeriksa username dan password. Username dipakai sebagai key dictionary.
data_user = {
    "admin": {"password": "admin1", "role": "admin"},
    "petugas": {"password": "petugas1", "role": "petugas"}
}

username = input("Username: ")
if username == "0":
    print("Program selesai.")
    break
password = input("Password: ")

if username not in data_user or data_user[username]["password"] != password:
    print("Username atau password salah!")
    continue

role = data_user[username]["role"]
print("Login berhasil. Selamat datang,", username, "(" + role + ")")
B. Data Tanaman
Bagian ini merupakan penyimpanan data awal tanaman menggunakan struktur dictionary. ID tanaman dipakai sebagai key, sedangkan catatan kondisi, perawatan, hama, dan panen disimpan dalam dictionary dengan nomor catatan sebagai key.
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
C. Menu Utama
Menu utama digunakan untuk mengakses seluruh fitur program. Nomor menu menjadi key dan nama menu menjadi value.
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

print("======= MENU UTAMA =======")
for nomor in menu_utama:
    print(nomor, ".", menu_utama[nomor])
pilihan = input("Pilih menu: ")
D. Tambah Tanaman
Bagian ini berfungsi untuk menambahkan tanaman baru. Hanya pengguna dengan role admin yang diperbolehkan menambah data. Tanaman baru disimpan ke dalam data_tanaman dengan ID baru sebagai key.
daftar_tahap = {"1": "Bibit", "2": "Vegetatif", "3": "Berbunga", "4": "Berbuah"}

if role != "admin":
    print("Maaf, hanya admin yang boleh menambah tanaman!")
    continue

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
for nomor in daftar_tahap:
    print(nomor, ".", daftar_tahap[nomor])
pilih_tahap = input("Pilih tahap: ")
while pilih_tahap not in daftar_tahap:
    print("Pilihan tidak valid!")
    pilih_tahap = input("Pilih tahap: ")

id_terakhir = id_terakhir + 1
data_tanaman[id_terakhir] = {
    "nama": nama,
    "jenis": jenis,
    "tanggal_tanam": tanggal,
    "jumlah": int(jumlah),
    "lokasi": lokasi,
    "media": media,
    "tahap": daftar_tahap[pilih_tahap]
}
print("Tanaman berhasil ditambahkan dengan ID", id_terakhir)
E. Ubah dan Hapus Tanaman
Bagian ini menggunakan ID tanaman untuk mencari data yang akan diubah atau dihapus. Pencarian cukup memakai in karena ID adalah key dictionary.
Mengubah data tanaman
id_input = input("Masukkan ID tanaman yang diubah: ")
if id_input.isdigit() == False:
    print("ID harus berupa angka!")
    continue
id_cari = int(id_input)

if id_cari not in data_tanaman:
    print("ID tanaman tidak ditemukan!")
    continue
tanaman = data_tanaman[id_cari]

print("Kosongkan (tekan Enter) jika tidak ingin mengubah.")
baru = input("Nama [" + tanaman["nama"] + "]: ")
if baru != "":
    tanaman["nama"] = baru
baru = input("Jumlah [" + str(tanaman["jumlah"]) + "]: ")
while baru != "" and baru.isdigit() == False:
    print("Jumlah harus berupa angka!")
    baru = input("Jumlah [" + str(tanaman["jumlah"]) + "]: ")
if baru != "":
    tanaman["jumlah"] = int(baru)

baru = input("Tahap [" + tanaman["tahap"] + "] (nomor): ")
while baru != "" and baru not in daftar_tahap:
    print("Pilihan tidak valid!")
    baru = input("Tahap [" + tanaman["tahap"] + "] (nomor): ")
if baru != "":
    tanaman["tahap"] = daftar_tahap[baru]

print("Data tanaman berhasil diubah.")
Menghapus data tanaman
if role != "admin":
    print("Maaf, hanya admin yang boleh menghapus tanaman!")
    continue

id_input = input("Masukkan ID tanaman yang dihapus: ")
if id_input.isdigit() == False:
    print("ID harus berupa angka!")
    continue
id_cari = int(id_input)

if id_cari not in data_tanaman:
    print("ID tanaman tidak ditemukan!")
    continue
tanaman = data_tanaman[id_cari]

yakin = input("Yakin ingin menghapus " + tanaman["nama"] + "? (ya/tidak): ")
if yakin == "ya":
    del data_tanaman[id_cari]

    kondisi_baru = {}
    for no in data_kondisi:
        if data_kondisi[no]["id"] != id_cari:
            kondisi_baru[no] = data_kondisi[no]
    data_kondisi = kondisi_baru

    perawatan_baru = {}
    for no in data_perawatan:
        if data_perawatan[no]["id"] != id_cari:
            perawatan_baru[no] = data_perawatan[no]
    data_perawatan = perawatan_baru

    hama_baru = {}
    for no in data_hama:
        if data_hama[no]["id"] != id_cari:
            hama_baru[no] = data_hama[no]
    data_hama = hama_baru

    panen_baru = {}
    for no in data_panen:
        if data_panen[no]["id"] != id_cari:
            panen_baru[no] = data_panen[no]
    data_panen = panen_baru

    print("Tanaman berhasil dihapus.")
else:
    print("Penghapusan dibatalkan.")
F. Pemantauan Kondisi Tanaman
Fitur ini mencatat kondisi daun, batang, tanah, dan akar tanaman. Pilihan kondisi disimpan dalam dictionary bersarang, dengan nama bagian tanaman sebagai key.
pilihan_kondisi = {
    "daun": {"1": "hijau", "2": "kuning", "3": "layu"},
    "batang": {"1": "normal", "2": "rusak"},
    "tanah": {"1": "lembap", "2": "normal", "3": "kering"},
    "akar": {"1": "normal", "2": "bermasalah"}
}

id_input = input("Masukkan ID tanaman: ")
if id_input.isdigit() == False:
    print("ID harus berupa angka!")
    continue
id_cari = int(id_input)

if id_cari not in data_tanaman:
    print("ID tanaman tidak ditemukan!")
    continue
tanaman = data_tanaman[id_cari]

catatan = {"id": id_cari}

for nama_k in pilihan_kondisi:
    print("")
    print("Kondisi", nama_k, ":")
    for nomor in pilihan_kondisi[nama_k]:
        print(nomor, ".", pilihan_kondisi[nama_k][nomor])
    pilih = input("Pilih: ")
    while pilih not in pilihan_kondisi[nama_k]:
        print("Pilihan tidak valid!")
        pilih = input("Pilih: ")
    catatan[nama_k] = pilihan_kondisi[nama_k][pilih]

catatan["tahap"] = tanaman["tahap"]
catatan["tanggal"] = input("Tanggal pemeriksaan (contoh 10-10-2026): ")
id_kondisi = id_kondisi + 1
data_kondisi[id_kondisi] = catatan
print("Catatan kondisi berhasil disimpan.")

if catatan["daun"] == "kuning" and catatan["tanah"] == "kering":
    print("Keterangan: tanaman perlu diperiksa dan mungkin membutuhkan perawatan.")
G. Jadwal dan Riwayat Perawatan
Digunakan untuk mencatat jenis perawatan yang dilakukan beserta jadwal perawatan berikutnya.
daftar_perawatan = {
    "1": "Penyiraman",
    "2": "Pemberian pupuk",
    "3": "Pemangkasan",
    "4": "Pembersihan gulma",
    "5": "Pemeriksaan kondisi",
    "6": "Lainnya"
}

id_input = input("Masukkan ID tanaman: ")
if id_input.isdigit() == False:
    print("ID harus berupa angka!")
    continue
id_cari = int(id_input)

if id_cari not in data_tanaman:
    print("ID tanaman tidak ditemukan!")
    continue

print("Jenis perawatan:")
for nomor in daftar_perawatan:
    print(nomor, ".", daftar_perawatan[nomor])
pilih = input("Pilih: ")
while pilih not in daftar_perawatan:
    print("Pilihan tidak valid!")
    pilih = input("Pilih: ")

tanggal = input("Tanggal perawatan (contoh 10-10-2026): ")
jadwal = input("Jadwal berikutnya (kosongkan jika tidak ada): ")
if jadwal == "":
    jadwal = "-"
keterangan = input("Keterangan/hasil perawatan: ")
if keterangan == "":
    keterangan = "-"

id_perawatan = id_perawatan + 1
data_perawatan[id_perawatan] = {
    "id": id_cari,
    "jenis": daftar_perawatan[pilih],
    "tanggal": tanggal,
    "jadwal": jadwal,
    "keterangan": keterangan
}
print("Catatan perawatan berhasil disimpan.")
H. Pengecekan Status Perawatan
Sistem menentukan status tanaman berdasarkan catatan kondisi terakhir.
for id_t in data_tanaman:
    t = data_tanaman[id_t]

    ada_kondisi = False
    for no in data_kondisi:
        if data_kondisi[no]["id"] == id_t:
            ada_kondisi = True
            kondisi = data_kondisi[no]

    ada_jadwal = False
    for no in data_perawatan:
        if data_perawatan[no]["id"] == id_t and data_perawatan[no]["jadwal"] != "-":
            ada_jadwal = True
            jadwal = data_perawatan[no]["jadwal"]

    if ada_kondisi == False:
        status = "Perlu Pemeriksaan (belum ada data kondisi)"
    elif kondisi["daun"] == "kuning" and kondisi["tanah"] == "kering":
        status = "Perlu Perawatan"
    elif kondisi["daun"] == "hijau" and kondisi["tanah"] != "kering" and kondisi["batang"] == "normal" and kondisi["akar"] == "normal":
        status = "Sehat"
    else:
        status = "Perlu Pemeriksaan"

    print("ID", id_t, "-", t["nama"], ":", status)
    if ada_jadwal == True:
        print("    Perawatan Terjadwal:", jadwal)
I. Pemantauan Hama dan Penyakit
Digunakan untuk menyimpan hasil pemeriksaan gejala hama atau penyakit tanaman.
id_input = input("Masukkan ID tanaman: ")
if id_input.isdigit() == False:
    print("ID harus berupa angka!")
    continue
id_cari = int(id_input)

if id_cari not in data_tanaman:
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

id_hama = id_hama + 1
data_hama[id_hama] = {
    "id": id_cari,
    "tanggal": tanggal,
    "gejala": gejala,
    "dugaan": dugaan,
    "penanganan": penanganan,
    "pencegahan": pencegahan,
    "hasil": hasil
}
print("Catatan berhasil disimpan.")
print("Saran: lakukan pemeriksaan lebih lanjut, karena gejala belum tentu menunjukkan satu jenis hama/penyakit.")
J. Data Panen
Bagian ini digunakan untuk mencatat hasil produksi tanaman.
daftar_kualitas = {"1": "Baik", "2": "Cukup", "3": "Kurang"}

id_input = input("Masukkan ID tanaman yang dipanen: ")
if id_input.isdigit() == False:
    print("ID harus berupa angka!")
    continue
id_cari = int(id_input)

if id_cari not in data_tanaman:
    print("ID tanaman tidak ditemukan!")
    continue
tanaman = data_tanaman[id_cari]

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
for nomor in daftar_kualitas:
    print(nomor, ".", daftar_kualitas[nomor])
pilih = input("Pilih: ")
while pilih not in daftar_kualitas:
    print("Pilihan tidak valid!")
    pilih = input("Pilih: ")

keterangan = input("Keterangan tambahan: ")
if keterangan == "":
    keterangan = "-"

id_panen = id_panen + 1
data_panen[id_panen] = {
    "id": id_cari,
    "nama": tanaman["nama"],
    "tanggal": tanggal,
    "jumlah": int(jumlah),
    "berat": int(berat),
    "kualitas": daftar_kualitas[pilih],
    "keterangan": keterangan
}
print("Data panen berhasil disimpan.")
K. Laporan dan Rekapitulasi
Bagian ini digunakan untuk menghitung total tanaman dan total berat hasil panen.
print("=== LAPORAN DATA TANAMAN ===")
total = 0
jenis_total = 0
for id_t in data_tanaman:
    t = data_tanaman[id_t]
    print("ID", id_t, "|", t["nama"], "| Jumlah:", t["jumlah"], "| Lokasi:", t["lokasi"], "| Tanam:", t["tanggal_tanam"])
    total = total + t["jumlah"]
    jenis_total = jenis_total + 1
print("Total:", jenis_total, "jenis,", total, "tanaman")

print("=== LAPORAN HASIL PANEN ===")
total_berat = 0
if not data_panen:
    print("Belum ada data.")
for no in data_panen:
    h = data_panen[no]
    print("ID", h["id"], "|", h["nama"], "|", h["tanggal"], "|", h["jumlah"], "|", h["berat"], "kg |", h["kualitas"])
    total_berat = total_berat + h["berat"]
print("Total berat panen:", total_berat, "kg")
