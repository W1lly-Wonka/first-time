# # problem no 1
# # diketahui sbb
# x = 4
# y = 3
# z = 2
# # ditanyakan
# w = ((x+y*z)/(x*y))**z
# # jawab
# print(w)
# # selesai 

# problem no 2
# diketahui sbb 
# silahkan masukkan angka berapapun : 4
# ditanyakan 
# kuadrat dari 4 = 16
# jawab 
# a = input ("silahkan masukkan angka yang diinginkan : ")
# b = input ("silahkan masukkan pangkat yang diinginkan : ")
# c = int(a)**int(b)
# print(c)
# selesai

# # problem no 3
# # diketahui sbb 
# # 485 hari, 1 bulan = 30 hari, 1 tahun = 360 hari 
# # ditanyakan 
# # jabarkan 485 hari dalam tahun bulan minggu hari 
# # jawab 
# import math
# a = int(input("masukkan angka: "))
# tahun = math.floor(float(a/360))
# bulan = math.floor(float(a%360/30))
# minggu = math.floor(float(a%360%30/7))
# hari = a%360%30%7
# print( a, 'hari', '=', tahun, 'Tahun', bulan, 'Bulan' ,minggu, 'Minggu', hari, 'Hari' )
# # selesai

# problem no 4
# diketahui usia andi + budi 49 tahun dengan rasio usia andi dan budi = 0.4
# ditanyakan
# berapa usia andi dan budi 2 tahun lagi?
# jawab 
# menggunakan cramer's rule
# a = andi
# b = budi
# a + b = 49
# rasio a/b = 0.4 -> a = 0.4 b / a - 0.4 b = 0
# (1 -0.4) (a) = (0)
# (1    1) (b)   (49)
# a = input ("silahkan masukkan angka yang diinginkan : ")
# b = input ("silahkan masukkan pangkat yang diinginkan : ")
# a1 = 1
# a2 = 1
# b1 = float (input("silahkan masukkan rasio yang diinginkan (tulis dalam negatif) : "))
# b2 = 1
# c1 = 0
# c2 = int (input("silahkan masukkan jumlah usia yang diinginkan : "))
# andi = ((c1*b2-b1*c2)/(a1*b2-b1*a2))
# print("usia andi 2 tahun ke depan adalah",andi+2)
# budi = ((a1*c2-c1*a2)/(a1*b2-b1*a2))
# print("usia budi 2 tahun ke depan adalah",budi+2)
# selesai

#problem no 5
# diketahui 
# misal halo dunia memiliki huruf a sebanyak 2 buah
# ditanyakan
# buat algoritma untuk menghitung karakter tertentu dalam string 
# jawab 
# x = input("silahkan masukkan kata apa saja: ")
# print (x.count('a'))
# selesai 

# # cara lain ben
# text = input("masukkan kata / kalimat anda: ")
# text_list = list((text).lower())
# print(text)
# huruf = input("masukkan huruf yang akan dihitung: ")
# huruf_lower = huruf.lower()
# print(huruf)
# banyak = text_list.count(huruf_lower)
# print(banyak)
# print(f"banyak huruf {huruf} dalam kata / kalimat \"{text}\" adalah {banyak} buah") 
# # penggunaan \ setelah tanda "" bertujuan untuk memperbolehkan petik yang sama walau di luar sudah ada petik

# cara lain lagi 
# text = input("masukkan text / kalimat anda: ")
# # print(text)
# # text_len =len(text.lower())
# # print(text_len)
# text_len1 =len(text)
# # print(text_len1)
# huruf = input("masukkan huruf yang ingin dihitung: ")
# huruf_lower = huruf.lower()
# # print(huruf)
# text_rep = text.replace(huruf_lower, "")
# text_len2 = len(text_rep)
# # print(text_len2)
# # print(len(text_len2))
# selisih = text_len1 - text_len2
# print(f"jumlah huruf {huruf} dalam {text} adalah sebanyak {selisih} buah")


# problem no 6
# diketahui
# jarak a - b = 120 km
# a = 60 km / h dari arah timur
# b = 40 km / h dari arah barat
# a & b jalan jam 9
# ditanyakan
# jamber a & b tabrakan?
# jawab
# import math
# a = int (input("silahkan masukkan waktu awal : ")) 
# s = int (input ("silahkan masukkan jarak : "))
# Va = int (input ("silahkan masukkan kecepatan mobil a : "))
# Vb = int (input ("silahkan masukkan kecepatan mobil b : "))
# # ta = tb karena waktu bertabrakan sama (kecepatan konstan) / percepatan = 0
# t = (s / (Va + Vb))
# print("A dan B akan bertabrakan pada pukul" ,a + math.floor(t),":",int (t*60%60))
# selesai


# no 1
# x = 4
# y = 3
# z = 2
# w = ((x+y*z)/(x*y))**z
# print (w)
# no 2
import math
# angka = int(input("silahkan masukkan angka berapapun: "))
# pangkat = int(input("silahkan masukkan pangkat berapapun:"))
# print("pangkat", pangkat, "dari angka", angka, "adalah: ", int(math.pow(angka,pangkat)))
# no 3
# total_hari = int(input("masukkan hari: "))
# tahun = str(math.floor(total_hari/360))
# bulan = str(math.floor(total_hari%360/30))
# minggu = str(math.floor(total_hari%360%30/7))
# hari = str(math.floor(total_hari%360%30%7))
# print(str(total_hari) + "=" + tahun + "tahun" + bulan + "bulan" + hari + "hari")
# no 4
# total = int(input("total umur andi dan budi: "))
# rasio = float(input("rasio umur andi dan budi: "))
# umur_budi = (total*10) / (10+(rasio*10))
# umur_andi = total - umur_budi
# print("umur andi 2 tahun lagi adalah: {}".format(umur_andi + 2))
# print(f"umur budi 2 tahun lagi adalah: {umur_budi + 2}")
# int + float = float
# print(int(1 + 0.5))
# print(2 * 0.5)
# print(round(10//5.5,5))
# no 5
# word = input("masukkan kata / kalimat: ").lower()
# cari = input(f"input huruf yang ingin dicari jumlahnya dari '{word}' : ").lower()
# word2 = word.replace(cari, "")
# print(f"huruf {cari} ada  {len(word)-len(word2)} buah")
# no 6
