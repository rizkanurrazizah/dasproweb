# try:
#     umur = float(input("input umur: "))
#     if umur < 0:
#         raise ValueError("umur tidak boleh negatif")
#     print(f" umur anda adalah {umur}")
# except ValueError as e:
#     print(f"terjadi kesalahan: {e}")

# while True:
#     try:
#         umur = float(input("input umur: "))
#         if umur < 0 :
#             raise ValueError("tidak boleh negatif")
#         print(f"umur anda adalah: {umur}")

#     except ValueError as e:
#         print(f"terjadi kesalahan: {e}")

while True:
    try:
        nilai = float(input("input nilai: "))
        if nilai <= 0 or nilai >=0:
            raise ValueError("nilai harus antara 0-100")
        
        print(f"nilai kamu: {nilai}")

    except ValueError as e:
        print(f"terjadi kesalahan: {e}")