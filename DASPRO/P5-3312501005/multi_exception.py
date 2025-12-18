# angka = 1

# while angka != -1:
#     angka = int(input("Masukkan sebuah angka: "))
#     hasil = 10 / angka
#     print(hasil)

angka = 1

while angka != -1:
    try:
        angka = int(input("Masukkan sebuah angka: "))
        hasil = 10 / angka
        print(f"Hasil pembagian adalah: {hasil}")
    except ValueError:
        print("Input tidak valid, Harap masukkan angka.")
    except ZeroDivisionError:
        print("Terjadi kesalahan tidak dapat membagi dengan nol.")
    except Exception as e:
        print(f"Kesalahan tak terduga terjadi: {e}")