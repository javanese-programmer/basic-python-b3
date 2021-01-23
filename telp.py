# Definisikan fungsi
def pembuka():
    print("PROGRAM PENCATAT KONTAK")
    print("\nSelamat Datang!\n")
    f = open("kontak.txt", "w")
    f.write("KONTAK SAYA\n")
    f.close()

def menu():
    print("---------------------------")
    print("---Menu---")
    print(" 1. Daftar Kontak\n 2. Tambah Kontak\n 3. Keluar")
    print("---------------------------\n")

def tampil_kontak():
    f = open("kontak.txt", "r")
    print(f.read())
    f.close()

def tambah_kontak():
    f = open("kontak.txt", "a")
    f.write(input("Nama : "))
    f.write("\n")
    f.write(input("No Telepon : "))
    f.write("\n")
    f.write("\n")
    f.close()
    print("\nKontak Berhasil Ditambahkan!\n")

def penutup():
    print("Program Selesai, sampai jumpa!\n")