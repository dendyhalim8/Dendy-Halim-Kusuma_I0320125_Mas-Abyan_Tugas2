usia = int(input("Berapa usia kamu?"))
ujian = input("Apakah Anda sudah lulus ujian kualifikasi (Y / T)?")
Y = 1
T = 0

if usia >= 21:
    usia = 1
else:
    usia = 0

hasil = usia+Y+T
if hasil == 2:
    hasil = "Anda dapat mendaftar di kursus."
else:
    hasil = "Anda tidak dapat mendaftar di kursus."

print(hasil)