nilai1 = int(input("Nilai 1: "))
nilai2 = int(input("Nilai 2: "))

try:
    x = nilai1 / nilai2
except ZeroDivisionError:
    print("Tidak bisa membagi dengan nol!")