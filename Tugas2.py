# Program pengecekan umur

umur = int(input("Masukkan umur anda: "))

if umur < 0:
    print("anda belum lahir")
elif umur < 18:
    print("anda belum cukup umur")
elif umur <= 60:
    print("anda cukup umur")
else:
    print("banyakin ibadah, bentar lagi mati")

print("Program selesai")