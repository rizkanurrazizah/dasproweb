print("""
Inputkan data sebagai berikut:
- Ketikkan 1 untuk hari senin                       - ketikkan 2 untuk hari selasa
- Ketikkan 3 untuk hari rabu                        - ketikkan 4 untuk hari kamis
- ketikkan 5 untuk hari jumat                       - ketikkan 6 untuk hari sabtu
- ketikkan 7 untuk hari minggu 
""")

hari = int(input("Pilih hari: \n"))
match hari:
    case 1:
        print("Hari ini adalah senin \n")
    case 2:
        print("Hari ini adalah selasa \n")
    case 3:
        print("Hari ini adalah rabu \n")
    case 4:
        print("Hari ini adalah kamis \n")
    case 5:
        print("Hari ini adalah jumat \n")
    case 6:
        print("Hari ini adalah sabtu \n")
    case 7:
        print("Hari ini adalah minggu \n")
        