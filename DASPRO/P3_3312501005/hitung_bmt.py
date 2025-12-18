nama = input("Input nama anda: ")
berat = float(input("Input berat anda: (kg) "))
tinggi = float(input("Pilih tinggi anda: (m) "))

imt = berat / (tinggi * tinggi)

print("Halo, " + nama)
print(f"Indeks masa tubuh anda adalah: {imt} ")

if imt < 17:
    print("Kurus berat")
elif imt >= 17 and imt <= 18.4:
    print("Kurus ringan")
elif imt >= 18.5 or imt <= 25:
    print("Normal")
elif imt >= 25.1 and imt <= 27:
    print("Gemuk ringan")
else:
    print("Gemuk Berat")