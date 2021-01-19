# Tampilan Menu
print("PROGRAM BUKU TELEPON")
print("--------------------")
print("\nSelamat Datang!\n")
print("---------------------------")
print("---Menu---")
print(" 1. Daftar Kontak\n 2. Tambah Kontak\n 3. Keluar")
print("---------------------------\n")

# Meminta input user
pilihan = int(input("Pilih Menu : "))
print("")

# Definisikan Array
nama = ['Nafi', 'Joko']
telp = ['08123456789', '08987654321']

# Definisikan Algoritma
while pilihan == 1:
    print("Daftar Kontak:")
    for i in range(0, len(nama)):
        print(" Nama : {}".format(nama[i]))
        print(" No Telepon : {}".format(telp[i]))
    
    print("\n---------------------------")
    print("---Menu---")
    print(" 1. Daftar Kontak\n 2. Tambah Kontak\n 3. Keluar")
    print("---------------------------\n")
    pilihan = int(input("Pilih Menu : "))
    
    if pilihan == 1:
        continue
    while pilihan == 2:
        nama.append(input("Nama : "))
        telp.append(input("No Telepon : "))
        print("\nKontak Berhasil Ditambahkan\n")
        print("---------------------------")
        print("---Menu---")
        print(" 1. Daftar Kontak\n 2. Tambah Kontak\n 3. Keluar")
        print("---------------------------\n")
        pilihan = int(input("Pilih Menu : "))
        print("")

while pilihan == 3:
    print("Program Selesai, sampai jumpa!\n")
    break
else:
    print("Menu Tidak Tersedia\n")