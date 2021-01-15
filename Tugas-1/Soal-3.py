# Masukkan nilai ujian
Teori = float(input("Masukkan nilai ujian teori Anda: "))
Praktik = float(input("Masukkan nilai ujian praktik Anda: "))

# Menentukan kelulusan peserta
if(Teori<70 and Praktik<70):
    print("Anda harus mengulang ujian teori dan praktik")
elif(Teori<70 and Praktik>=70):
    print("Anda harus mengulang ujian teori")
elif(Teori>=70 and Praktik<70):
    print("Anda harus mengulang ujian praktik")
else:
    print("Selamat, Anda Lulus")