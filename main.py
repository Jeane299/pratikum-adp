print("="*40)
print("\nSelamat datang di restoran bintang 4")
print("="*40)

nama = input("Masukkan Nama anda: ")
nomor = input("Masukkan nomor handphone anda: ")
alamat = input("Masukkan alamat anda: ")

print("Daftar paket makanan: ") 
print("\n1. Paket Nikmat:") 
print("Nasi Goreng + es teh: Rp.25000")
print("\n2. Paket Sedap:")
print("Indomie Goreng + es teh: Rp.20000")
print("\n3. Paket Snack:")
print("Pempek + es kelapa: Rp.15000")
print("\n4. Paket Puas:")
print("Ayam goreng crispy 4 + nasi 2 + es teh 2: Rp.65000")
print("\n5. Paket Keluarga:")
print("Nasi goreng 4 + Ayam goreng crispy 4 + es teh 4: Rp.130000")
print("\nSilahkan masukkan jumlah pesanan.")
print("Jika tidak ingin mengambil paket yang diminta isi 0")

nikmat = int(input("Paket Nikmat : ")) 
sedap = int(input("Paket Sedap : "))
snack = int(input("Paket Snack: ")) 
puas = int(input("Paket Puas: ")) 
keluarga = int(input("Paket Keluarga: ")) 

pesanan = (nikmat * 25000) + (sedap * 20000) + (snack * 15000) + (puas * 65000) + (keluarga * 130000)
pajak = pesanan * (10/100)
jumlah = nikmat + sedap + snack + puas + keluarga

if pesanan < 150000:
    ongkir = 25000
else:
    ongkir = 0 

total = pesanan + pajak + ongkir

print("="*40)
print("Struk Pesanan")
print("="*40)
print("Nama :", nama)
print("Nomor Telefon : ", nomor)
print("Alamat Pengiriman : ", alamat)
print("\nDetail pesanan :")
print("1. Paket Nikmat : ", nikmat)
print("2. Paket Sedap : ", sedap)
print("3. Paket Snack : ", snack)
print("4. Paket Puas : ", puas)
print("5. Paket Keluarga : ", keluarga)
print("Jumlah : ", jumlah)
print("Total harga : Rp.", pesanan)
print("Pajak (10%) : Rp.", pajak)
print("Biaya Pengiriman : Rp.", ongkir)
print("\nTotal akhir : Rp.", total)