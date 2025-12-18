print ("===Program Belanja Budi===")

barang1 = int(input("Masukkan harga barang 1:"))
barang2 = int(input("Masukkan harga barang 2:"))
barang3 = int(input("Masukkan harga barang 3:"))
barang4 = int(input("Masukkan harga barang 4:"))
barang5 = int(input("Masukkan harga barang 5:"))

total = barang1 +  barang2 + barang3 + barang4 + barang5
print(f"Total bayar adalah : Rp {total}")

if total <= 20000 :
    print