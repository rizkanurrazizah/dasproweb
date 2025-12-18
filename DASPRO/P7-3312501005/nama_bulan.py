def konversi_bulan(bulan):
    match bulan:
        case 1:  return "Januari"
        case 2:  return "Februari"
        case 3:  return "Maret"
        case 4:  return "April"
        case 5:  return "Mei"
        case 6:  return "Juni"
        case 7:  return "Juli"
        case 8:  return "Agustus"
        case 9:  return "September"
        case 10:  return "Oktober"
        case 11:  return "November"
        case 12:  return "Desember"

try:
    tanggal = int(input("Input tanggal: "))
    bulan = int(input("Input bulan: (1-12) "))
    tahun = int(input("Input tahun: "))

    if tanggal < 1 or tanggal > 31:
        print("Error: Tanggal Tidak Valid!")
    elif bulan < 1 or bulan > 12:
        print("Eror: Bulan Tidak Valid!")
    else:
        konversi = konversi_bulan(bulan)
    print(f"{tanggal}/{konversi}/{tahun}")

except ValueError:
    print("Eror: Input harus berupa angka!")


