# Bab 4 - Variabel dan Tipe Data

# Numbers: integer dan float
nilai_ips = 85
nilai_indonesia = 90
nilai_pjok = 88
total = nilai_ips + nilai_indonesia + nilai_pjok
rata_rata = total / 3

print("Nilai IPS         :", nilai_ips)
print("Nilai B. Indonesia:", nilai_indonesia)
print("Nilai PJOK        :", nilai_pjok)
print("Total nilai       :", total)
print("Rata-rata         :", round(rata_rata, 2))

# Strings
nama = "Muhamad Daffa Al Muhtar"
kota = "Subang"
cita_cita = "pengusaha"
print("Nama saya " + nama + " dari " + kota)
print("Cita-cita saya menjadi " + cita_cita)
print("Nama dalam huruf besar:", nama.upper())
print("Jumlah huruf pada nama:", len(nama))

# Boolean
suka_basket = True
suka_mi_ayam = True
nilai_di_atas_85 = rata_rata > 85
print("Suka basket?", suka_basket)
print("Suka mi ayam?", suka_mi_ayam)
print("Rata-rata di atas 85?", nilai_di_atas_85)

# Mengecek tipe data
print(type(nilai_ips), type(rata_rata), type(nama), type(suka_basket))
