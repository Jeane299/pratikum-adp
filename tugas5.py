nim = []
nama_mhs = []
nilai_mhs = []
while True:
    print("\n=== Program Manajemen Nilai Mahasiswa ===")
    print("1. Tambah Data")
    print("2. Hapus Data")
    print("3. Tampilkan Data")
    print("4. Keluar")
    pilih = input("Pilih menu (1-4): ")
    if pilih == "1":
        no = input("Masukkan Nomor Mahasiswa: ")
        nama = input("Masukkan Nama Mahasiswa: ")
        nilai = float(input("Masukkan Nilai Mahasiswa: "))
        nim.append(no)
        nama_mhs.append(nama)
        nilai_mhs.append(nilai)
        print("Data berhasil ditambahkan.")
    elif pilih == "2":
        cari_nim = input("Masukkan Nomor Mahasiswa yang akan dihapus: ")
        if cari_nim in nim:
            indeks = nim.index(cari_nim)
            del nim[indeks]
            del nama_mhs[indeks]
            del nilai_mhs[indeks]
            print("Data berhasil dihapus.")
        else:
            print("Nomor mahasiswa tidak ditemukan.")
    elif pilih == "3":
        if nim:
            print("\nData Mahasiswa (Diurutkan berdasarkan nilai):")
            for i in range(len(nilai_mhs) - 1):
                for j in range(i + 1, len(nilai_mhs)):
                    if nilai_mhs[i] < nilai_mhs[j]:
                        nilai_mhs[i], nilai_mhs[j] = nilai_mhs[j], nilai_mhs[i]
                        nama_mhs[i], nama_mhs[j] = nama_mhs[j], nama_mhs[i]
                        nim[i], nim[j] = nim[j], nim[i]
            for i in range(len(nim)):
                print(f"{i+1}. Nomor: {nim[i]}, Nama: {nama_mhs[i]}, Nilai: {nilai_mhs[i]}")
        else:
            print("\nTidak ada data mahasiswa.")
    elif pilih == "4":
        print("Keluar dari program.")
        break
    else:
        print("Pilihan tidak valid.Coba lagi.")
    
