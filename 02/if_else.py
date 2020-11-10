# x = 5
# y = "5"
# z = 6
## conditional statement
# print(x==float(y))#sama dengan
# print(x==z)
# print(x!=z)#tidak sama dengan
# print(x>z)#lebih besar
# print(x<z)#lebih kecil
# print(x>=int(y))#lebih besar sama dengan
# print(x<=z)#lebih kecil sama dengan
# # and atau or
# # False and True = False
# print(x==z and x<z)
# # False or True = True
# print(x==z or x<z)
# # rules and
# # True and True = True
# # True and False = False
# # False and True = False
# False and False = False
# rules or
# True or True = True
# True or False = True
# False or True = True
# False and False = False

# print(not(5>6))
# print(~(x>6))
# print(~(3)) # -4
# print(~(2)) # -3
# print(~(1)) # -2

# nilai = int(input("masukkan nilai siswa: ")) #60
# if nilai >=80: #60>=80 False
#     print("murid lulus")
# else: #tidak ada yang harus di cek, langsung print
#     print("murid harus remidi")

# nilai 90
# 90>=80 True and 90<=100 True = True
# nilai 75
# 75>=80 False and 75 <=100 True = False
# kondisi if else elif tidak ada batasnya
# kalo print harus True kalo False akan terus mencari kondisi True
# if nilai >= 80 and nilai <= 100:
#     print("A")
# elif nilai >= 70 and nilai < 80:
#     print("B")
# else:
#     print("C")


# quiz

# # input = 4
# # print = angka 4 termasuk bilangan genap
# angka = int(input("masukkan angka:"))
# if angka % 2 ==0:
#     print("bilangan", angka, "adalah bilangan genap")
# else:
#     print("bilangan", angka, "adalah bilangan ganjil")

# x = '$'
# print(x.isdigit()) # false
# print(x.isalpha()) # false
# print(x.isalnum()) # false
# print(x.isnumeric()) # false
# print(x.isascii()) # true
# print('a' == 'a') # true

# print('12345'.isdigit())  # true
# print('12345'.isnumeric())  # true
# print('一二三四五'.isdigit()) # false
# print('一二三四五'.isnumeric()) # true



'''
input massa dalam kg
input tinggi dalam cm
imt = ((massa / tinggi)/tinggi)*10000
< 18.5 print berat badan anda kurang
18.5 - 24.9 print berat badan anda ideal
25 - 29.9 print bb anda berlebih
40 < print anda obesitas
print massa anda 60 kg dan tinggi anda 1.7 m
imt = ______
berat badan anda ideal
'''
# berat = input('Masukkan berat (kg): ')
# tinggi = input('Masukkan tinggi (cm): ')

# if berat.isnumeric() == False or tinggi.isnumeric() == False:
#     print('Input only numerical data')
#     # isalpha: apakah sebuah string mengandung alphabet saja
#     # isalnum: apakah sebuah string mengandung alpha-numerical
#     # isnumeric: apakah sebuah string mengandung numerical saja

# else:
#     berat = int(berat)
#     tinggi = int(tinggi)
#     if berat < 40 or tinggi < 40:
#         print('Apakah Anda baik baik saja?')
#     else:
#         imt = ((berat / tinggi)/tinggi)*10000         
#         print(f'Indeks massa tubuh anda adalah {imt}')
#         if imt < 18.5:
#             print('BB Anda kurang')
#         elif 18.5 < imt <= 24.9:
#             print('BB Anda ideal')
#         elif 24.9 < imt <= 29.9:
#             print('BB Anda berlebih')
#         elif 29.9 < imt <= 39.9:
#             print('BB Anda sangat berlebih')
#         else: print('Anda Obesitas')

'''
pisang = 3000
lebih dari 100k diskon 10%
lebih dari 50k kurang dari 100k 5%
kurang dari 50k no diskon
berapa banyak pisang yang ingin dibeli? 30
total belanja anda adalah 85k
'''
# harga_pisang = 3000
# qty = int(input("masukkan jumlah yang ingin dibeli: "))
# qtyXharga_pisang = harga_pisang*qty
# if qtyXharga_pisang > 100000:
#     print("total belanja anda adalah:",int(qtyXharga_pisang-(qtyXharga_pisang*0.1)),"rupiah")
# elif qtyXharga_pisang >= 50000 and qtyXharga_pisang <= 100000:
#     print("total belanja anda adalah:",int(qtyXharga_pisang-(qtyXharga_pisang*0.05)),"rupiah")
# else:
#     print("total belanja anda adalah:",int(qtyXharga_pisang),"rupiah")

'''
year of service 
lebih dari 10 tahun bonus gaji 10%
berapa gaji anda? 1000000
year of service? 15
selamat anda mendapat bonus! total gaji anda 1100000
'''

# Gaji_awal = (int(input("masukkan gaji anda: ")))
# Tahun = (int(input("masukkan tahun anda bekerja: ")))
# Bonus_gaji = (Gaji_awal*0.1)
# Gaji_akhir = int(Bonus_gaji+Gaji_awal)
# if Tahun > 10:
#     print("selamat! gaji anda mengalami kenaikan menjadi", Gaji_akhir)
# else:
#     print("maaf anda belum mendapatkan bonus")
'''
Ambil 3 input umur dari 3 user lalu tentukan siapa yang lebih tua.

contoh:
in: umur user_1 = 50
in: umur user_2 = 40
in: umur user_3 = 25

out: user 1 adalah yang paling tua

contoh lain:
in: umur user_1 = 40
in: umur user_2 = 40
in: umur user_3 = 40

out: tidak ada yang lebih tua
'''
# user_1 = int(input("masukkan umur user 1: "))
# user_2 = int(input("masukkan umur user 2: "))
# user_3 = int(input("masukkan umur user 3: "))
# if user_1 > user_2 and user_1 > user_3:
#     print("user 1 adalah yang paling tua")
# elif user_2 > user_1 and user_2 > user_3:
#     print("user 2 adalah user yang paling tua")
# elif user_3 > user_1 and user_3 > user_2:
#     print("user 3 adalah yang paling tua")
# else:
#     print("tidak ada yang lebih tua")

'''
4. Buatlah program sederhana untuk menentukan apakah seorang siswa boleh mengikuti
ujian atau tidak berdasarkan presentase absennya. Minimal absensi adalah 75%.

contoh:
in: total kelas yang diadakan: 100
in: total attendances: 50

out: Total kehadiran Anda 50%. Maaf Anda tidak diperbolehkan mengikuti ujian.
'''

# kelas = int(input("total kelas yang diadakan: "))
# absen = int(input("total kehadiran: "))
# kehadiran = absen/kelas*100
# if kehadiran >= 75:
#     print(f"total kehadiran {kehadiran}%. silahkan mengikuti ujian")
# else:
#     print(f"total kehadiran {kehadiran}%. maaf anda tidak dipersilahkan mengikuti ujian")

# # cara ben
# umur_user = [] # tujuannya buat menampung segala macam inputan sebelum di olah
# umur1 = int(input("umur user1: "))
# umur2 = int(input("umur user2: "))
# umur3 = int(input("umur user3: "))
# umur_user.extend([umur1,umur2,umur3])
# help(umur_user.extend)
# # Help on built-in function extend:                                                                                                                             

# # extend(iterable, /) method of builtins.list instance
# #     Extend list by appending elements from the iterable.

# if umur1 == umur2 == umur3:
#     print("semua umur user sama")
# else:
#     tua = max(umur_user) # ngecek yang paling gede nilainya
#     print(f"umur yang paling tua adalah {tua}")
