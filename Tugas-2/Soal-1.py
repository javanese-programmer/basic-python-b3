# Definiskan fungsi
def menu():
    print("\n---------------------------")
    print("---Menu---")
    print(" 1. Daftar Kontak\n 2. Tambah Kontak\n 3. Keluar")
    print("---------------------------\n")

def tampil_kontak(name, telephone):
    print("Daftar Kontak: ")
    for i in range(0, len(name)):
        print(" Nama : {}".format(name[i]))
        print(" No Telepon : {}".format(telephone[i]))

def tambah_kontak(name, telephone):
    name.append(input("Nama : "))
    telephone.append(input("No Telepon : "))
    print("\nKontak Berhasil Ditambahkan\n")

# Tampilan Menu
print("PROGRAM BUKU TELEPON")
print("--------------------")
print("\nSelamat Datang!\n")
menu()

# Meminta input user
pilihan = int(input("Pilih Menu : "))
print("")

# Definisikan Array
nama = ['Nafi', 'Joko']
telp = ['08123456789', '08987654321']

# Definisikan Algoritma
while pilihan == 1:
    tampil_kontak(nama, telp)
    menu()
    pilihan = int(input("Pilih Menu : "))
    
    if pilihan == 1:
        continue
    while pilihan == 2:
        tambah_kontak(nama, telp)
        menu()
        pilihan = int(input("Pilih Menu : "))
        print("")

while pilihan == 2:
    tambah_kontak(nama, telp)
    menu()
    pilihan = int(input("Pilih Menu : "))
    print("")
    
    if pilihan == 2:
        continue
    while pilihan == 1:
        tampil_kontak(nama, telp)
        menu()
        pilihan = int(input("Pilih Menu : "))

while pilihan == 3:
    print("Program Selesai, sampai jumpa!\n")
    break
else:
    print("Menu Tidak Tersedia\n")