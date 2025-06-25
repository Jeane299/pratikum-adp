import os
import json
import time
from termcolor import colored, cprint

file_name1 = "class_schedule.json"
file_name2 = "todo_list.json"

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

def baca_data(file_path):
    try:
        with open(file_path, "r") as f:
            data = json.load(f)
        return data
    except (json.JSONDecodeError, FileNotFoundError):
        return {}

def simpan_data(file_path, data):
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)

def tambahclass_schedule(data_dict, file_path):
    daftar_hari = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat"]

    hari = input("Masukkan nama hari (ex: Senin): ").strip().capitalize()
    if hari not in daftar_hari:
        print("Hari tidak valid! Hanya boleh Senin s.d. Jumat.")
        input("Tekan enter untuk kembali...")
        return  # keluar dari fungsi tanpa menambahkan jadwal

    mata_kuliah = input("Masukkan nama mata kuliah: ").strip().title()
    waktu = input("Masukkan waktu mata kuliah (ex: 08:00 - 09:30): ").strip()

    if hari not in data_dict:
        data_dict[hari] = []

    data_dict[hari].append({
        "Mata Kuliah": mata_kuliah,
        "Waktu": waktu
    })

    simpan_data(file_path, data_dict)
    print("Jadwal berhasil ditambahkan.")
    input("Tekan enter untuk kembali...")

def edit_cs(data_dict, file_path):
    print("\n>> Menu Edit Data")
    hari = input("Masukkan nama hari yang ingin diedit: ").strip().capitalize()
    if hari in data_dict and data_dict[hari]:
        for i, jadwal in enumerate(data_dict[hari]):
            print(f"[{i}] {jadwal['Mata Kuliah']} - {jadwal['Waktu']}")
        try:
            idx = int(input("Pilih nomor jadwal: "))
            if 0 <= idx < len(data_dict[hari]):
                data_dict[hari][idx]["Mata Kuliah"] = input("Mata kuliah baru: ")
                data_dict[hari][idx]["Waktu"] = input("Waktu baru: ")
                simpan_data(file_path, data_dict)
                print("Jadwal berhasil diedit.")
            else:
                print("Nomor jadwal tidak valid.")
        except ValueError:
            print("Input tidak valid.")
    else:
        print("Hari tidak ditemukan atau tidak ada jadwal.")
    input("Tekan enter untuk kembali..")

def hapus_cs(data_dict, file_path):
    print(f"\nMenu Hapus Data")
    hari = input("Masukkan nama hari yang ingin dihapus: ").strip().capitalize()
    if hari in data_dict and data_dict[hari]:
        for i, jadwal in enumerate(data_dict[hari]):
            print(f"[{i}] {jadwal['Mata Kuliah']} - {jadwal['Waktu']}")
        try:
            idx = int(input("Pilih nomor jadwal yang ingin dihapus: "))
            if 0 <= idx < len(data_dict[hari]):
                deleted = data_dict[hari].pop(idx)
                print(f"Jadwal '{deleted['Mata Kuliah']}' berhasil dihapus.")
                simpan_data(file_path, data_dict)
            else:
                print("Nomor jadwal tidak valid.")
        except ValueError:
            print("Input tidak valid.")
    else:
        print("Hari tidak ditemukan atau tidak ada jadwal.")
    input("Tekan enter untuk kembali..")


def tabel_cs(file_path):
    data = baca_data(file_path)
    list_hari = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat"]
    print("=" * 60)
    cprint(f"{'Hari':<10} | {'Mata Kuliah':<25} | {'Waktu':<20}", "white", "on_black")
    for hari in list_hari:
        if hari in data:
            for item in data[hari]:
                cprint(f"{hari:<10} | {item['Mata Kuliah']:<25} | {item['Waktu']:<20}", "white", "on_cyan")
        else:
            cprint(f"{hari:<10} | {'(Kosong)':<25} | {'-':<20}", "white", "on_red")
    print("=" * 60)

def tambah_todo(data_dict, file_path):
    project = input("Masukkan nama project: ")
    duedate = input("Masukkan deadline (dd-mm-yyyy): ")
    jenis = input("Masukkan tipe project (ex: tugas/ujian): ")
    
    while True:
        prioritas = int(input("Masukkan skala prioritas (1-5): "))
        if 1 <= prioritas <= 5:
            break
        else:
            print("Prioritas harus dari angka 1-5")
        
    semua_item = []
    for items in data_dict.values():
        semua_item.extend(items)
    nomor = len(semua_item)+1
    if project not in data_dict:
        data_dict[project] = []

    data_dict[project].append({
        "No": nomor,
        "Project": project,
        "Due Date": duedate,
        "Tipe": jenis,
        "Prioritas": prioritas
    })
    simpan_data(file_path, data_dict)
    print("List berhasil ditambahkan")
    input("Tekan enter untuk kembali...")

def edit_todo(data_dict, file_path):
    semua_item = []
    for project_items in data_dict.values():
        semua_item.extend(project_items)
    for i, item in enumerate(semua_item):
        print(f"[{i}] {item['Project']} - {item['Due Date']} - {item['Tipe']} - {item['Prioritas']}")
    try:
        indeks = int(input("Pilih nomor data yang ingin diedit: "))
        if 0 <= indeks < len(semua_item):
            item = semua_item[indeks]
            item["Project"] = input("Project baru: ").strip().capitalize()
            item["Due Date"] = input("Due Date baru (dd-mm-yyyy): ")
            item["Tipe"] = input("Jenis baru: ").strip().capitalize()            
            while True:
                prioritas = int(input("Masukkan skala prioritas (1-5): "))
                if 1 <= prioritas <= 5:
                    item["Prioritas"] = prioritas
                    break
                else: print("Prioritas harus dari angka 1-5")
            
            simpan_data(file_path, data_dict)
            print("Data berhasil diedit.")
        else:
            print("Indeks tidak valid.")
    except ValueError:
        print("Input tidak valid.")
    
    input("Tekan enter untuk kembali...")

