saldo = 500000

def lihat_saldo():
    print(f"Saldo anda saat ini: Rp. {saldo}")

def tarik_uang(n):
    global saldo
    saldo = saldo - n

def simpan_uang(n):
    global saldo
    saldo = saldo + n

simpan_uang(100000)
tarik_uang(25000)
simpan_uang(5000)
lihat_saldo()  
