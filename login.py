user = raw_input ('username :')
import getpass
sandi = getpass.getpass()
if sandi == "123" and user == "123":
    print ("Anda berhasil login")
else:
    print ("username atau password salah")