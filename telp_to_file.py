# import library/modul
import telp

# panggil modul
telp.pembuka()
telp.menu()

# Minta input dari user
def pilihan():
    choice = int(input("Masukkan pilihan : "))
    print("")
    return choice

# definisikan algoritma
pilih = pilihan()
while True:
    if pilih == 1:
        telp.tampil_kontak()
    elif pilih == 2:
        telp.tambah_kontak()
    elif pilih == 3:
        telp.penutup()
        break
    else:
        print("Menu tidak tersedia")
    telp.menu()
    pilih = pilihan()