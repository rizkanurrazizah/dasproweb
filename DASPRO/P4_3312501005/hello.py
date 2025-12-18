# for i in range(10):
#     print(f"{i} Hello World!")

# di mulai dari 1 di hentikan saat menyentuh 11 dengan iterasi 2
# for i in range(1, 11, 2):
#     print(f"{i} Hello World!")
nilai = int(input("masukkan jumlah: "))
jumlah = 0

for i in range(1, nilai + 1 ):
    if i % 2 == 0:
        print(f"{i} adalah genap")
        jumlah += i

print("jumlah bilangan genap adalah", jumlah)

# for i in range(10):
#     if i == 5:
#         break
#     else:
#         print(f"{i}")

# for i in range(10):
#     if i % 3 == 0:
#         continue
#     else:
#         print(f"{i}")

# menyediakan nilai nya di awal agar tidak terjadi error
# i = 1
# while (i <= 10):
#     print(f"{i} Hello world")
#     i = i + 1

# perulangan terus menerus hingga jawabannya seblak
# makanan = ""
# while (makanan != "seblak"):
#     makanan = input("makan apa kita?")

# print(f"Ayo makan {makanan}")

# umur = 0
# while (umur <= 0):
#     umur = int(input("umur berapa??"))
# print(f"umur anda: {umur}")