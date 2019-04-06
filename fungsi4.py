def cetak_perolehan_nilai(nama,twiter,*scores):
    print "Nama   :",nama;
    print "Twiter :",twiter;
    print "Score  :"
    i=1
    for score in scores:
        print "nilai ke- %d : %d" %(i,score)
        i=i+1
    return;

print "Dengan adanya varible-length variable sisa akan menjadi tuple:"
cetak_perolehan_nilai("Silvy","@slvy99",90,80,70,80,90)