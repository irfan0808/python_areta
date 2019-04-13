try:
    sebuah_file = open("absen.csv",'w')

    print "Nama File Yang Tadi Dibuat :",sebuah_file.name
    print "mode pembacaan file :",sebuah_file.mode
    print "Apakah fienya sudah ditutup :",sebuah_file.closed

    sebuah_file.write('1.Jajang Surahman,Tekhnik Informatika,ITENAS\n')
    sebuah_file.write('2.Angel Corine,Manajemen Informatika,UNIKOM\n')
    sebuah_file.write('3.Samsul Basri,Ilmu Komputer,UPI\n')

    sebuah_file.close()
    print "Apakah filenya sudah ditutup? :",sebuah_file.closed

except IOError, e:
    print "proses gagal karena : ", e