x = 100

def myfunc():
    x = 300  # Local Scope
    print(x)

def myfunc2():
    print(x)

print(x)
myfunc()
myfunc2()
print(x)