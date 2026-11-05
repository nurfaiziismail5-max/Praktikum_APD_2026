"""Kondisi, perawatan, hama/penyakit, panen, dan status perawatan."""
import data
from tampilan import tampil_menu, tampil_tabel, pesan_sukses, pesan_error, pesan_info, beri_warna, HIJAU, MERAH, KUNING
from validasi import input_teks, input_angka, input_tanggal, pilih_dari_menu, ambil_id_tanaman
from prettytable import PrettyTable


def tambah_kondisi():
    id_cari = ambil_id_tanaman()
    if id_cari is None:
        return
    catatan = {"id": id_cari}
    for nama_k in data.pilihan_kondisi:
        catatan[nama_k] = pilih_dari_menu("Kondisi " + nama_k, data.pilihan_kondisi[nama_k], "Pilih: ")
    catatan["tahap"] = data.data_tanaman[id_cari]["tahap"]
    catatan["tanggal"] = input_tanggal("Tanggal pemeriksaan (DD-MM-YYYY, Enter = hari ini): ", default_hari_ini=True)
    data.id_terakhir["kondisi"] += 1
    data.data_kondisi[data.id_terakhir["kondisi"]] = catatan
    pesan_sukses("Catatan kondisi berhasil disimpan.")
    if catatan["daun"] == "kuning" and catatan["tanah"] == "kering":
        pesan_info("Keterangan: tanaman perlu diperiksa dan mungkin membutuhkan perawatan.")


def tambah_perawatan():
    id_cari = ambil_id_tanaman()
    if id_cari is None:
        return
    jenis = pilih_dari_menu("Jenis perawatan", data.daftar_perawatan, "Pilih: ")
    tanggal = input_tanggal("Tanggal perawatan (DD-MM-YYYY, Enter = hari ini): ", default_hari_ini=True)
    jadwal = input_tanggal("Jadwal berikutnya (DD-MM-YYYY, kosongkan jika tidak ada): ", boleh_kosong=True)
    if jadwal is None:
        jadwal = "-"
    keterangan = input_teks("Keterangan/hasil perawatan: ", True)
    if keterangan == "":
        keterangan = "-"
    data.id_terakhir["perawatan"] += 1
    data.data_perawatan[data.id_terakhir["perawatan"]] = {
        "id": id_cari, "jenis": jenis, "tanggal": tanggal,
        "jadwal": jadwal, "keterangan": keterangan}
    pesan_sukses("Catatan perawatan berhasil disimpan.")


def tambah_hama():
    id_cari = ambil_id_tanaman()
    if id_cari is None:
        return
    tanggal = input_tanggal("Tanggal pemeriksaan (DD-MM-YYYY, Enter = hari ini): ", default_hari_ini=True)
    gejala = input_teks("Gejala yang ditemukan: ")
    dugaan = input_teks("Hama/penyakit yang dicurigai: ", True)
    if dugaan == "":
        dugaan = "Belum diketahui"
    penanganan = input_teks("Tindakan penanganan: ", True)
    if penanganan == "":
        penanganan = "-"
    pencegahan = input_teks("Tindakan pencegahan: ", True)
    if pencegahan == "":
        pencegahan = "-"
    hasil = input_teks("Hasil pemeriksaan berikutnya: ", True)
    if hasil == "":
        hasil = "-"
    data.id_terakhir["hama"] += 1
    data.data_hama[data.id_terakhir["hama"]] = {
        "id": id_cari, "tanggal": tanggal, "gejala": gejala, "dugaan": dugaan,
        "penanganan": penanganan, "pencegahan": pencegahan, "hasil": hasil}
    pesan_sukses("Catatan berhasil disimpan.")
    pesan_info("Saran: lakukan pemeriksaan lebih lanjut, karena gejala belum tentu menunjukkan satu jenis hama/penyakit.")


def tambah_panen():
    id_cari = ambil_id_tanaman()
    if id_cari is None:
        return
    tanggal = input_tanggal("Tanggal panen (DD-MM-YYYY, Enter = hari ini): ", default_hari_ini=True)
    jumlah = input_angka("Jumlah hasil panen: ")
    berat = input_angka("Berat hasil panen (kg, angka bulat): ")
    kualitas = pilih_dari_menu("Kualitas hasil panen", data.daftar_kualitas, "Pilih: ")
    keterangan = input_teks("Keterangan tambahan: ", True)
    if keterangan == "":
        keterangan = "-"
    data.id_terakhir["panen"] += 1
    data.data_panen[data.id_terakhir["panen"]] = {
        "id": id_cari, "nama": data.data_tanaman[id_cari]["nama"], "tanggal": tanggal,
        "jumlah": jumlah, "berat": berat, "kualitas": kualitas,
        "keterangan": keterangan}
    pesan_sukses("Data panen berhasil disimpan.")


def menu_catatan(judul, fungsi_tambah, data_catatan, kolom):
    while True:
        tampil_menu(judul, data.menu_catat)
        pilih = input("Pilih: ")
        if pilih == "1":
            fungsi_tambah()
        elif pilih == "2":
            tampil_tabel(judul, kolom, data_catatan)
        elif pilih == "3":
            break
        else:
            pesan_error("Pilihan tidak valid!")


def status_tanaman(id_t):
    """Menentukan status perawatan tanaman dari catatan kondisi terakhir."""
    kondisi = None
    jadwal = "-"
    for no in data.data_kondisi:
        if data.data_kondisi[no]["id"] == id_t:
            kondisi = data.data_kondisi[no]
    for no in data.data_perawatan:
        if data.data_perawatan[no]["id"] == id_t and data.data_perawatan[no]["jadwal"] != "-":
            jadwal = data.data_perawatan[no]["jadwal"]

    if kondisi is None:
        status = "Perlu Pemeriksaan (belum ada data kondisi)"
    elif kondisi["daun"] == "kuning" and kondisi["tanah"] == "kering":
        status = "Perlu Perawatan"
    elif kondisi["daun"] == "hijau" and kondisi["tanah"] != "kering" and kondisi["batang"] == "normal" and kondisi["akar"] == "normal":
        status = "Sehat"
    else:
        status = "Perlu Pemeriksaan"
    return status, jadwal


def cek_status_perawatan():
    tabel = PrettyTable(["ID", "Nama", "Status", "Perawatan Terjadwal"])
    tabel.title = "PENGECEKAN STATUS PERAWATAN"
    tabel.align = "l"
    for id_t in data.data_tanaman:
        status, jadwal = status_tanaman(id_t)
        if status == "Sehat":
            status = beri_warna(status, HIJAU)
        elif status == "Perlu Perawatan":
            status = beri_warna(status, MERAH)
        else:
            status = beri_warna(status, KUNING)
        tabel.add_row([id_t, data.data_tanaman[id_t]["nama"], status, jadwal])
    print("")
    if not data.data_tanaman:
        print("Belum ada data tanaman.")
    else:
        print(tabel)
