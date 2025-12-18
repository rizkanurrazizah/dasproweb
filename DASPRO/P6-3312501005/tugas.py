# """Menghitung Nilai Ujian"""
# nilai = int(input("Input nilai anda: "))

# try:
#     if nilai < 0 or nilai > 100:
#         print("Nilai ujian harus antara 0 sampai 100!")
#     print("Nilai Valid:", nilai)
# except ValueError as e:
#     print("Kesalahan:", e)

# """Simple program to validate exam scores."""

# def validate_score():
#     """Check if the entered score is valid (0–100) and display the result."""
#     try:
#         score = int(input("Enter your score: "))
#         if 0 <= score <= 100:
#             print(f"Valid score: {score}")
#         else:
#             print("Score must be between 0 and 100!")
#     except ValueError as error:
#         print(f"Error: {error}")


# if __name__ == "__main__":
#     validate_score()

"""Menghitung Faktorial"""

n = int(input("Input sebuah nilai: "))

if n <= 0:
    print("Input tidak valid, masukkan bilangan lebih besar dari 0.")
else:
    total = 1
    for i in range(n, 0, -1):
        total = total * i

print(f"Hasil faktorial dari {n} adalah: {total}")
