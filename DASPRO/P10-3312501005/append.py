# bilangan = []

# while True:
#     x = int(input("Input sebuah bilangan: "))

#     # hentikan perulangan dengan nilai sentinel -1
#     if x == -1:
#         break
#     bilangan.append(x)

# if len(bilangan) == 0:
#     print("Tidak ada data di list ini")
# else:
#     for e in bilangan:
#         print(f"{e} \t", end="")


bilangan = []

while True:
    x = int(input("Input sebuah bilangan: "))

    # hentikan perulangan dengan nilai sentinel -1
    if x == -1:
        break
    bilangan.insert(len(bilangan), x)

if len(bilangan) == 0:
    print("Tidak ada data di list ini")
else:
    for e in bilangan:
        print(f"{e} \t", end="")