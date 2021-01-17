def Luas(panjang, lebar):
    luas = panjang*lebar
    return luas

# print(Luas(10,2))

def persegi(panjang, lebar):
    luas = panjang*lebar
    keliling = 2*(panjang + lebar)
    return luas, keliling

print(persegi(10,2))