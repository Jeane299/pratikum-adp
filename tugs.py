def input_data (n):
    nama = []
    nim = []
    pretest = []
    postest = []
    tugas = []
    bonus = []
    for i in range (n):
        print(f"\nPraktikan ke-{i+1}")
        nama.append(input("Masukkan nama Anda: "))
        nim.append(int(input("Masukkan NIM anda: ")))
        pretest.append(float(input("Masukkan nilai pretest Anda: ")))
        postest.append(float(input("Masukkan nilai postest Anda: ")))
        tugas.append(float(input("Masukkan nilai tugas Anda: ")))
        bonus.append(float(input("Masukkan nilai bonus Anda: ")))
    return nama, nim, pretest, postest, tugas, bonus

def rata_rata(nilai, n):
    total = 0
    for i in range (n):
        total = total + nilai[i]
    return total / n

def nilai_akhir(pretest, postest, tugas, bonus, n):
    hitung_nilai = []
    for i in range(n):
        hasil = 0.25 * pretest[i] + 0.25 * postest[i] + 0.5 * tugas[i] + bonus[i]
        hitung_nilai.append(hasil)
    return hitung_nilai
def urutkan(hitung_nilai, nama, nim, n):
    for i in range (n-1):
        for j in range (n-1-i):
            if hitung_nilai[j] < hitung_nilai[j+1]:
                hitung_nilai[j], hitung_nilai[j+1] = hitung_nilai[j+1], hitung_nilai[j]
                nama[j], nama[j+1] = nama[j+1], nama[j]
                nim[j], nim[j+1] = nim[j+1], nim[j]
                
    peringkat = []
    for i in range(n):
        peringkat.append(i + 1)
                
    return hitung_nilai, nama, nim, peringkat

while True:
    n = int(input("Masukkan jumlah praktikan: "))
    if n > 0:
        break
    else:
        print("Input tidak valid. Silahkan masukkan bilangan bulat positif")

nama, nim, pretest, postest, tugas, bonus = input_data(n)
rata_pretest = rata_rata(pretest, n)
rata_postest = rata_rata(postest, n)
rata_tugas = rata_rata(tugas, n)
hitung_nilai = nilai_akhir(pretest, postest, tugas, bonus, n)
rata_hitung_nilai = rata_rata(hitung_nilai, n)
hitung_nilai, nama, nim, peringkat = urutkan(hitung_nilai, nama, nim, n)

# Tampilkan hasil
print("\n| {:<15} | {:<10} | {:<12} | {:<9} |".format("Nama", "NIM", "Nilai Akhir", "Peringkat"))
print("|" + "-"*17 + "|" + "-"*12 + "|" + "-"*14 + "|" + "-"*11 + "|")
for i in range(n):
    print("| {:<15} | {:<10} | {:<12.2f} | {:<9} |".format(nama[i], nim[i], hitung_nilai[i], peringkat[i])) 
print("| {:<15} | {:<10} | {:<12} |".format("", "", "Rata2 nilai akhir: {:.2f}".format(rata_hitung_nilai)))