print("=========Aplikasi Perhitungan Nilai===========")
absen = int(input("Masukan Nilai Absen : "))
tugas = int(input("Masukan Nilai Tugas : "))
uts   = int(input("Masukan Nilai Uts   : "))
uas   = int(input("Masukan Nilai Uas   : "))

hitungAbsen = (absen * 10)/100
hitungTugas = (tugas * 20)/100
hitungUts   = (uts   * 30)/100
hitungUas   = (uas   * 40)/100
nilaiAkhir  = hitungAbsen+hitungTugas+hitungUts+hitungUas
 

if nilaiAkhir >= 90 and nilaiAkhir<= 100:
    grade="A"
    status="Lulus"
elif nilaiAkhir >= 75 and nilaiAkhir < 90:
    grade="B"
    status="Lulus"
elif nilaiAkhir >= 55 and nilaiAkhir < 75:
    grade="C"
    status="Lulus"
elif nilaiAkhir >= 40 and nilaiAkhir < 55:
    grade="D"
    status="Tidak Lulus"
else:
    grade="E"
    status="Tidak Lulus"

print("========= Hasil Nilai Akhir ===========")
print("Nilai Absen Anda Adalah : ",hitungAbsen)
print("Nilai Tugas Anda Adalah : ",hitungTugas)
print("Nilai Uts Anda Adalah   : ",hitungUts)
print("Nilai Uas Anda Adalah   : ",hitungUas)
print("Nilai Akhir Anda Adalah : ",nilaiAkhir)

print("=== Grade ===")
print("Anda Mendapatkan Grade : ",grade)
print("Anda Dinyatakan : ",status)