print("=== Program Perhitungan Luas Segitiga (while loop) ===")

# Input nama mahasiswa
nama = input("Masukkan Nama Mahasiswa: ")

lanjut = "y"
total_luas = 0
jumlah_data = 0

# Perulangan while selama pengguna ingin melanjutkan
while lanjut == "y":
    alas = float(input("Masukkan alas segitiga: "))
    tinggi = float(input("Masukkan tinggi segitiga: "))

    luas = 0.5 * alas * tinggi
    total_luas += luas
    jumlah_data += 1

    print(f"Luas segitiga ke-{jumlah_data} = {luas}")

# Setelah keluar dari loop, tampilkan hasil akhir
print("\n==== HASIL AKHIR ====")
print(f"Nama Mahasiswa : {nama}")
print(f"Jumlah Data    : {jumlah_data}")
print(f"Total Luas     : {total_luas}")

# Jika ingin, tambahkan rata-rata luas
if jumlah_data > 0:
    print(f"Rata-Rata Luas : {total_luas / jumlah_data}")
else:
    print("Tidak ada data yang dihitung.")
