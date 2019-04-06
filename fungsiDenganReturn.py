def fungsi_tanpa_parameter():
    temp = 0
    for i in range (1,5):
        temp=temp + 1
    return temp

def fungsi_berparameter(batas_akhir):
    temp = 0
    for i in range (1,batas_akhir):
        temp = temp + 1
    return temp

print "contoh fungsi tanpa parameter:"
print "hasil:",fungsi_tanpa_parameter()
print "hasil:",fungsi_tanpa_parameter()
print "hasil:",fungsi_tanpa_parameter() 

print "\n\n"

print "contoh penggunaan fungsi berparameter:"
print "hasil:",fungsi_berparameter(15)
print "hasil:",fungsi_berparameter(20)
print "hasil:",fungsi_berparameter(25)



