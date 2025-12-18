from konverter.suhu.celcius import celcius
from konverter.uang.dollar import usdollar, sgdollar, zwdollar

def demo_suhu():
    suhu = int(input("Input suhu: "))
    unit = input("Input unit suhu (f,k,r): ")
    hasil = celcius(suhu, unit)
    print(f"{suhu}{unit} = {round(hasil, 1)} celcius")

def demo_uang():
    nominal = int(input("Input nominal rupiah: "))

    hasil_zwd = zwdollar(nominal)
    print(f"Rupiah → Zimbabwe Dollar : {hasil_zwd}")

    hasil_sgd = sgdollar(nominal)
    print(f"Rupiah → Singapore Dollar : {hasil_sgd}")

    hasil_usd = usdollar(nominal)
    print(f"Rupiah → US Dollar : {hasil_usd}")

if __name__ == "__main__":
    print("=== Demo Konverter ===")
    pilihan = input("Pilih mode: (s)uhu / (u)ang: ").strip().lower()
    if pilihan == "s":
        demo_suhu()
    else:
        demo_uang()


# # konverter/main.py
# from konverter.suhu import celcius
# from konverter.uang import usdollar, sgdollar, zwdollar

# def demo_suhu():
#     suhu = int(input("Input suhu: "))
#     unit = input("Input unit suhu (f,k,r): ")
#     hasil = celcius(suhu, unit)
#     print(f"{suhu}{unit} = {round(hasil, 1)} celcius")

# def demo_uang():
#     pass

# if __name__ == "__main__":
#     print("=== Demo Konverter ===")
#     pilihan = input("Pilih mode: (s)uhu / (u)ang: ").strip().lower()
#     if pilihan == "s":
#         demo_suhu()
#     else:
#         demo_uang()

