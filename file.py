f = open("file.txt","w")
f.write("Hello")
f.close()

f = open("file.txt","a")
f.write("\nHello Juga")
f.close()

f = open("file.txt","r")
# print(f.read())
# print(f.read(5))
# print(f.readlines())

x = f.readlines()
print(x)
print(x[1])