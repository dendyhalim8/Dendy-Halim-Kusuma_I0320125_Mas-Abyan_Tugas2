#Menghitung luas Persegi panjang
Panjang = input("Masukan Panjang ")
Lebar = input("Masukan Lebar ")
Luas = float(Panjang)*float(Lebar)


#Menghitung luas Lingkaran
Jari_Jari = input("Masukan Jari-Jari ")
Luas = float(Jari_Jari)*float(Jari_Jari)*22/7
print("Luas Lingkaran adalah", Luas)

#Menghitung luas Kubus
rusuk = input("Masukan rusuk ")
Luas_Permukaan = 6*float(rusuk)*float(rusuk)
Volume = float(rusuk)*float(rusuk)*float(rusuk)
print("Luas Permukaan Kubus adalah", Luas_Permukaan,'\n',"Volume Kubus Adalah", Volume)

#Menghitung konversi suhu celcius ke farenheit
celcius = input("Masukan nilai celcius ")
fahreinheit = (float(celcius)*9/5)+32
print("Suhu dalam fahreinheit adalah",fahreinheit,"°F")

#Menghitung konversi suhu reamur ke kelvin
reamur = input("Masukan nilai reamur ")
kelvin = (float(reamur)*5/4)+273.15
print("Suhu dalam kelvin adalah",kelvin,"K")
