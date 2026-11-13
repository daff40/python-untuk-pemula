# Bab 7 - Perulangan pada Python

# for dengan range
print("=== Latihan basket ===")
for i in range(1, 6):
    print("Tembakan ke-" + str(i))

# for dengan list
print("=== Daftar hobi ===")
hobi = ["bermain game", "basket"]
for h in hobi:
    print("Hobi saya:", h)

# while dengan penghitung
print("=== Hitung mundur ===")
hitung = 5
while hitung > 0:
    print(hitung)
    hitung = hitung - 1
print("Mulai!")

# break dan continue
print("=== Mencari angka 4 ===")
for angka in range(1, 10):
    if angka == 2:
        continue
    if angka == 4:
        print("Ketemu angka 4, berhenti")
        break
    print("Angka:", angka)
