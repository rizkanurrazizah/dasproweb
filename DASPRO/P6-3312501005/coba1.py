# # ===============================================
# # Program: Menghitung Luas Segitiga (For Loop + Exception Handling)
# # Nama File: luas_segitiga_for_only.py
# # ===============================================

# print("=== Program Luas Segitiga (For Loop + Exception Handling) ===")

# # Input identitas mahasiswa
# nama = input("Masukkan Nama Mahasiswa: ")
# nim = input("Masukkan NIM Mahasiswa: ")

# try:
#     # Input jumlah segitiga
#     n = int(input("Masukkan jumlah segitiga yang ingin dihitung: "))
#     if n <= 0:
#         raise ValueError("Jumlah harus lebih besar dari 0!")

#     total_luas = 0

#     # Perulangan for (tanpa while sama sekali)
#     for i in range(1, n + 1):
#         print(f"\nData ke-{i}")
#         try:
#             alas = float(input("Masukkan alas segitiga: "))
#             if alas <= 0:
#                 raise ValueError("Alas harus lebih besar dari nol!")

#             tinggi = float(input("Masukkan tinggi segitiga: "))
#             if tinggi <= 0:
#                 raise ValueError("Tinggi harus lebih besar dari nol!")

#         except ValueError as e:
#             print(f"Error: {e} Data ke-{i} dilewati.")
#             continue  # langsung lanjut ke data berikutnya
#         except Exception as e:
#             print(f"Terjadi kesalahan: {e}")
#             continue

#     # Hasil akhir
#     luas = 0.5 * alas * tinggi
#     total_luas += luas
#     print(f"Luas segitiga ke-{i} = {luas}")

#     rata = total_luas / n if n > 0 else 0

#     print("\n=== HASIL AKHIR ===")
#     print(f"Nama Mahasiswa : {nama}")
#     print(f"NIM Mahasiswa  : {nim}")
#     print(f"Jumlah Data    : {n}")
#     print(f"Total Luas     : {total_luas}")
#     print(f"Rata-Rata Luas : {rata}")

# except ValueError as e:
#     print(f"Error Input: {e}")
# except Exception as e:
#     print(f"Terjadi kesalahan tidak terduga: {e}")

# print("\nProgram selesai dijalankan.")


nilai = int(input("masukkan jumlah: "))
jumlah = 0

for i in range(1, nilai, 1 ):
    if i % 2 == 0:
        print(f"{i} adalah genap")
        jumlah += i

print("jumlah bilangan genap adalah", jumlah)