sapa = "Halo, temen-temen!"
spasi = "         "
print(sapa)

# Indexing
# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17
# H A L O ,   T E M E N  -  T  E  M  E  N  !

kata1 = sapa[6:11]
kata2 = sapa[1]
kata3 = sapa[16]

print(kata1)
print(kata1 + kata2 + kata3)

# Panjang Kata
print(len(sapa))
print(len(spasi))

# Penjumlahan string dari input
nama = input("Masukkan nama:")
umur = input("Masukkan umur:")
alamat = input("Masukkan alamat:")
Merge = "Perkenalkan namaku adalah " + nama + ", umurku " + umur + ", alamatku " + alamat
print(Merge)
print(Merge[0:42])