nama_mahasiswa = input("Masukkan nama mahasiswa: ")

nilai_dasar_pemrograman = float(input("Masukkan nilai Mata Kuliah Dasar Pemrograman: "))
nilai_pemrograman_web   = float(input("Masukkan nilai Mata Kuliah Pemrograman Web: "))
nilai_matematika        = float(input("Masukkan nilai Mata Kuliah Matematika: "))

total = nilai_dasar_pemrograman + nilai_pemrograman_web + nilai_matematika

jumlah_matakuliah = 3
rata_rata = total / jumlah_matakuliah

print(f"Total Nilai     : {total}")
print(f"Rata-rata Nilai : {rata_rata}")
print(f"Halo {nama_mahasiswa}")

