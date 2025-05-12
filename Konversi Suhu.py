# FARENHEIT ATAU CELCIUS
hm = input("Masukan jenis suhu(Celcius/Farenheit): ")
if hm == "Celcius":

    # CELCIUS KE FARENHEIT
    print("---Konversi suhu Celcius ke Farenheit---")
    cel = float(input("Masukan suhu Celcius: "))
    okeh = cel * 9/5
    ans = okeh + 32
    print(f"Kalau jadi Farenheit menjadi: {ans}")

else:

    # FARENHEIT KE CELCIUS
    print("---Konversi suhu Farenheit ke Celcius---")
    far = float(input("Masukan suhu Farenheit: "))
    oke = far - 32
    anw = oke * 5/9
    print(f"Kalau jadi suhu Celcius menjadi: {anw}")