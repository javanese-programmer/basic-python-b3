# Break untuk menghentikan iterasi
# for i in range(6):
#     if i == 2:
#         break
#     print(i)

txt = input("Masukkan code: ")
while True:
    if txt == 'stop' or txt == 'Stop' or txt == 'STOP':
        break
    print("Hasil: {}".format(txt))
    print("------------------------")
    txt = input('Masukkan code: ')