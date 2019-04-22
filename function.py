user = raw_input ('username :')
import getpass
sandi = getpass.getpass()
if sandi == "123" and user == "123":
    print ("Anda berhasil login")

else:
    print ("username atau password salah")
    exit()

print "==============================="
def menu():
    print "menu pilihan"
    print "-------------"
    print "1.persegi panjang"
    print "2.segitiga"
    print "3.lingkaran"
    print "4.exit"
    print "-------------"
def persegi():
    print "menghitung luas persegi panjang"
    print "-------------"
    p = int (raw_input("masukan panjang :"))
    l = int (raw_input("masukan lebar :"))
    luas = (p*l)
    print "luas persegi panjang =",luas
    print "ingin menghitung luas lagi (y/t):"
    back = str (raw_input().upper())
    if back=="y":
        menu()
    else:
        exit()

def segitiga():
    print "menghitung luas segitiga"
    print "-------------"
    a = int (raw_input("masukan alas :"))
    t = int (raw_input("masukan tinggi :"))
    luas = (a*t)/2
    print "luas segitiga =",luas
    print "ingin menghitung luas lagi (y/t):"
    back = raw_input().upper()
    if back=="y":
        menu()
    else:
        exit()

def lingkaran():
    print "menghitung luas lingkaran"
    print "-------------"
    r = int (raw_input("masukan jari jari :"))
    phi = 3,14
    luas = phi*r*r
    print "luas lingkaran =",luas
    print "ingin menghitung luas lagi (y/t):"
    back = raw_input().upper()
    if back=="y":
        menu()
    else:
        exit()

menu()
while 1:
    pilih = raw_input ("masukan pilihan anda :")
    if pilih =="1":
        persegi()
    elif pilih =="2":
        segitiga()
    elif pilih =="3":
        lingkaran()
    elif pilih =="4":
        exit()
    else:
        print "maaf pilihan anda tidak ada di menu"
        print "ingin menghitung luas lagi (y/t)"
    back = raw_input().upper()
    if back == "y":
        menu()
    else:
        exit()

