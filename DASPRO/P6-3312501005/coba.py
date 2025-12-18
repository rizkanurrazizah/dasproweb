# # =============================================================
# # Ujian Praktik Python
# # Materi : Perulangan for
# # Tujuan : Menghitung jumlah dan rata-rata bilangan
# # =============================================================

# print("=== PROGRAM PERULANGAN FOR ===")

# nama = input("Masukkan Nama Mahasiswa : ")
# nim = input("Masukkan NIM Mahasiswa  : ")
# n = int(input("Masukkan jumlah bilangan : "))

# daftar_angka = []

# # Perulangan for untuk input angka
# for i in range(1, n + 1):
#     angka = float(input(f"Bilangan ke-{i} : "))

#     if angka < 0:
#         print("Angka negatif dilewati!")
#         continue

#     daftar_angka.append(angka)

# # Hitung total menggunakan for
# total = 0
# for nilai in daftar_angka:
#     total += nilai

# # Hitung rata-rata
# rata_rata = total / len(daftar_angka) if daftar_angka else 0

# # Tampilkan hasil
# print("\n==== HASIL PERHITUNGAN ====")
# print(f"Nama Mahasiswa : {nama}")
# print(f"NIM Mahasiswa  : {nim}")
# print(f"Jumlah Data    : {len(daftar_angka)}")
# print(f"Total Bilangan : {total}")
# print(f"Rata-rata      : {rata_rata:.2f}")


# ===============================================
# Program: Menghitung Luas Segitiga (Versi For Loop)
# Nama File: luas_segitiga_for.py
# ===============================================

# print("=== Program Perhitungan Luas Segitiga (for loop) ===")

# # Input identitas dan jumlah data
# nama = input("Masukkan Nama Mahasiswa: ")
# n = int(input("Masukkan Jumlah Segitiga: "))

# total_luas = 0  # variabel penjumlahan luas
# print("\nIterasi | Alas | Tinggi | Luas")
# print("--------------------------------")

# # Perulangan for sebanyak n kali
# for i in range(1, n + 1):
#     print(f"Data ke-{i}")
#     alas = float(input("Masukkan alas: "))
#     tinggi = float(input("Masukkan tinggi: "))

#     luas = 0.5 * alas * tinggi
#     total_luas += luas  # akumulasi total luas

#     print(f"{i:<8} | {alas:<4} | {tinggi:<6} | {luas}\n")

# # Hitung rata-rata luas
# rata = total_luas / n if n > 0 else 0

# # Tampilkan hasil akhir
# print("==== HASIL AKHIR ====")
# print(f"Nama Mahasiswa : {nama}")
# print(f"Jumlah Data    : {n}")
# print(f"Total Luas     : {total_luas}")
# print(f"Rata-Rata Luas : {rata}")
