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

def tampil():
    data = baca_data()
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
    print("\nMenu: [1]Tambah [2]Hapus [3]Tampil [4]Keluar")
    pilih = input("Pilih: ")
    if pilih == "1":tambah()
    elif pilih == "2":hapus()
    elif pilih == "3":tampil()
    elif pilih == "4":break
    else: 
        print("Pilihan tidak valid.")
