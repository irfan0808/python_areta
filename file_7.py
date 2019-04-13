import os

try:
    os.remove('daftar.txt')
    print "file sudah di hapus .."
except (IOError,OSError),e:
    print "proses error karena :",e 
