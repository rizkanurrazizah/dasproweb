print("=== Program Belanja Lina")

barang1 = int(input("Masukkan harga barang 1: "))
barang2 = int(input("Masukkan harga barang 2: "))
barang3 = int(input("Masukkan harga barang 3: "))
barang4 = int(input("Masukkan harga barang 4: "))
barang5 = int(input("Masukkan harga barang 5: "))

total = barang1 + barang2 + barang3 + barang4 + barang5
print(f"Total bayar: Rp {total}")

if total <= 50000:
    print("Murah")
elif total <= 100000:
    print("Kategori Normal")
elif total <= 150000:
    print("Kategori Cukup Mahal")
elif total <= 200000:
    print("Kategori Mahal")
else:
    print("Kategori Sangat Mahal")