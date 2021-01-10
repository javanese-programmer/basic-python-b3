angka = 10
angka_str = "Ini adalah angka 10"
angka_list = ["ini", "adalah", "angka", "10"]

print(angka_str)
print(angka_str[0])
print(angka_list)
print(angka_list[0])
print(len(angka_str))
print(len(angka_list))

# MENAMBAHKAN DATA PADA LIST
# sebelum
print(angka_list)

# sesudah ditambah
angka_list.append("lho rek")
print(angka_list)

#  edit
angka_list[3] = 1000
print(angka_list)

# PERULANGAN
for i in range(0,6):
    print("i yang ke: {}".format(i))

halo = ""
for i in range(0,5):
    halo = halo + "Halo "
print(halo)

for x in angka_list:
    print(x)

for x in range(0,len(angka_list)):
    print(x)

hasil = ""
for x in range(0, len(angka_list)):
    hasil = hasil + angka_list[x] + " "
    print(hasil)
print(hasil)