def delete_todo(data_dict, file_path):
    print("\nMenu Hapus To-Do")
    semua_item = []
    for project_items in data_dict.values():
        semua_item.extend(project_items)
    for i, item in enumerate(semua_item):
        print(f"[{i}] {item['Project']} - {item['Due Date']} - {item['Tipe']} - {item['Prioritas']}")

    try:
        idx = int(input("Pilih nomor To-Do yang ingin dihapus: "))
        if 0 <= idx < len(semua_item):
            deleted = semua_item[idx]
            for project in data_dict:
                data_dict[project] = [item for item in data_dict[project] if item["No"] != deleted["No"]]
            simpan_data(file_path, data_dict)
            print(f"To-Do '{deleted['Project']}' berhasil dihapus.")
        else:
            print("Nomor To-Do tidak valid.")
    except ValueError:
        print("Input tidak valid.")
    input("Tekan enter untuk kembali...")


def tabel_todo(file_path):
    data = baca_data(file_path)
    semua_item = []
    for items in data.values():
        semua_item.extend(items)

    if not semua_item:
        print("Belum ada data To-Do.")
        input("Tekan enter untuk kembali...")
        return

    print("Menampilkan tabel...")
    time.sleep(1)
    print("-" * 68)
    cprint(f"{'No':<5} | {'Project':<20} | {'Tipe':<10} | {'Deadline':<12} | {'Prioritas':<6}", "white", "on_blue")
    for item in semua_item:
        cprint(f"{item['No']:<5} | {item['Project']:<20} | {item['Tipe']:<10} | {item['Due Date']:<12} | {item['Prioritas']:<9}", "white", "on_cyan")
    print("-" * 68)

def submenu_studentplanner():
    while True:
        cprint("\r-- Class Schedule --", "white", "on_magenta", attrs=["bold"])
        cprint("Menu: [1] Tambah  [2] Tampilkan  [3] Edit [4] Hapus [5] Keluar", "blue", "on_white")
        pilihan = input("Pilih: ")

        if pilihan == "1":
            data = baca_data(file_name1)  
            tambahclass_schedule(data, file_name1)
        elif pilihan == "2":
            tabel_cs(file_name1)
        elif pilihan == "3":
            data = baca_data(file_name1)
            edit_cs(data, file_name1)
        elif pilihan == "4":
            data = baca_data(file_name1)
            hapus_cs(data, file_name1)
        elif pilihan == "5":
            break
        else:
            print("Pilihan tidak valid.")

def submenu_todolist():
    while True:
        #os.system('cls' if os.name == 'nt' else 'clear')  # biar bersih setiap buka menu
        cprint("\n-- TO-DO LIST --", "white", "on_magenta", attrs=["bold"])
        cprint("Menu: [1] Tambah  [2] Tampilkan  [3] Edit [4] Hapus [5] Keluar", "blue", "on_black")
        pilihan = input("Pilih: ")

        if pilihan == "1":
            data = baca_data(file_name2) 
            tambah_todo(data, file_name2)
        elif pilihan == "2":
            tabel_todo(file_name2)
        elif pilihan == "3":
            data = baca_data(file_name2)
            edit_todo(data, file_name2)
        elif pilihan == "4":
            data = baca_data(file_name2) 
            delete_todo(data, file_name2)
        elif pilihan == "5":
            break
        else:
            cprint("Pilihan tidak valid.", "red", "on_white")
            input("Tekan Enter untuk kembali...")

if not os.path.exists(file_name1):
    with open(file_name1, "w") as f:
        f.write("{}")

if not os.path.exists(file_name2):
    with open(file_name2, "w") as f:
        f.write("{}")

def animasi_loading():
    for i in range(101):
        cprint(f"\rLoading... {i}%", 'white', 'on_blue', end='')
        time.sleep(0.01)
    print()

def menu_utama():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear layar saat mulai
        tampil_logo()
        cprint(f"\nSELAMAT DATANG DI DONANCE", "white", "on_magenta", attrs=["bold"])
        print(" ")
        
        animasi_loading()  # Tampilkan loading 0-100%

        # HAPUS layar setelah loading selesai
        time.sleep(0.5)  # Tambahkan sedikit jeda biar tidak terlalu mendadak
        os.system('cls' if os.name == 'nt' else 'clear')

        tampil_logo()
        cprint("\n=== MENU UTAMA ===", "white", "on_magenta", attrs=["bold"])
        cprint("[1] Class Schedule  [2] To-Do List  [3] Keluar", "magenta")
        pilih = input("Pilih menu: ")

        if pilih == "1":
            submenu_studentplanner()
        elif pilih == "2":
            submenu_todolist()
        elif pilih == "3":
            print("Keluar...")
            break
        else:
            print("Pilihan tidak valid.")
            input("Tekan Enter untuk kembali...")

menu_utama()

#submenu_todolist()
#submenu_studentplanner()