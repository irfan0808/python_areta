try:
    sebuah_file =open("absen.csv",'rb')

    print "Nama File Yang Tadi Dibuat :",sebuah_file.name
    print "mode pembacaan file :",sebuah_file.mode
    print "Apakah fienya sudah ditutup :",sebuah_file.closed

    print "isi file:\n"
    for line in sebuah_file:
        print line
    
    print "posisi pointer pada file :",sebuah_file.tell()
    print "kembali lagi ke awal :",sebuah_file.seek(0,0)

    print "isi file:\n"
    for line in sebuah_file:
        print line

    print "posisi pointer pada file :",sebuah_file.tell()

    sebuah_file.close()
    print "apakah file sudah di tutup? :",sebuah_file.closed
except IOError, e:
    print "proses gagal karena :",e