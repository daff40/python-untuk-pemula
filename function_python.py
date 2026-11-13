# Bab 9 - Function pada Python

# Function tanpa parameter
def sapa():
    print("Halo, saya Daffa dari Subang")

sapa()

# Function dengan parameter
def sapa_teman(nama):
    print("Halo", nama, "ayo main basket!")

sapa_teman("Faiza")
sapa_teman("Raka")

# Function dengan return
def hitung_total(harga, jumlah):
    return harga * jumlah

total = hitung_total(12000, 3)
print("Total beli mi ayam:", total)

# Function dengan nilai default
def tampilkan_hobi(hobi="bermain game"):
    print("Hobi saya adalah", hobi)

tampilkan_hobi()
tampilkan_hobi("basket")

# Function menghitung rata-rata dari list
def rata_rata(daftar_nilai):
    return sum(daftar_nilai) / len(daftar_nilai)

nilai = [85, 90, 88]
print("Rata-rata nilai:", round(rata_rata(nilai), 2))
