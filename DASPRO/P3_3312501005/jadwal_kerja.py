hari = input("Input nama hari: ")

match hari:
    case "senin" | "selasa" | "rabu" | "kamis":
        print("JADWAL KERJA: 08:00 - 17:00 WIB")
    case "jumat":
        print("JADWAL KERJA: 08:00 -17:30 WIB")
    case "sabtu" | "minggu":
        print("WAKTUNYA LIBUR. JANGAN DIGANGGU")
    case _:
        print("Nama hari tidak dikenali")

#hari = input("Input nama hari: ")

#match hari:
#    case "senin" | "selasa" | "rabu" | "kamis":
#        print("JADWAL KERJA: 08:00 - 17:00 WIB")
#    case "jumat":
#        print("JADWAL KERJA: 08:00 -17:30 WIB")
#    case "sabtu":
#        print("JADWAL KERJA 08:00 - 14:00 WIB")
#    case "minggu":
#        print("WAKTUNYA LIBUR. JANGAN DIGANGGU")
#    case _:
#        print("Nama hari tidak dikenali")