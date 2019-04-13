try:
    sebuah_file = open("file_aing",'r')

    print "Nama File Yang Tadi Dibuat :",sebuah_file.name
    print "mode pembacaan file :",sebuah_file.mode
    print "Apakah fienya sudah ditutup :",sebuah_file.closed

    print "isi file : \n", sebuah_file.read()
    print "Posisi pointer pada file :" , sebuah_file.tell()

    sebuah_file.close()
    print "apakah filenya sudah di tutup ? :", sebuah_file.closed
except IOError, e:
    print "proses gagal karena : ", e