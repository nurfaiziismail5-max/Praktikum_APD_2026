status = True
while status == True:
    print(" ==== MENU ====")
    print("1. Profile Kelompok")
    print("2. Bina Damping")
    print("3. Tambah Anggota")
    print("4. Daftar Anggota")
    print("5. Hapus Nama Anggota")
    print("6. Edit Nama Anggota")
    ulang = "ya"
    daftar_anggota = ["Zaid", "Belva", "Al","Ririn","Azka","Johan","Niyah","Falih","Juna","Ibnu","Adam","Faiz","Diyah","Zaky","Rado"]

    pilihan = input(" Pilih Menu : ")
    if pilihan == "1":
        print(" === INTERNET OF THINGS ===")
        print(" Filosofi : Tulisan IOT Menjadi nama kelompok yang melambangkan keterhubungan dan inovasi teknologi, Bentuk wifi melambangkan keterhubungan solidaritas dan kekompakan. Pola heksagonal menggambarkan teknologi inovasi struktur dan kekuatan. Warna biru tua melambangkan kepercayaan, profesionalisme, teknologi dan ke stabilan. Biru muda melambangkan kreativitas, ketenangan, keterbukaan, dan kemudahan "
            )
    elif pilihan == "2" :
        print("- Dzaky Ainur Rahman")
        print("- Muhammadancel Prinata")

    elif pilihan == "3":
        while ulang == "ya":
            tambahan_anggota = input(" Tambah Anggota : ")
            daftar_anggota.append(tambahan_anggota)
            ulang = input("Tambah Lagi (ya/tidak)")
            if ulang != "ya" :
                break

    elif pilihan == "4":
        print(f"Daftar Anggota = {daftar_anggota}")
        break

# PEMBAGIAN TUGAS
# KETUA = AZKA

