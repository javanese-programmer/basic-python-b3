# this_dict = {
#     'brand' : 'Ford',
#     'model' : 'mustang',
#     'year'  : 1964
# }

# data_list = ['ford', 'mustang', 1964]

# bio = {
#     'nama'   : 'Tariq',
#     'umur'   : 20,
#     'tinggi' : 161
# }

# print(this_dict)
# print(data_list)
# print(bio['nama'])

jumlah_anak = {
    'kelas7' : 20,
    'kelas8' : 30,
    'kelas9' : 20
}

# print("Jumlah anak kelas 7 adalah {}".format(jumlah_anak['kelas7']))
# print("Jumlah anak kelas 8 adalah {}".format(jumlah_anak['kelas8']))
# print("Jumlah anak kelas 9 adalah {}".format(jumlah_anak['kelas9']))

# jumlah_anak['kelas9'] = 40

# print("")
# print("Jumlah anak kelas 7 adalah {}".format(jumlah_anak['kelas7']))
# print("Jumlah anak kelas 8 adalah {}".format(jumlah_anak['kelas8']))
# print("Jumlah anak kelas 9 adalah {}".format(jumlah_anak['kelas9']))

for x in jumlah_anak:
    print(x)
    print(jumlah_anak[x])