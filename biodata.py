class biodata:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def show(self):
        print("\nBIODATA DIRI")
        print("Nama          : " + self.name)
        print("Umur          : " + self.age)
        print("Jenis Kelamin : " + self.gender + "\n")

def masukan():
    print("\nINPUT")
    Nama = input("Masukkan nama Anda                : ")
    Umur = int(input("Masukkan umur Anda                : "))
    Gender = input("Masukkan jenis kelamin Anda (L/P) : ")
    return Nama, Umur, Gender

out = masukan()
bio = biodata(out[0], str(out[1]), out[2])
bio.show()