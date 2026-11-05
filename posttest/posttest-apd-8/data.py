"""Menyimpan semua data dan konstanta program."""
import hashlib


def buat_hash(teks):
    """Mengubah teks menjadi hash SHA-256 (password tidak disimpan polos)."""
    return hashlib.sha256(teks.encode()).hexdigest()


data_user = {
    "admin": {"password": buat_hash("admin1"), "role": "admin"},
    "pengguna": {"password": buat_hash("pengguna1"), "role": "pengguna"}
}

data_tanaman = {
    1: {"nama": "Mangga", "jenis": "Buah", "tanggal_tanam": "01-01-2026", "jumlah": 15, "lokasi": "Kebun A", "media": "Tanah", "tahap": "Vegetatif"},
    2: {"nama": "Apel", "jenis": "Buah", "tanggal_tanam": "01-01-2026", "jumlah": 10, "lokasi": "Kebun B", "media": "Tanah", "tahap": "Vegetatif"},
    3: {"nama": "Anggur", "jenis": "Buah", "tanggal_tanam": "01-01-2026", "jumlah": 10, "lokasi": "Kebun C", "media": "Tanah", "tahap": "Berbunga"}
}

data_kondisi = {}
data_perawatan = {}
data_hama = {}
data_panen = {}

# ID terakhir tiap data (dictionary supaya bisa diubah dari file lain tanpa global)
id_terakhir = {"tanaman": 3, "kondisi": 0, "perawatan": 0, "hama": 0, "panen": 0}

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

# Format kolom: (judul kolom, kunci data, satuan)
kolom_tanaman = [("Nama", "nama", ""), ("Jenis", "jenis", ""), ("Tanggal Tanam", "tanggal_tanam", ""),
                 ("Jumlah", "jumlah", ""), ("Lokasi", "lokasi", ""), ("Media", "media", ""),
                 ("Tahap", "tahap", "")]
kolom_ringkas_tanaman = [("Nama", "nama", ""), ("Jumlah", "jumlah", ""), ("Lokasi", "lokasi", ""),
                         ("Tanggal Tanam", "tanggal_tanam", "")]
kolom_kondisi = [("ID Tanaman", "id", ""), ("Tanggal", "tanggal", ""), ("Daun", "daun", ""),
                 ("Batang", "batang", ""), ("Tanah", "tanah", ""), ("Akar", "akar", ""),
                 ("Tahap", "tahap", "")]
kolom_perawatan = [("ID Tanaman", "id", ""), ("Jenis Perawatan", "jenis", ""), ("Tanggal", "tanggal", ""),
                   ("Jadwal Berikutnya", "jadwal", ""), ("Keterangan", "keterangan", "")]
kolom_hama = [("ID Tanaman", "id", ""), ("Tanggal", "tanggal", ""), ("Gejala", "gejala", ""),
              ("Dugaan", "dugaan", ""), ("Penanganan", "penanganan", ""),
              ("Pencegahan", "pencegahan", ""), ("Hasil Lanjut", "hasil", "")]
kolom_panen = [("ID Tanaman", "id", ""), ("Nama", "nama", ""), ("Tanggal", "tanggal", ""),
               ("Jumlah", "jumlah", ""), ("Berat", "berat", " kg"), ("Kualitas", "kualitas", ""),
               ("Keterangan", "keterangan", "")]
