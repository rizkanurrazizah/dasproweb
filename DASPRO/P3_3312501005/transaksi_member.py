nama_barang = input("Barang apa yang anda beli??: ")
jumlah = int(input("Berapa jumlah barang yang dibeli??: "))
harga = int(input("Berapa harga barang per item???: "))

tanya_diskon = input("Ada membernya kak?? (ya/tidak): ")

if tanya_diskon == "ya":
    member = input("Input jenis member ?? (silver/gold/platinum): ")
    if member == "platinum":
        diskon = 75
    elif member == "gold":
        diskon = 50
    elif member == "silver":
        lama = int(input("Berapa lama menjadi member (tahun)? "))
        if lama >= 2:
            diskon = 30
        else:
            diskon = 25
    
    else:
        print("Jenis member tidak dikenali. Diskon tidak diberikan.")
        diskon = 0
else:
    diskon = 0

total = (jumlah * harga) * (100 - diskon) / 100


print(f"Total harga "+nama_barang+" adalah Rp."+ str(total))
    