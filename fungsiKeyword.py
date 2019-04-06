def cetak_biodata(nama,umur,kota):
    print "Nama :",nama;
    print "Umur :",umur;
    print "Kota :",kota;
    return;

#kalau memakai keyword argument mau urutannya gimanapun input akan sesuai
print "Tanpa memakai keyword argument : "
cetak_biodata(kota="bandung",nama="mike",umur=18)

print "\n"

# kalau tidak memakai keyword argument : mau urutannya gimanapun input tidak akan sesuai
print "Memakai keyword argument : "
cetak_biodata( "bandung", "miki", 50)

print "\n"
# kalau tidak memakai keyword argument : tapi urutannya sesuai maka input akan sesuai
print "Memakai keyword argument : tapi urutannya sesuai "
cetak_biodata( "miki", 50, "bandung")
