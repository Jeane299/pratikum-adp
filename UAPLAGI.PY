import os
import time
from termcolor import colored, cprint

file_name1 = "class_schedule.txt"
file_name2 = "todo_list.txt"

# Fungsi baca data dari file

def baca_data(file_path):
    with open(file_path, "r") as f:
        isi = f.read().strip()
        if isi:
            return eval(isi)
        else:
            return {}

def simpan_data(file_path, data):
    with open(file_path, "w") as f:
        f.write(repr(data))

def tampil_logo():
    logo = [
"░██████╗████████╗██╗░░░██╗██████╗░██╗░░░██╗  ██████╗░██╗░░░██╗██████╗░██████╗░██╗░░░██╗",
"██╔════╝╚══██╔══╝██║░░░██║██╔══██╗╚██╗░██╔╝  ██╔══██╗██║░░░██║██╔══██╗██╔══██╗╚██╗░██╔╝",
"╚█████╗░░░░██║░░░██║░░░██║██║░░██║░╚████╔╝░  ██████╦╝██║░░░██║██║░░██║██║░░██║░╚████╔╝░",
"░╚═══██╗░░░██║░░░██║░░░██║██║░░██║░░╚██╔╝░░  ██╔══██╗██║░░░██║██║░░██║██║░░██║░░╚██╔╝░░",
"██████╔╝░░░██║░░░╚██████╔╝██████╔╝░░░██║░░░  ██████╦╝╚██████╔╝██████╔╝██████╔╝░░░██║░░░",
"╚═════╝░░░░╚═╝░░░░╚═════╝░╚═════╝░░░░╚═╝░░░  ╚═════╝░░╚═════╝░╚═════╝░╚═════╝░░░░╚═╝░░░",
    ]
    for line in logo:
        cprint(line, "magenta")
# Tambah class schedule
def tampilkan_tabel_hari(daftar_hari):
    cprint("=" * 64, "white", "on_blue")
    for hari in daftar_hari:
        cprint(f"{hari:^12}", "white", "on_blue", end=" ")
    print()
    cprint("=" * 64, "white", "on_blue")

def tambah_class_schedule(data, file_path):
    daftar_hari = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat"]
    tampilkan_tabel_hari(daftar_hari)

    hari = input(colored("Masukkan hari: ","magenta")).strip().capitalize()
    if hari not in daftar_hari:
        cprint("Hari tidak valid! Hanya boleh Senin s.d. Jumat.", "red", "on_white")
        input(colored("Tekan enter untuk kembali...","magenta"))
        return

    matkul = input(colored("Masukkan mata kuliah: ","magenta")).strip()
    waktu = input(colored("Masukkan waktu: ","magenta")).strip()

    if hari not in data:
        data[hari] = []
    data[hari].append({"Mata Kuliah": matkul, "Waktu": waktu})
    simpan_data(file_path, data)
    cprint("Data berhasil ditambahkan.","magenta")

from termcolor import cprint

def tampilkan_class_schedule(data):
    hari_list = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat"]
    print("="*60)
    cprint(f"{'Hari':<10} | {'Mata Kuliah':<25} | {'Waktu':<20}", "white", "on_black")
    print("="*60)
    for hari in hari_list:
        if hari in data:
            for item in data[hari]:
                teks = f"{hari:<10} | {item['Mata Kuliah']:<25} | {item['Waktu']:<20}"
                cprint(teks, "white", "on_blue")
        else:
            teks = f"{hari:<10} | {'- Tidak ada jadwal':<25}"
            cprint(teks, "grey", "on_red")

def edit_class_schedule(data, file_path):
    hari = input(colored("Masukkan hari: ", "magenta")).capitalize()
    if hari in data:
        for i, item in enumerate(data[hari]):
            print(i, ":", item["Mata Kuliah"], "|", item["Waktu"])
        indeks = int(input(colored("Pilih indeks yang mau diedit: ", "magenta")))
        data[hari][indeks]["Mata Kuliah"] = input(colored("Mata kuliah baru: ", "magenta"))
        data[hari][indeks]["Waktu"] = input(colored("Waktu baru: ", "magenta"))
        simpan_data(file_path, data)
        cprint("Data berhasil diedit.","magenta")
    else:
        cprint("Hari tidak ditemukan.","magenta")

# Hapus class schedule

def hapus_class_schedule(data, file_path):
    hari = input("Masukkan hari: ").capitalize()
    if hari in data:
        for i, item in enumerate(data[hari]):
            print(i, ":", item["Mata Kuliah"], "|", item["Waktu"])
        index = int(input("Pilih indeks yang mau dihapus: "))
        data[hari].pop(index)
        simpan_data(file_path, data)
        print("Data berhasil dihapus.")
    else:
        print("Hari tidak ditemukan.")

# Tambah To-Do

