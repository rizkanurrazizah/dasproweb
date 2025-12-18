import random

def arisan(anggota):
    if not anggota:
        return "Daftar anggota kosong"
    return random.choice(anggota)

pemenang = arisan("Ani", "Budi", "Cici", "Doni", "Eko", "Fulan")
print(f"Selamat! Pemenang arisan bulan ini adalah {pemenang}")
