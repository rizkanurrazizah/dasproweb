def get_kupon(kode, subtotal):
    daftar_kupon = ("MurahMeriah", "TanggalTua", "Merdeka17", "HariIbu")

    if subtotal <= 50000:
        return 0

    if kode in daftar_kupon:
        return 25000
    else:
        return 0

# def get_kupon(k):
#     daftar_kupon = ("MurahMeriah", "TanggalTua", "Merdeka17", "HariIbu")

#     if k in daftar_kupon:
#         # berikan potongan 25rb
#         return 25000
#     else:
#         # tidak ada potongan
#         return 0