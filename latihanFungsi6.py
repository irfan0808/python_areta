def cetak_perolehan_nilai(nama,nim,**data_diri):
    print "Nama   :",nama;
    print "NIM    :",nim;
    print "\n"
    print "===Data Diri==="
    i=1
    for data in data_diri:
        print "%s : %s" %(data,data_diri[data])
        

    return;


cetak_perolehan_nilai("Irfan",98127366717,alamat="Dasana Indah",no_hp="0812-8983-6704",tanggal_lahir="22-Januari",
tempat_lahir="Tasikmalaya",email ="irfanalaziz19@gmail.com",
hoby="Bersyukur")