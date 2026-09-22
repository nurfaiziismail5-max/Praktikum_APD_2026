komponen_1 = 120000
komponen_2 = 135000
komponen_3 = 150000
komponen_4 = 175000
komponen_5 = 200000
komponen_6 = 220000
biaya_admin = 15000

harga_komponen = [komponen_1, komponen_2, komponen_3, komponen_4, komponen_5, komponen_6]

total_biaya = komponen_1 + komponen_2 + komponen_3 + komponen_4 + komponen_5 + komponen_6 + biaya_admin

rata_rata = total_biaya / len(harga_komponen)

nim = 77

bolean = nim != rata_rata

kurs_gbp = 20500
total_biaya_gbp = total_biaya / kurs_gbp

print("Total Biaya (IDR) :", total_biaya)
print("Rata-Rata :", rata_rata)
print("NIM :", nim)
print("Hasil Bolean :", bolean)

print("\n--- Output Poin Plus ---")
print("List Harga Komponen  :")
for harga in harga_komponen : print(f"-{harga}")
print("Total Biaya (GBP)    :", total_biaya_gbp)

print("Slice Komponen 1 - 4 :", harga_komponen[-6:-2])