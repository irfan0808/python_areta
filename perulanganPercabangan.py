terus_tanya = True
while terus_tanya:
    temp = raw_input('masukan angka kurang dari 10 !! :')
    angka = int(temp)
    if angka < 10:
        terus_tanya = False
        print("Anda Menginput Nilai : ",angka)
    else:
        terus_tanya = True

       