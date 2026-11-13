# Bab 14 - Instalasi Pycharm
# Catatan langkah memasang PyCharm

langkah = [
    "Buka situs resmi JetBrains",
    "Pilih PyCharm edisi Community",
    "Unduh installer sesuai sistem operasi",
    "Jalankan installer lalu ikuti petunjuknya",
    "Buka PyCharm dan buat project baru",
    "Pilih interpreter Python atau virtual environment",
]

print("=== Langkah Instalasi PyCharm ===")
for nomor, isi in enumerate(langkah, start=1):
    print(str(nomor) + ".", isi)

print("Total langkah:", len(langkah))
