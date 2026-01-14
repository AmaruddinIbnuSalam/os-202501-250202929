print("Masukkan path file Dataset.csv")
path_file = input("Path: ")

import csv

# Menyimpan data dari CSV
daftar_proses = []
alokasi = {}
permintaan = {}

# Membaca file CSV
with open(path_file, mode ="r") as file:
    pembaca = csv.DictReader(file)
    for baris in pembaca:
        proses = baris["Process"]
        daftar_proses.append(proses)
        alokasi[proses] = baris["Allocation"]
        permintaan[proses] = baris["Request"]

# Mencari relasi menunggu (wait-for)
menunggu = {}

for p in daftar_proses:
    for q in daftar_proses:
        if p != q and permintaan[p] == alokasi[q]:
            menunggu[p] = q

# Menampilkan relasi menunggu
print("\n:Wait-for graph:")
for p in menunggu:
    print(p, "menunggu", menunggu[p])

# Deteksi deadlock (mencari siklus)
deadlock = False
sudah_dikunjungi = set()

for awal in menunggu:
    proses_sekarang = awal
    sudah_dikunjungi.clear()

    while proses_sekarang in menunggu:
        if proses_sekarang in sudah_dikunjungi:
            deadlock = True
            break
        sudah_dikunjungi.add(proses_sekarang)
        proses_sekarang = menunggu[proses_sekarang]

    if deadlock:
        break

# Menampilkan hasil akhir
if deadlock:
    print("\n DEADLOCK TERDETEKSI")
    print("Proses yang terlibat:", " -> ".join(sudah_dikunjungi))
else:
    print("\n TIDAK TERDAPAT DEADLOCK")
