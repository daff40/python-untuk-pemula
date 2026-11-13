# Bab 10 - Class dan Object pada Python

# Class sebagai cetakan, object sebagai hasilnya
class Siswa:
    def __init__(self, nama, kelas, kota):
        self.nama = nama
        self.kelas = kelas
        self.kota = kota
        self.hobi = []

    def tambah_hobi(self, hobi):
        self.hobi.append(hobi)

    def perkenalan(self):
        print("Nama  :", self.nama)
        print("Kelas :", self.kelas)
        print("Kota  :", self.kota)
        print("Hobi  :", ", ".join(self.hobi))

# Membuat object dari class
daffa = Siswa("Muhamad Daffa Al Muhtar", "XI RPL", "Subang")
daffa.tambah_hobi("bermain game")
daffa.tambah_hobi("basket")
daffa.perkenalan()

# Object kedua dari class yang sama
faiza = Siswa("Faiza", "XI RPL", "Subang")
faiza.tambah_hobi("basket")
print("---")
faiza.perkenalan()

# Class dengan perhitungan
class Kantin:
    def __init__(self, menu, harga):
        self.menu = menu
        self.harga = harga

    def total(self, jumlah):
        return self.harga * jumlah

mi_ayam = Kantin("Mi Ayam", 12000)
print("---")
print("Total 3 porsi", mi_ayam.menu, ":", mi_ayam.total(3))
