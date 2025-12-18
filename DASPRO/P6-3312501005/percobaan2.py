rr=float(input('Input jari-jari: '))
pa=float(input('input panjang: '))
le=float(input("Input lebar: "))

import math, dataclasses

luasLingkaran =math.pi * rr * rr
keliling_lingkaran = 2 * math.pi * rr

luas_persegi_panjang = pa * le
keliling_persegi_panjang = 2 * (pa + le)

print(f"Luas Lingkaran: {luasLingkaran}")
print("Keliling Lingkaran: ", keliling_lingkaran)
print("Luas Persegi Panjang: ", luas_persegi_panjang)
print("Keliling Persegi Panjang: ", keliling_persegi_panjang)

# """Program sederhana menghitung luas dan keliling lingkaran serta persegi panjang."""

# import math

# rr = float(input('Input jari-jari: '))
# pa = float(input('Input panjang: '))
# le = float(input("Input lebar: "))

# luas_lingkaran = math.pi * rr * rr
# keliling_lingkaran = 2 * math.pi * rr

# luas_persegi_panjang = pa * le
# keliling_persegi_panjang = 2 * (pa + le)

# print(f"Luas Lingkaran: {luas_lingkaran}")
# print("Keliling Lingkaran: ", keliling_lingkaran)
# print("Luas Persegi Panjang: ", luas_persegi_panjang)
# print("Keliling Persegi Panjang: ", keliling_persegi_panjang)
