# bilangan1 = int(input("Input bilangan 1: "))
# bilangan2 = int(input("Input bilangan 2: "))

# pembagian = bilangan1 / bilangan2
    
# print(pembagian)

# try:
#     bilangan1 = int(input("Input bilangan 1: "))
#     bilangan2 = int(input("Input bilangan 2: "))

#     pembagian = bilangan1 / bilangan2

# except Exception as e:
#     print(e)
#     pembagian = 0

# print(pembagian)

# try:
#     bilangan1 = int(input("Input bilangan 1: "))
#     bilangan2 = int(input("Input bilangan 2: "))

#     pembagian = bilangan1 / bilangan2

# except ValueError as e:
#     print(e)
#     pembagian = 0
# except ZeroDivisionError as e:
#     print(e)
#     pembagian = 0
# except Exception as e:
#     print(e)
#     pembagian = 0

# print(pembagian)

# try:
#     bilangan1 = int(input("Input bilangan 1: "))
#     bilangan2 = int(input("Input bilangan 2: "))

#     pembagian = bilangan1 / bilangan2

# except ValueError as e:
#     # bilangan 2 itu menggunakan huruf kyk nol
#     print("Harus bilangan ya!") 
#     pembagian = 0
# except ZeroDivisionError as e:
#     # bilangan 2 itu harus 0 (angka)
#     print("Jangan nol ya woi!")
#     pembagian = 0
# except Exception as e:
#     print("Ooops! Sistem sedang down!")
#     pembagian = 0

# print(pembagian)

# try:
#     bilangan1 = int(input("Input bilangan 1: "))
#     bilangan2 = int(input("Input bilangan 2: "))

#     if bilangan2 == 0:
#         raise ZeroDivisionError("Jangan nol ya om!")
    
#     pembagian = bilangan1 / bilangan2

# except ValueError as e:
#     # bilangan 2 itu menggunakan huruf kyk nol
#     print("Harus bilangan ya!") 
#     pembagian = 0
# except ZeroDivisionError as e:
#     # bilangan 2 itu harus 0 (angka)
#     print(f"Ada error: {e}")
#     pembagian = 0
# except Exception as e:
#     print("Ooops! Sistem sedang down!")
#     pembagian = 0

# print(pembagian)

"""
Ini adalah kode untuk melakukan pembagian
"""
try:
    bilangan1 = int(input("Input bilangan 1: "))
    bilangan2 = int(input("Input bilangan 2: "))

    if bilangan2 == 0:
        raise ZeroDivisionError("Jangan nol ya om!")
    
    pembagian = bilangan1 / bilangan2

except ValueError as e:
    # bilangan 2 itu menggunakan huruf kyk nol
    print("Harus bilangan ya!") 
    pembagian = 0
except ZeroDivisionError as e:
    # bilangan 2 itu harus 0 (angka)
    print(f"Ada error: {e}")
    pembagian = 0
except Exception as e:
    print("Ooops! Sistem sedang down!")
    pembagian = 0

print(pembagian)