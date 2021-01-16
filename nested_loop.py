# for i in range(2):
#     for j in range(2):
#         print("i : {}, j : {}".format(i,j))
# print("")

# for i in range(3):
#     print("i : {}".format(i))
#     for j in range(3):
#         print("j : {}".format(j))
#     print("")

# Menampilkan matriks 3D
angka = [
    [
        [1, 3],
        [3, 5]
    ],
    [
        [2, 4],
        [4, 6]
    ]
]

for i in angka:
    print("Ini i : {}".format(i))
    for j in i:
        print("Ini j : {}".format(j))
        for k in j:
            print("Ini k : {}".format(k))
    print("")