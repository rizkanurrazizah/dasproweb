# nilai = int(input("Input nilai anda: "))

# try:
#     if nilai < 0 or nilai > 100:
#         raise ValueError("Nilai ujian harus antara 0 sampai 100!")
#     print("Nilai Valid:", nilai)
# except ValueError as e:
#     print("Kesalahan:", e)

nilai = int(input("Input nilai anda: "))

try:
    if nilai < 0 or nilai > 100:
        print("Nilai ujian harus antara 0 sampai 100!")
    print("Nilai Valid:", nilai)
except ValueError as e:
    print("Kesalahan:", e)