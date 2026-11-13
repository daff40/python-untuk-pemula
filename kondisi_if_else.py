# Bab 6 - Kondisi If Else pada Python

# if, elif, else dengan nilai pelajaran
nilai_pjok = 88

if nilai_pjok >= 90:
    print("Nilai PJOK sangat bagus")
elif nilai_pjok >= 80:
    print("Nilai PJOK bagus")
elif nilai_pjok >= 70:
    print("Nilai PJOK cukup")
else:
    print("Nilai PJOK perlu belajar lagi")

# Kondisi dengan input dari pengguna
uang = int(input("Berapa uangmu sekarang? "))
harga_mi_ayam = 12000

if uang >= harga_mi_ayam:
    print("Cukup untuk beli mi ayam")
    print("Kembaliannya:", uang - harga_mi_ayam)
else:
    print("Uangnya kurang", harga_mi_ayam - uang, "rupiah")

# Kondisi dengan operator logika
cuaca_cerah = True
punya_bola = True

if cuaca_cerah and punya_bola:
    print("Ayo main basket di lapangan")
else:
    print("Main game di rumah saja")
