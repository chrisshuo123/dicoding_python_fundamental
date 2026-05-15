import argparse
from datetime import datetime
 
parser = argparse.ArgumentParser()
parser.add_argument('-n', '--nama', required=True, help="Masukkan Nama Anda")
parser.add_argument('-t', '--tanggallahir', required=True, help="Masukkan Tanggal Lahir Anda (DD-MM-YYYY)")
args = parser.parse_args()
 
# Parse string tanggal menjadi datetime object
tgl_lahir = datetime.strptime(args.tanggallahir, "%d-%m-%Y")
tahun = tgl_lahir.year
hari_ini = datetime.now()
usia = hari_ini.year - tgl_lahir.year - ((hari_ini.month, hari_ini.day) < (tgl_lahir.month, tgl_lahir.day))

# Tentukan panggilan berdasarkan usia
if usia < 30:
    panggilan = "Kakak"
else:
    panggilan = "Bapak"

print(f"Terima kasih telah menggunakan libParser_mod.py pada tahun {tahun}, {panggilan} {args.nama}")
