# Bab 8 - Lists dan Dictionaries pada Python

# List: kumpulan data berurutan
mapel = ["IPS", "Bahasa Indonesia", "PJOK"]
print("Daftar mapel:", mapel)
print("Mapel pertama:", mapel[0])
print("Mapel terakhir:", mapel[-1])

mapel.append("Matematika")
print("Setelah ditambah:", mapel)
mapel.remove("Matematika")
print("Setelah dihapus :", mapel)
print("Jumlah mapel    :", len(mapel))

# Dictionary: data dengan nama kunci (key)
profil = {
    "nama": "Muhamad Daffa Al Muhtar",
    "kelas": "XI RPL",
    "kota": "Subang",
    "cita_cita": "pengusaha"
}
print("Nama     :", profil["nama"])
print("Kota     :", profil["kota"])

profil["makanan"] = "mi ayam"
print("Makanan  :", profil["makanan"])

# Dictionary berisi nilai pelajaran
nilai = {"IPS": 85, "Bahasa Indonesia": 90, "PJOK": 88}
for pelajaran, angka in nilai.items():
    print(pelajaran, "=", angka)

print("Nilai tertinggi:", max(nilai.values()))
