# ================================================================
# Ujian Praktik Python
# Materi : Perulangan (for, while, break, continue, nested loop)
# Topik  : Menghitung Luas Beberapa Lingkaran
# ================================================================

# Input Data Mahasiswa
print("=== PROGRAM PENGHITUNG LUAS LINGKARAN ===")
nama = input("Masukkan Nama Mahasiswa : ")
nim = input("Masukkan NIM Mahasiswa  : ")
n = int(input("Masukkan jumlah lingkaran: "))

# Inisialisasi variabel
daftar_luas = []      # Menyimpan hasil luas setiap lingkaran
pi = 3.14             # Nilai konstanta π
batas_iterasi = 10    # Batas maksimum lingkaran yang boleh dihitung

# ---------------------------------------------------------------
# Perulangan FOR untuk input jari-jari dan perhitungan luas
# ---------------------------------------------------------------
for i in range(1, n + 1):
    if i > batas_iterasi:
        print("Perhitungan dihentikan (batas 10 lingkaran)")
        break  # menghentikan perulangan jika melewati batas
    
    r = float(input(f"Lingkaran ke-{i}, masukkan jari-jari (r): "))
    
    if r == 0:
        print("Jari-jari bernilai 0 → dilewati (continue)\n")
        continue  # melewati perhitungan tanpa error
    
    luas = pi * (r ** 2)
    daftar_luas.append((i, r, luas))  # simpan tuple hasil (iterasi, jari-jari, luas)

# ---------------------------------------------------------------
# Perulangan WHILE untuk menampilkan trace table hasil perhitungan
# ---------------------------------------------------------------
print("\n==== TRACE TABLE ====")
print("Iterasi | Jari-jari | Luas Lingkaran")
print("-------------------------------------")

index = 0
while index < len(daftar_luas):
    iterasi, r, luas = daftar_luas[index]
    print(f"{iterasi:<8}| {r:<10}| {luas:.2f}")
    index += 1

# ---------------------------------------------------------------
# Hitung total dan rata-rata luas
# ---------------------------------------------------------------
if len(daftar_luas) > 0:
    total_luas = sum([data[2] for data in daftar_luas])
    rata2_luas = total_luas / len(daftar_luas)
else:
    total_luas = 0
    rata2_luas = 0

# ---------------------------------------------------------------
# Nested Loop untuk menampilkan pola segitiga bintang
# ---------------------------------------------------------------
print("\nPola Segitiga:")
for i in range(1, len(daftar_luas) + 1):
    for j in range(i):
        print("*", end="")
    print()  # pindah baris setelah satu baris selesai

# ---------------------------------------------------------------
# Hasil akhir program
# ---------------------------------------------------------------
print("\n==== HASIL AKHIR ====")
print(f"Nama Mahasiswa : {nama}")
print(f"NIM Mahasiswa  : {nim}")
print(f"Jumlah Data    : {len(daftar_luas)} Lingkaran")
print(f"Total Luas     : {total_luas:.2f}")
print(f"Rata-rata Luas : {rata2_luas:.2f}")

print("\nProgram selesai. Terima kasih!")
