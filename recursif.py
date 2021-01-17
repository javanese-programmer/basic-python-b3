def masukkan():
    masuk = input("Masukkan input : ")
    if masuk == 'Stop':
        print("Stop")
    else:
        masukkan()

masukkan()