def tambah_todo(data, file_path):
    project = input(colored("Nama project: ","magenta"))
    tipe = input(colored("Tipe (tugas/ujian): ","magenta"))
    deadline = input(colored("Deadline: ","magenta"))
    while True:
        prioritas = int(input(colored("Prioritas (1-5): ","magenta")))
        if 1 <= prioritas <= 5:
            break
        else:
            cprint(f"Masukkan angka (1-5)", "magenta")
    if project not in data:
        data[project] = []
    data[project].append({"Tipe": tipe, "Deadline": deadline, "Prioritas": prioritas})
    simpan_data(file_path, data)
    print("To-Do berhasil ditambahkan.")

def edit_todo(data, file_path):
    project = input("Masukkan nama project: ")
    if project in data:
        for i, item in enumerate(data[project]):
            print(i, ":", item["Tipe"], "|", item["Deadline"], "| Prioritas:", item["Prioritas"])
        
        index = int(input("Pilih indeks yang mau diedit: "))

        # Ambil data baru dulu
        new_project = input("Project baru: ")
        new_tipe = input("Tipe baru: ")
        new_deadline = input("Deadline baru: ")
        new_prioritas = int(input("Prioritas baru (1-5): "))

        # Buat item baru
        item_baru = {
            "Tipe": new_tipe,
            "Deadline": new_deadline,
            "Prioritas": new_prioritas
        }

        # Jika project belum ada, buat list kosong dulu
        if new_project not in data:
            data[new_project] = []

        # Tambahkan item baru ke project baru
        data[new_project].append(item_baru)

        # Hapus item lama
        data[project].pop(index)
        if not data[project]:  # Jika sudah tidak ada item, hapus key-nya
            del data[project]

        simpan_data(file_path, data)
        print("Data berhasil diedit.")
    else:
        print("Project tidak ditemukan.")

# Hapus To-Do

def hapus_todo(data, file_path):
    project = input("Masukkan nama project: ")
    if project in data:
        for i, item in enumerate(data[project]):
            print(i, ":", item["Tipe"], "|", item["Deadline"], "| Prioritas:", item["Prioritas"])
        index = int(input(colored("Pilih indeks yang mau dihapus: ","magenta")))
        data[project].pop(index)
        simpan_data(file_path, data)
        cprint("Data berhasil dihapus.","magenta")
    else:
        cprint("Project tidak ditemukan.","magenta")

# Tampilkan To-Do
def tampilkan_todo(data):
    print("=" * 70)
    cprint(f"{'Project':<15} | {'Tipe':<25} | {'Deadline':<20} | {'Prioritas':<10}", "white", "on_black")
    print("=" * 70)
    for project, items in data.items():
        for item in items:
            teks = f"{project:<15} | {item['Tipe']:<25} | {item['Deadline']:<20} | {item['Prioritas']:<10}"
            cprint(teks, "white", "on_blue")  # Ganti on_blue sesuai preferensi

# Menu utama
open(file_name1, "a").close()
open(file_name2, "a").close()

def animasi_loading():
    for i in range(101):
        cprint(f"\rLoading... {i}%", 'white', 'on_blue', end='')
        time.sleep(0.01)
        
    print()

def menu():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        tampil_logo()
        animasi_loading()
        time.sleep(0.5)
        os.system('cls' if os.name == 'nt' else 'clear')
        tampil_logo()
        kotak_menu = [
            "        Menu Utama         ",
            "1. Class Schedule",
            "2. To-Do List",
            "3. Keluar"
        ]

        cprint("=" * 30, "white", "on_magenta")  # atas kotak
        for baris in kotak_menu:
            cprint(f"{baris:<30}", "yellow", "on_magenta")
        cprint("=" * 30, "white", "on_magenta")  # bawah kotak

        pilih = input(colored("\nPilih menu: ", "magenta"))
        
        if pilih == "1":
            data_cs = baca_data(file_name1)
            menu_cs(data_cs)
        elif pilih == "2":
            data_todo = baca_data(file_name2)
            menu_todo(data_todo)
        elif pilih == "3":
            break

def menu_cs(data):
    while True:
        print()
        cprint("\r-- Class Schedule --", "white", "on_magenta", attrs=["bold"])
        cprint("Menu: [1] Tambah  [2] Tampilkan  [3] Edit [4] Hapus [5] Keluar", "blue", "on_white")
        pilihan = input("Pilih: ")
        if pilihan == "1":
            tambah_class_schedule(data, file_name1)
        elif pilihan == "2":
            tampilkan_class_schedule(data)
        elif pilihan == "3":
            edit_class_schedule(data, file_name1)
        elif pilihan == "4":
            hapus_class_schedule(data, file_name1)
        elif pilihan == "5":
            break

def menu_todo(data):
    while True:
        print()
        cprint("\r-- TO-DO LIST --", "white", "on_magenta", attrs=["bold"])
        cprint("Menu: [1] Tambah  [2] Tampilkan  [3] Edit [4] Hapus [5] Keluar", "blue", "on_black")
        pilihan = input("Pilih: ")
        if pilihan == "1":
            tambah_todo(data, file_name2)
        elif pilihan == "2":
            tampilkan_todo(data)
        elif pilihan == "3":
            edit_todo(data, file_name2)
        elif pilihan == "4":
            hapus_todo(data, file_name2)
        elif pilihan == "5":
            break


menu()
