"""Fungsi perhitungan (termasuk rekursif)."""
import data


def jumlah_rekursif(daftar, indeks=0):
    """Menjumlahkan isi list secara rekursif."""
    if indeks >= len(daftar):
        return 0
    return daftar[indeks] + jumlah_rekursif(daftar, indeks + 1)


def hitung_total_tanaman():
    """Mengembalikan total jenis dan total jumlah tanaman."""
    daftar_jumlah = []
    for id_t in data.data_tanaman:
        daftar_jumlah.append(data.data_tanaman[id_t]["jumlah"])
    jenis = len(daftar_jumlah)
    total = jumlah_rekursif(daftar_jumlah)
    return jenis, total
