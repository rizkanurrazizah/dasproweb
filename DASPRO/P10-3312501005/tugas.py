# nilai = [90, 75, 77, 60, 65, 65]

# # MEAN
# mean = sum(nilai) / len(nilai)

# # MEDIAN
# nilai_sorted = sorted(nilai)
# n = len(nilai)

# if n % 2 == 1:
#     median = nilai_sorted[n // 2]
# else:
#     median = (nilai_sorted[n // 2 - 1] + nilai_sorted[n // 2]) / 2

# # MODUS
# modus = max(set(nilai), key=nilai.count)

# print("Mean  :", mean)
# print("Median:", median)
# print("Modus :", modus)

nilai = [90, 75, 77, 60, 65, 65]

mean = sum(nilai) / len(nilai)

nilai_sorted = sorted(nilai)
n = len(nilai)

if n % 2 == 1:
    median = nilai_sorted[n // 2]
else:
    median = (nilai_sorted[n // 2 - 1] + nilai_sorted[n // 2]) / 2

modus = max(set(nilai), key=nilai.count)

print(nilai_sorted)
print(f"#Mean dari list nilai adalah {mean}")
print(f"#Median dari list nilai adalah {median}")
print(f"#Modus dari list nilai adalah {modus}")
