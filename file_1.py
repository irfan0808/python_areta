try:
    sebuah_file=open("absen.csv",'w')
    print "Nama File Yang Tadi Dibuat :",sebuah_file.name
    print "mode pembacaan file :",sebuah_file.mode
    print "Apakah fienya sudah ditutup :",sebuah_file.closed

    sebuah_file.close()
    print "apakah filenya sudah ditutup ? :",sebuah_file.closed 
except IOError, e:
    print "proses gagal karena :", e