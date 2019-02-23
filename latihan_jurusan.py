jurusan =raw_input("Pilih Jurusan : ")
jam =raw_input("Pilih Jam : ")

if jurusan == "TI" :
    jurus = "Tekhnik Informatika"
    if jam == "PG":
        jm = "pagi"
        biaya = "2.000.000"
    else :
        jm = "siang"
        biaya = "2.500.000"

else :
    jurus = "Sistem Informasi"
    if jam == "PT":
        jm = "pagi"
        biaya = "1.000.000"
    else :
        jm = "siang"
        biaya = "1.500.000"
print("Anda Memilih Jurusan",jurus)
print("Dengan Pilihan Jam",jm)
print("Dengan Biaya",biaya)


