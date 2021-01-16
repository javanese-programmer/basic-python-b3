print("JUMLAH CUSTOMER")
n = int(input("Masukkan jumlah customer hari ini: "))
print("")

print("----------------------------------------------")
nama =[]
umur =[]
print("INPUT DATA CUSTOMER")
for i in range(n):
    nama.append(input("Masukkan nama customer: "))
    umur.append(int(input("Masukkan umur customer: ")))
    print("")

print("----------------------------------------------")
print("CUSTOMER HARI INI:")
for i in range(n):
    print("Nama Customer {} : {}".format(i+1, nama[i]))
    print("Umur Customer {} : {}".format(i+1, umur[i]))
    print("")