kalimat = input("Inputan kalimat: ")
hitung_vokal = 0

for karakter in kalimat:
    match karakter:
        case 'a' | 'i' | 'u' | 'e' | 'o':
            hitung_vokal += 1
        case _:
            continue

print("Jumlah huruf cokal dalam kalimat adalah:", hitung_vokal)