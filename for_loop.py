fruits = ['apple', 'banana', 'cherry']

# Menampikan isi array
# for x in fruits:
#     print(x)

# Menampilkan urutan elemen
# banyakdata = len(fruits)
# for i in range(banyakdata):
#     print(i)

# Menampilkan elemen array
# for i in range(banyakdata):
#     print(fruits[i])

# Menambahkan elemen dari masukan user
banyak_data = 3
for j in range(banyak_data):
    fruits.append(input("Masukkan data: "))
print(fruits)