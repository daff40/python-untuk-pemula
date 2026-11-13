# Bab 12 - Virtual Environments
# Mengecek apakah program berjalan di dalam virtual environment
import sys

print("Lokasi Python  :", sys.executable)
print("Prefix venv    :", sys.prefix)

if sys.prefix != sys.base_prefix:
    print("Status         : virtual environment AKTIF")
else:
    print("Status         : memakai Python global")

# Daftar langkah membuat venv
langkah = [
    "python -m venv venv",
    "source venv/bin/activate",
    "pip install nama_paket",
    "pip freeze > requirements.txt",
    "deactivate",
]
print("=== Langkah memakai venv ===")
for no, perintah in enumerate(langkah, start=1):
    print(str(no) + ".", perintah)
