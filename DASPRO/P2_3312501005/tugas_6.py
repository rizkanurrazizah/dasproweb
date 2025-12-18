nilai_dasar_pemrograman = float(input("Masukkan nilai Mata Kuliah Dasar Pemrograman: "))
nilai_pemrograman_web   = float(input("Masukkan nilai Mata Kuliah Pemrograman Web: "))
nilai_matematika        = float(input("Masukkan nilai Mata Kuliah Matematika: "))

total = nilai_dasar_pemrograman + nilai_pemrograman_web + nilai_matematika

rata_rata = total / 3

print(f"Rata-rata nilai dari 3 mata kuliah adalah: {rata_rata}")