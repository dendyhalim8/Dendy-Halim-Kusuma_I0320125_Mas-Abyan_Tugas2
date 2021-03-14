#Masukan tanggal lahir
tanggal_Lahir = input("Masukan Tanggal lahir ")
bulan_Lahir = input("Masukan Bulan lahir ")
tahun_Lahir = input("Masukan Tahun lahir ")

#Masukan tanggal sekarang
tanggal_Sekarang = input("Masukan Tanggal Sekarang ")
bulan_Sekarang = input("Masukan Bulan Sekarang ")
tahun_Sekarang = input("Masukan Tahun Sekarang ")

#Penjumlahan umur
umur_tahun = int(tahun_Sekarang)-int(tahun_Lahir)
umur_bulan = int(bulan_Sekarang)-int(bulan_Lahir)
umur_hari = int(tanggal_Sekarang)-int(tanggal_Lahir)

#Tahun & bulan
if umur_bulan > 0:
    umur_tahun_tambahan = 0
    umur_bulan_sekarang = umur_bulan
elif umur_bulan < 0:
    umur_tahun_tambahan = 1
    umur_bulan_sekarang = 12+int(umur_bulan)
else:
    if umur_hari >= 0:
        umur_tahun_tambahan = 0
        umur_bulan_sekarang = umur_bulan
    else:
        umur_tahun_tambahan = 1
        umur_bulan_sekarang = 11
umur_tahun_sekarang = int(umur_tahun)-int(umur_tahun_tambahan)

#hari
tahun_kabisat = int(tahun_Sekarang)/4
if umur_bulan == 0:
    bulan_Sekarang = bulan_Sekarang
else:
    bulan_Sekarang = int(bulan_Sekarang)-1
    if bulan_Sekarang == 0:
        bulan_Sekarang = 12

#jumlah hari dalam 1 bulan
if bulan_Sekarang == 1:
    jumlah_hari =31
elif bulan_Sekarang == 2:
    if tahun_kabisat == 505:
        jumlah_hari = 29
    elif tahun_kabisat == 506:
        jumlah_hari = 29
    elif tahun_kabisat == 507:
        jumlah_hari = 29
    else:
        jumlah_hari = 28
elif bulan_Sekarang == 3:
    jumlah_hari = 31
elif bulan_Sekarang == 4:
    jumlah_hari = 30
elif bulan_Sekarang == 5:
    jumlah_hari = 31
elif bulan_Sekarang == 6:
    jumlah_hari = 30
elif bulan_Sekarang == 7:
    jumlah_hari = 31
elif bulan_Sekarang == 8:
    jumlah_hari = 31
elif bulan_Sekarang == 9:
    jumlah_hari = 30
elif bulan_Sekarang == 10:
    jumlah_hari = 31
elif bulan_Sekarang == 11:
    jumlah_hari = 30
else:
    jumlah_hari = 31
if umur_hari >= 0:
    umur_hari_sekarang = umur_hari
else:
    umur_hari_sekarang = jumlah_hari+umur_hari
print("Umur anda sekarang",umur_tahun_sekarang,"tahun,",umur_bulan_sekarang,"bulan,",umur_hari_sekarang,"hari")
