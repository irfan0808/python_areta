def cetak_perolehan_nilai(nama,twiter,**data_tambahan):
    print "Nama   :",nama;
    print "Twiter :",twiter;
    print "\n"
    print "Data Lainnya :"
    i=1
    for data in data_tambahan:
        print "%s : %s" %(data,data_tambahan[data])
        

    return;

# kalau parameter diisi semua
print "Dengan adanya keyword argument, argumen tersisa akan menjadi dictionary : "
cetak_perolehan_nilai("Silvy","@sivlysiv",email ="silvysilvy@gmail.com",
facebook="www.facebook.com/silvysil", telp  ="0838-1234-5678")