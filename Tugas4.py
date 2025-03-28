welcome_message = " Selamat datang di sistem reservasi tiket konser!"
print("*************************")
print(f"** {welcome_message}  **")
print("*************************")

print("\nKursi yang tersedia")
list_kursi = " "
n = 1
for i in range (7):
    for j in range (5):
         list_kursi += str(n) + " "
         print(n, end=' ')
         n += 1 
    print()

harga_vvip = 600000
harga_vip = 550000
harga_reguler = 450000
harga_ekonomi = 350000
sisa_vvip = 10
sisa_vip = 15
sisa_reguler = 10
sisa_ekonomi = 0
print("\nHarga Tiket")
print(f"VVIP        : Rp {harga_vvip}")
print(f"VIP         : Rp {harga_vip}")
print(f"Reguler     : Rp {harga_reguler}")
print(f"Ekonomi     : Rp {harga_ekonomi}")

jumlah_pesan = int(input("\nMasukkan jumlah pesanan tiket: "))
for i in range (jumlah_pesan):
     print(f"Pemesanan ke {i + 1}: ")
     nama = input("Masukkan nama anda: ")
     kursi_ke = int(input("Masukkan nomor kursi :"))
     password = input("Masukkan password untuk mengakses kursi anda: ")
     
     if kursi_ke <= 10 :
           if sisa_vvip > 0:
            kelas = "VVIP"
            harga = harga_vvip
            sisa_vvip -= 1
            
           else:
            print("Maaf, kursi VVIP sudah habis.")
            continue
     elif 10 < kursi_ke <= 25 :
          if sisa_vip > 0:
            kelas = "VIP"
            harga = harga_vip
            sisa_vip -= 1
            
          else:
            print("Maaf, kursi VIP sudah habis.")
            continue
     elif 25< kursi_ke <= 35 :
          if sisa_reguler > 0:
            kelas = "Reguler"
            harga = harga_reguler
            sisa_reguler -= 1
            
          else:
            print("Maaf, kursi Reguler sudah habis.")
            continue
     else:
          print("Maaf, kursi Ekonomi tidak tersedia.")
          continue

         
     print("\n")
     print("=========STRUK PEMESANAN TIKET========")
     print(f"Nama        : {nama}")
     print(f"Nomor Kursi : {kursi_ke}")
     print(f"Kategori    : {kelas}")
     print(f"Harga       : Rp {harga}")
     print(f"Password    : {password}")
     if str(kursi_ke) in list_kursi:
           list_kursi = list_kursi.replace(str(kursi_ke), '0', 1)
     else : 
          print("Angka yang Anda pilih tidak ada dalam list.")
          list_kursi += str(n) + " "
     


print("\nSisa Kursi Per Kategori :")
print(f"VVIP        : {sisa_vvip}")
print(f"VIP         : {sisa_vip}")
print(f"Reguler     : {sisa_reguler}")
print(f"Ekonomi     : {sisa_ekonomi}")

print("\nLayout kursi setelah pemesanan")
print(list_kursi, end='')
print()
print("\nTerimakasih telah melakukan reservasi")


        