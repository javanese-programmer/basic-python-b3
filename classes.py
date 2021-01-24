class myclass:
    x = 5
    y = 10
    kali = x*y
    tambah = x+y

def myclasses():
    x = 5
    y = 10
    kali = x*y
    tambah = x+y
    return x, y, kali, tambah

# Mendefinisikan 'Objek'
# 'Objek' adalah cetakan dari class, cetakan bisa lebih dari satu
p1 = myclass()   
p2 = myclass()

# Untuk class, dapat memanggil variabel di dalam (tanpa return)
print(p1.x)
print(p1.y)
print(p1.kali)
print(p1.tambah)

# Untuk fungsi, harus ada return, tidak bisa memanggil variabel dalam
print(myclasses()[0])
print(myclasses()[1])
print(myclasses()[2])
print(myclasses()[3])