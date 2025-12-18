nama = input("Masukkan nama mahasiswa: ")
dasar_pemrograman = float(input("Masukkan nilai Dasar Pemrograman: "))
pemrograman_web = float(input("Masukkan nilai Pemrograman Web: "))
matematika = float(input("Masukkan nilai Matematika: "))
total_nilai = dasar_pemrograman + pemrograman_web + matematika
rata_rata = total_nilai / 3


print(f"Mahasiswa {nama} memiliki rata-rata nilai {rata_rata}")
