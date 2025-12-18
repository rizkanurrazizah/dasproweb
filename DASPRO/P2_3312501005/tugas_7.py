nama_mahasiswa = input("inputkan nama mahasisawa:")
nilai_dasar_pemrograman = float(input("Masukkan nilai Mata Kuliah Dasar Pemrograman: "))
nilai_pemrograman_web   = float(input("Masukkan nilai Mata Kuliah Pemrograman Web: "))
nilai_matematika        = float(input("Masukkan nilai Mata Kuliah Matematika: "))

total = nilai_dasar_pemrograman + nilai_pemrograman_web + nilai_matematika

rata_rata = total / 3

print(f"Nama Mahasiswa  : {nama_mahasiswa}")
print(f"Rata-rata Nilai : {rata_rata}")

print(f"Mahasiswa {nama_mahasiswa} memiliki rata-rata {rata_rata}")