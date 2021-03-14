##Perkenalan nama
print("Halo, nama saya Dendy Halim Kusuma")
print("Saya biasa dipanggil dendy")
print("Saya berasal dari Bengkulu")

##umur

#Tanggal lahir
tanggal_Lahir = 1
bulan_Lahir = 1
tahun_Lahir = 2002

#Tanggal sekarang
tanggal_Sekarang = 13
bulan_Sekarang = 3
tahun_Sekarang = 2021

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
    else:
        bulan_sekarang = bulan_Sekarang
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
print("Umur saya sekarang",umur_tahun_sekarang,"tahun,",umur_bulan_sekarang,"bulan,",umur_hari_sekarang,"hari")

##Tinggi Badan
tinggi = 175
satu_meter = 100
tinggi_cm = float(tinggi)-satu_meter
print("Tinggi saya 1 meter",tinggi_cm,"cm")

##Ukuran Sepatu
ukuran_sepatu = int(45)
print("Ukuran sepatu saya",ukuran_sepatu)

##Alamat Rumah
jalan = str("Hibrida,")
RT_rumah = str("20,")
RW_rumah = str("03,")
no_rumah = str("26B,")
kelurahan = str("Sidomulyo,")
kecamatan = str("Gading Cempaka,")
kota = str("Bengkulu")
print("Alamat saya di jalan",jalan,"RT",RT_rumah,"RW",RW_rumah,"No",no_rumah,"Kota",kota)
