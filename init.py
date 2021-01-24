class person:
    def __init__(self, name, age, nama_lawan):
        self.name = name
        self.age = age
        self.nama_lawan = nama_lawan
    def sapa(self):
        print("Halo, namaku " +self.name)
        print("Namamu siapa?")
    def salamkenal(self):
        print("Salam Kenal " +self.nama_lawan)
        print("Senang bertemu denganmu, sampai jumpa!")

# p1 = person("Nafi", 22)
# p2 = person("Dodit", 21)

p1 = person("Nafi", 22, "Dodit")
p1.sapa()
p1.salamkenal()