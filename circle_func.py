print("\nINI ADALAH PROGRAM MENGHITUNG LINGKARAN")
print("---------------------------------------")

# Definisikan fungsi
def circle(radius):
    luas = radius*radius*22/7
    keliling = radius*2*22/7
    return luas, keliling

print("Daftar Kode \n Mulai : Memulai program \n Stop : Menghentikan program\n")
code = input("Masukkan kode : ")

if code == 'Mulai':
    while code != 'Stop' and code == 'Mulai':
        # Minta masukan dari User
        jari_jari = float(input("Masukkan jari-jari lingkaran : "))
        # Panggil Fungsi
        lingkaran = circle(jari_jari)
        # Tampilkan ke layar
        print("Lingkaran memiliki luas {:.2f} cm\u00b2 dan keliling {:.2f} cm\n".format(lingkaran[0], lingkaran[1]))
        code = input("Masukkan kode : ")

print("\nTerima kasih sudah menggunakan program!\n")