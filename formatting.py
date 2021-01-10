age = 20
tahun = "tahun"
txt = "Namaku adalah Tariq dan umurku adalah {} {}".format(age,tahun)

print(txt)
print(type(age))
print(type(tahun))

print("Menghitung Luar Persegi Panjang")
panjang = input("Masukkan panjang:")
lebar = input("Masukkan lebar:")
Luas = float(panjang) * float(lebar)
output = "{} dikalikan {} menghasilkan luas {}".format(panjang, lebar, Luas)
print(output)

tinggi = float(input("Masukkan tinggi:"))
Volume = float(panjang) * float(lebar) * tinggi
print(Volume)
