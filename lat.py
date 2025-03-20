lambda_t = float(input("Masukkan nilai Lambda * t: "))
m = int(input("Masukkan nilai m: "))
e = 2.71828

for n in range(m + 1):
    faktorial = 1
    for i in range(1, n + 1):
        faktorial *= i
    pn = (e ** (-lambda_t)) * ((lambda_t ** n) / faktorial)
    print(f"P(N(t) =={n}) ={pn}")