gaji =  int(input("Masukan Gaji : "))
berkeluarga = True
punya_rumah = True



if gaji > 3000000:
    print ("Gaji sudah diatas UMR")
    if berkeluarga:
        print ("Wajib ikutan asuransi dan menabung untuk pensiun")
    else:
        print ("Tidak perlu ikutan asuransi")

    if punya_rumah:
        print ("wajib bayar pajak rumah")
    else:
        print ("tidak wajib bayar pajak rumah")
else:
    print ("Gaji belum UMR")
