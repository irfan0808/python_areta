print("===Halaman Login===")
input_lagi = True
while input_lagi:
    temp = raw_input('Masukan Username Anda :')
    nama = str(temp)
    if nama == "irfano":
        input_lagi = False
        print("Selamat Datang : ",nama)
    else:
        input_lagi = True

       