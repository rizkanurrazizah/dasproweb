import diskon
from kupon import get_kupon

def hitung_total(subtotal, potongan):
    return subtotal - potongan

def kasir():
    harga_satuan = int(input("Input harga barang: "))
    jumlah_barang = int(input("Input jumlah barang: "))

    jenis_member = input("Input member: (silver/gold/platinum) ")
    persen_diskon = diskon.get_diskon(jenis_member)

    subtotal = harga_satuan * jumlah_barang
    nilai_diskon = subtotal * persen_diskon

    kode_kupon = input("Input kupon (jika ada): ")
    nilai_kupon = get_kupon(kode_kupon, subtotal)

    total_bayar = hitung_total(subtotal, nilai_diskon) - nilai_kupon
    print(f"Harga yang harus dibayar adalah: Rp. {total_bayar}")

kasir()

# import diskon 
# import kupon 
 
# def hitung_total(subtotal, potongan): 
#     return subtotal - potongan 
 
# def kasir(): 
#     harga_satuan = int(input("Input harga barang: ")) 
#     jumlah_barang = int(input("Input jumlah barang: ")) 
 
#     jenis_member = input("Input member: (silver/gold/platinum) ") 
#     persen_diskon = diskon.get_diskon(jenis_member) 
 
#     subtotal = harga_satuan * jumlah_barang 
#     nilai_diskon = subtotal * persen_diskon 
 
#     kode_kupon = input("Input kupon (jika ada): ") 
#     nilai_kupon = kupon.get_kupon(kode_kupon) 
 
#     total_bayar = hitung_total(subtotal, nilai_diskon) - nilai_kupon 
#     print(f"Harga yang harus dibayar adalah: Rp. {total_bayar}") 
 
# kasir() 