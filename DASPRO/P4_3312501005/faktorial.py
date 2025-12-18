n = int(input("Input sebuah nilai: "))

if n <= 0:
    print("Input tidak valid, masukkan bilangan lebih besar dari 0.")
else:
    pass

    total = 1
    for i in range(n, 0, -1):
        total = total * i

print(f"Hasil faktorial dari {n} adalah: {total}")

