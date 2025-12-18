nama = input("Masukkan nama: ")
nim = input("Masukkan nim: ")

while True:
    try:
        alas = float(input("Maukkan alas: "))
        if alas <= 0:
            raise ValueError("Nilai harus lebih besar dari 0")
    
        tinggi = float(input("Masukkan tinggi: "))
        if tinggi <= 0:
            raise ValueError("Nilai harus lebih besar dari 0")
    
        luas = 0.5 * alas * tinggi
        break

    except ValueError as e:
        print(f"Error: {e} coba lagi")

    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

print(f"nama mahasiswa: {nama}")
print(f"nim mahasiswa: {nim}")
print(f"alas: {alas}")
print(f"tinggi: {tinggi}")
print(f"luas segitiga: {luas}")