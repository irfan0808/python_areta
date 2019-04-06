def cetak_biodata(nama="irfan",kota="",umur=18):
    print "Nama :",nama;
    print "Umur :",umur;
    print "Kota :",kota;
    return;

print "tanpa memakai default argument :"
cetak_biodata(umur=50,kota="bandung")

print "\n"

print "memakai default argument :"
cetak_biodata()