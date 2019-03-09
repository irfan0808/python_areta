dic_toko ={'Nama Toko':'Areta Mart',
           'Alamat   ':'Dasana Indah-Kelapa Dua',
           'Email    ':'areta@gmail.com',
           'Telpon   ':'021-121-121-121',}

list_buah = ['jeruk','nanas','apel','semangka']
tuple_harga =(1000,2000,1500,4500)
list_sayur = ['bayam','sawi','daun singkong','kol','wortel']

#dic_buah ={'Buah ':'jeruk,nanas,apel,semangka'}
#dic_harga={'Harga':'1000,2000,1500,4500'}
#dic_sayur={'Sayur':'Bayam,sawi,daun singkong,kol,wortel'}

print("IDENTITAS MINI MARKET")
print"\n"

for dic in dic_toko:
    print dic,':',dic_toko[dic]

print"\n"

print ("PRODUK YANG DIJUAL ")
print"\n"

#for dic in dic_buah:
#    print dic,':',dic_buah[dic]

#for dic in dic_harga:
#    print dic,':',dic_harga[dic]

#for dic in dic_sayur:
#    print dic,':',dic_sayur[dic]

print list_buah
print tuple_harga
print list_sayur

print"\n"

print dic_toko['Nama Toko']
print list_buah[2]
print tuple_harga[3]

