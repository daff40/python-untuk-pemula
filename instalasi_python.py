# Bab 2 - Instalasi Python
# Mengecek versi Python dan sistem operasi yang dipakai
import sys
import platform

print("Versi Python  :", sys.version.split()[0])
print("Sistem        :", platform.system(), platform.release())
print("Lokasi Python :", sys.executable)
print("Python sudah terpasang di laptop milik Daffa")
