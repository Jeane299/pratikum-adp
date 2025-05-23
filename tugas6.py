while True:
    n = int(input("Masukkan jumlah titik: "))
    if n > 0:
        break
    else:
        print("Input tidak valid. Silahkan masukkan bilangan bulat positif")

titik = []
for i in range(0, n):
    print(f"\nTitik ke-{i+1}")
    x = float(input("Masukkan titik x: "))
    y = float(input("Masukkan titik y: "))
    titik.append([x, y])

print(f"Titik-titik yang telah dimasukkan: {titik}")
print()
print("="*21, "Hasil Perhitungan Jarak", "="*20)
for i in range(len(titik)):
    for j in range(i+1, len(titik)):
        titik_i = titik[i]
        titik_j = titik[j]
        jarak = ((titik_j[0] - titik_i[0])**2 + (titik_j[1] - titik_i[1])**2) **0.5
        print(f"| Jarak titik {i+1} {titik[i]} | ke titik {j+1} {titik[j]} | : |{jarak:.2f}|")

print(f"Selamat anda telah menghitung {n} titik!")
