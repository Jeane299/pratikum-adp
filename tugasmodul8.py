# import os
# import time

# for i in range (30):
#     print(" "*i, "9", end="")
#     time.sleep(0.2)
#     os.system('cls')
#     print()

# for i in range(30):
#     print(" "*(30-i), "x", end='')
#     time.sleep(0.2)
#     os.system('cls')
#     print()
    
import json
import os

FILE_NAME = "data_keuangan.json"

def baca_data():
    try:
        with open(FILE_NAME, "r") as f:
            data = json.load(f)
        return data
    except json.JSONDecodeError:
        return []

def simpan_data(data):
    f = open(FILE_NAME, "w")
    json.dump(data, f, indent=4)
    f.close()

def tambah():
    tanggal = input("Tanggal (dd-mm-yyyy): ")
    keterangan = input("Keterangan: ")
    jumlah = float(input("Jumlah: "))
    tipe = input("Tipe (pemasukan/pengeluaran): ").lower()
    data = baca_data()
    data.append({
        "tanggal": tanggal,
        "keterangan": keterangan,
        "jumlah": jumlah,
        "tipe": tipe
    })
    simpan_data(data)
    print("Data berhasil ditambahkan.")

def hapus():
    keterangan = input("Keterangan transaksi yang ingin dihapus: ")
    data = baca_data()
    data_baru = [d for d in data if d["keterangan"] != keterangan]
    if len(data) == len(data_baru):
        print("Data tidak ditemukan.")
    else:
        simpan_data(data_baru)
        print("Data berhasil dihapus.")

def edit():
    keterangan = input("Keterangan transaksi yang ingin diedit: ")
    data = baca_data()
    ditemukan = False
    for d in data:
        if d["keterangan"] == keterangan:
            d["tanggal"] = input("Tanggal baru (dd-mm-yyyy): ")
            d["keterangan"] = input("Keterangan baru: ")
            d["jumlah"] = float(input("Jumlah baru: "))
            d["tipe"] = input("Tipe baru (pemasukan/pengeluaran): ").lower()
            ditemukan = True
    if ditemukan:
        simpan_data(data)
        print("data berhasil diedit")

    else:
        print("data dengan keterangan tersebut tidak ditemukan")

def tampil():
    data = baca_data()
    if not data:
        print("Belum ada data keuangan.")
        return
    print("\nData Keuangan Pribadi:")
    print("-" * 70)
    print(f"{'No':<3} {'Tanggal':<12} {'Keterangan':<25} {'Jumlah':<12} {'Tipe':<12}")
    print("-" * 70)
    nomor = 1
    for d in data:
        print(f"{nomor:<3} {d['tanggal']:<12} {d['keterangan']:<25} {d['jumlah']:<12.2f} {d['tipe']:<12}")
        nomor += 1
    print("-" * 70)

# Buat file jika belum ada
if not os.path.exists(FILE_NAME):
    open(FILE_NAME, "w").close()

while True:
    print("\nMenu: [1]Tambah [2]Hapus [3]Edit [4]Tampil [5]Keluar")
    pilih = input("Pilih: ")
    if pilih == "1":tambah()
    elif pilih == "2":hapus()
    elif pilih == "3":edit()
    elif pilih == "4":tampil()
    elif pilih == "5":break
    else: 
        print("Pilihan tidak valid.")
