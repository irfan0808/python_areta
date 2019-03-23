ini_dictionary={
                   'Nama '   :'Budi Santoso',
                   'Kelas'  :'12.4A',
                   'No hp'  :'081298889299'}

for ini in ini_dictionary:
    print ini,':',ini_dictionary[ini]

print "\n"

absen = int(input("Masukan Nilai Absen : "))
tugas = int(input("Masukan Nilai Tugas : "))
uts   = int(input("Masukan Nilai UTS   : "))
uas   = int(input("Masukan Nilai UAS   : "))

nilaiAbsen = (absen * 0.1)
nilaiTugas = (tugas * 0.2)
nilaiUts   = (uts   * 0.3)
nilaiUas   = (uas   * 0.4)

nilaiAkhir = nilaiAbsen+nilaiTugas+nilaiUts+nilaiUas

print "\n"

print("Nilai Akhir Anda Adalah : ",nilaiAkhir)