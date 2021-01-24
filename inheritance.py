class person:
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber
    def display(self):
        print(self.name)
        print(self.idnumber)

class employee (person):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post
        person.__init__(self, name, idnumber)
    def display2(self):
        print(self.name)
        print(self.idnumber)
        print(self.salary)
        print(self.post)

a = employee("Hitman", "047", "1000000", "Assassin")
a.display()
print("---------------------------------------------")
a.display2()