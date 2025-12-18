# import bangundatar as bd

# alas = int(input("Input alas: "))
# tinggi = int(input("Input tinggi: "))

# luas_segitiga = bd.luas_segitiga(alas, tinggi)

# print(f"Luas seigitiga adalah {luas_segitiga}")


import bangundatar as bd

print("=== Hitung Bangun Datar ===")

a = int(input("Input alas segitiga: "))
t = int(input("Input tinggi segitiga: "))
luas_segitiga = bd.luas_segitiga(a, t)
print(f"Luas segitiga adalah {luas_segitiga}")

s = int(input("Input sisi persegi: "))
luas_persegi = bd.luas_persegi()
print(f"Luas persegi adalah {luas_persegi}")

p = int(input("Input panjang persegi panjang: "))
l = int(input("Input lebar persegi panjang: "))
luas_pp = bd.luas_persegi_panjang(p, l)
print(f"Luas persegi panjang adalah {luas_pp}")

r = int(input("Input jari-jari lingkaran: "))
luas_lingkaran = bd.luas_lingkaran(r)
print(f"Luas lingkaran adalah {luas_lingkaran}")
