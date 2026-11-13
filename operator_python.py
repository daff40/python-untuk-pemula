# Bab 5 - Operator pada Python

# Operator aritmatika
harga_mi_ayam = 12000
jumlah = 3
total_bayar = harga_mi_ayam * jumlah
print("Total bayar mi ayam :", total_bayar)
print("Sisa dari uang 50000:", 50000 - total_bayar)
print("Dibagi 2 orang      :", total_bayar / 2)
print("Hasil bagi bulat    :", total_bayar // 5)
print("Sisa bagi           :", total_bayar % 5)
print("Pangkat 2 dari 7    :", 7 ** 2)

# Operator perbandingan
skor_saya = 24
skor_teman = 18
print("Skor saya lebih besar?", skor_saya > skor_teman)
print("Skor sama?", skor_saya == skor_teman)
print("Skor berbeda?", skor_saya != skor_teman)

# Operator logika
latihan_basket = True
sudah_makan = False
print("Boleh main?", latihan_basket and sudah_makan)
print("Salah satu benar?", latihan_basket or sudah_makan)
print("Belum makan?", not sudah_makan)
