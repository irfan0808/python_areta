import os

try:
    os.rename('absen.csv','daftar-hadir.csv')
    print "Nama file sudah di ubah .."
except (IOError,OSError),e:
    print "proses error karena :",e 
