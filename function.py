# def my_function():
#     print("Hello from a function")

# my_function()
# my_function()

def sapa():
    print("Hallo!")

def bertanya():
    print("Apa kabar?")

def kesakitan():
    print("Aduh!")

# masukan = input("Interaksi: ")
# if masukan == 'sapa':
#     sapa()
# elif masukan == 'bertanya':
#     bertanya()
# elif masukan == 'kesakitan':
#     kesakitan()

def perkenalan(nama, umur, tinggi):
    print("Perkenalkan, namaku {}, umurku {}, tinggiku {} cm".format(nama, umur, tinggi))

# perkenalan('Tariq', 12, 161)
# perkenalan('Fitria', 13, 162)
# perkenalan('Aziz', 14, 163)

# Name = input("Masukkan nama : ")
# Age = int(input("Masukkan umur : "))
# Height = float(input("Masukkan tinggi : "))

# perkenalan(Name, Age, Height)

# Variabel di dalam fungsi tidak berpengaruh ke Variabel di LUAR
# Variabel di luar tidak bisa DIEDIT dalam fungsi
# nilai = 6
# def my_func():
#     nilai = 10
#     print("Nilai dalam fungsi adalah {}".format(nilai))

# my_func()
# print("Nilai di luar fungsi adalah {}".format(nilai))

# Variabel berupa array dapat diedit di dalam fungsi
# array = []
# def edit_array():
#     array.append(0)
#     array.append(1)
#     array.append(2)
#     array.append(3)

# edit_array()
# print(array)