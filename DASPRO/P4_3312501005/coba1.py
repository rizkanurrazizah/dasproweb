# ===============================================
# Program: Menghitung Luas Segitiga dengan Exception Handling
# Nama File: luas_segitiga_exception.py
# ===============================================

print("=== Program Luas Segitiga dengan Exception Handling ===")

# Input identitas mahasiswa
nama = input("Masukkan Nama Mahasiswa: ")
nim = input("Masukkan NIM Mahasiswa: ")

while True:
    try:
        # Input alas
        alas = float(input("NMasukkan alas segitiga: "))
        if alas <= 0:
            raise ValueError("Nilai harus lebih besar dari nol!")
        
        # Input tinggi
        tinggi = float(input("Masukkan tinggi segitiga: "))
        if tinggi <= 0:
            raise ValueError("Nilai harus lebih besar dari nol!")
        break  

    except ValueError as e:
        print(f"Error: {e} Coba lagi.")

    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

luas = 0.5 * alas * tinggi
# Tampilkan hasil perhitungan
print("=== HASIL PERHITUNGAN ===")
print(f"Nama Mahasiswa : {nama}")
print(f"NIM Mahasiswa  : {nim}")
print(f"Alas Segitiga  : {alas}")
print(f"Tinggi Segitiga: {tinggi}")
print(f"Luas Segitiga  : {luas}")

print("\nProgram selesai dijalankan.")
