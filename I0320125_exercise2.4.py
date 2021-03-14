#menampilkan informasi program

print("Konversi suhu (fahrenheit ke Celcius)")

#input suhu dalam fahreinheit
F = float(input("Masukan suhu(fahrenheit): "))

#melakukan konversi suhu ke celcius
C = 5 * (F-32) / 9

#menampilkan hasil konversi ke layar
print("Fahrenheit: ", F)
print("Celcius: ", C)