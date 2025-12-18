def tambah(x, y):
    return x + y

def kurang(x, y):
    return x - y

def kali(x, y):
    return x * y

def bagi(x, y):
    if y == 0:
        return "Error: pembagian dengan nol!"
    return x / y

def selesai():
    print("Program selesai. Sampai jumpa lagi!")

def hitung(x, y, op):
    match op:
        case "+":
            return tambah(x, y)
        case "-":
            return kurang(x, y)
        case "*":
            return kali(x, y)
        case "/":
            return bagi(x, y)
        case _:
            return "Operator tidak dikenal"

def main():
    while True:
        try:
            x = int(input("Input bilangan x: "))
            y = int(input("Input bilangan y: "))
        except ValueError:
            print("Input harus berupa angka bulat.")
            continue

        operasi = input("Pilih operasi (+, -, *, /): ").strip()
        hasil = hitung(x, y, operasi)
        print(hasil)

        ulang = input("Ulangi program? (y/n): ").strip().lower()
        if ulang != "y":
            break

    selesai()

if __name__ == "__main__":
    main()
