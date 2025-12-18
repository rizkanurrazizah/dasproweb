# ===============================================
# Program: Menghitung Luas Segitiga (Versi For Loop)
# Nama File: luas_segitiga_for.py
# ===============================================

print("=== Program Perhitungan Luas Segitiga (for loop) ===")

# Input identitas dan jumlah data
nama = input("Masukkan Nama Mahasiswa: ")
n = int(input("Masukkan Jumlah Segitiga: "))

total_luas = 0  # variabel penjumlahan luas
print("\nIterasi | Alas | Tinggi | Luas")
print("--------------------------------")

# Perulangan for sebanyak n kali
for i in range(1, n + 1):
    print(f"Data ke{i}")
    alas = float(input("Masukkan alas: "))
    tinggi = float(input("Masukkan tinggi: "))

    luas = 0.5 * alas * tinggi
    total_luas += luas  # akumulasi total luas

    print(f"{i:<8} | {alas:<4} | {tinggi:<6} | {luas}\n")

# Hitung rata-rata luas
rata = total_luas / n if n > 0 else 0

# Tampilkan hasil akhir
print("==== HASIL AKHIR ====")
print(f"Nama Mahasiswa : {nama}")
print(f"Jumlah Data    : {n}")
print(f"Total Luas     : {total_luas}")
print(f"Rata-Rata Luas : {rata}")
