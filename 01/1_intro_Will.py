# print('Hello world!') #string tanpa masuk variable harus kasih tanda petik

# print(29) #ini adalah variabel jadi ga perlu tanda petik

# #fungsi print mencetak sesuatu

# nama = 'ridho' #string
# umur = 29 #integer
# pekerjaan = 'lecturer' 
# tinggi = 173.5 #float
# jomblo = False #boolean true or false

# x, y, z = "Orange", "Banana", "Cherry"

# print(x)
# print(y)
# print(z)

# Orange
# Banana
# Cherry

# x = "awesome"

# def myfunc():
#   print("Python is " + x)

# myfunc()

# Python is awesome

# print(nama)
# print(umur)
# print(pekerjaan)
# print(jomblo)
# print(type(jomblo))

# print(False + False) # 0 + 0
# print(True + True) # 1 + 1
# print(True + False) # 1 + 0

# a = 1
# b = 2
# c = 1
# print(a == b) # a tidak sama dengan b hasilnya false
# print(a == c) # a sama dengan c hasilnya true

# print(type(nama))
# print(type(umur))
# type(nama)
# dtype_nama = type(nama)
# dtype_umur = type(umur)

# print(dtype_nama)
# print(dtype_umur)

# nama = input('what is your name: ')
# print('hello my name is ' + nama + ' umur saya ' + str(29)) #jika menggunakan + harus ditambah spasi dalam string
# print('hello my name is', nama, 'umur saya', 29)#jika menggunakan , tidak perlu ditambah spasi
# #mungkin sedikit tambahan, kalo menggunakan + type dari elementnya harus sama, klo pke , bisa beda (str dan int bisa)

# x = "awesome"

# def myfunc():
#   x = "fantastic"
#   print("Python is " + x) # hasilnya Python is fantastic

# myfunc() # harus ada karena agar fantastic bisa jalan

# print("Python is " + x) # hasilnya Python is awesome

# def myfunc():
#   global x
#   x = "fantastic"

# myfunc()

# print("Python is " + x) # kalo di print bisa keluar hasilnya karena menggunakan kata global pada x

# x = "awesome"

# def myfunc():
#   global x
#   x = "fantastic"

# myfunc()

# print("Python is " + x) # kata global dalam fungsi akan mengganti kata awesome dengan fantastic 


# nama = 25
# print(nama)
# #shortcut otomatis komen = ctrl / (di blok dulu yang mau di komen)

# print(2-1)
# print(2+1)
# print(3*2)
# print(4/2) #2.0 adalah float
# print(4//2) # pembagian 2 => int  
# print(5%2)#modulo
# print(5/2)
# print(5//2)#pembulatan ke bawah
# print(2**3) #pangkat/power

#mengganti data types
# x = '10'
# print(type(x))
# y = int(x)
# print(type(y))

# z = '25.5'
# print(float(z))

# a = 23
# a_str = str(a)
# print(a_str)
# print(type(a_str))

# b = 1.5
# b_str = str(b)
# print(b_str)
# print(type(b_str))

# c = '2'
# #12.0
# print(float(c)+10)

#nama = 'randy' (input)
#umur = 26 (input)
#Hallo nama saya randy, umur saya 5 tahun ke depan adalah 31

# nama = input('what is your name: ')
# umur = input('input your age: ') #datatypes selalu string, ketika menggunakan input
# print('halo nama saya', nama, ',umur saya 5 tahun ke depan adalah', int(umur)+5)
# print('halo nama saya ' + nama + ',umur saya 5 tahun ke depan adalah ' + str(int(umur)+5))

# usiaAndi = 30
# usiaAndi = usiaAndi + 5
# usiaAndi += 5
# usiaAndi *=2
# usiaAndi/=2
# print(usiaAndi)

# from math import pi, fabs, pow, sqrt, ceil, floor #jika hanya butuh beberapa fungsi saja
# print (pi)
# import math as m 
# print(m.pi)
# import math #cara 1, jika butuh semua fungsi yang ada di math
# print(math.pi)
# print(math.fabs(-4.7))
# print(math.pow(2,4))
# print(math.sqrt(16))
# print(math.ceil(2.5))#pembulatan ke atas
# print(math.floor(2.5))#pembulatan ke bawah
# print(round(5.555667, 0))

# x = 'halo dunia lain' 
# print(x) # halo dunia lain
# print(type(x)) # <class 'str'>
# print(len(x)) #character juga kena print = 15
# print(x.index('a')) #index (no.kamar) mulai dari 0123456789, case sensitive = 1
# #max index = len-1, karena mulainya dari 0
# print(x.split()) #memisahkan kemudian jadi list (daftar akan sesuatu, string, integer, float, boolean dll)
# ## ['halo', 'dunia', 'lain']
# print(x.split('a')) # ['h', 'lo duni', ' l', 'in']
# print(x.lower()) # halo dunia lain
# print(x.upper()) # HALO DUNIA LAIN
# print(x.capitalize()) # Halo dunia lain
# print('halo dunia lain. apa kabar'.capitalize()) # Halo dunia lain. apa kabar = kapital di awal saja, setelah titik tidak ada
# print(x.replace('dunia', 'apa')) # halo apa lain
# txt = " Hello World " 
# x = txt.strip()
# print(x) # Return the string without any whitespace at the beginning or the end.


# print("halo hari jum'at") #double qoute
# print('halo hari jum'at') #akan error = invalid syntax
# print('''halo hari "jum'at"''') #triple quote

# age = 36
# txt = "My name is John, and I am {} "
# print(txt.format(age)) # My name is John, and I am 36

# help(txt.format)

# format(...) method of builtins.str instance
#     S.format(*args, **kwargs) -> str

#     Return a formatted version of S, using substitutions from args and kwargs.
#     The substitutions are identified by braces ('{' and '}').

# print(bool("abc")) # True

# fruits = {"apple", "banana", "cherry"}
# more_fruits = ["orange", "mango", "grapes"]
# fruits.update(more_fruits) # {'orange', 'apple', 'banana', 'cherry', 'grapes', 'mango'}
# print(fruits)
# fruits.discard("apple")
# print(fruits)
# # help(fruits.discard) # discard(...) method of builtins.set instance
#     # Remove an element from a set if it is a member.

#     # If the element is not a member, do nothing.
# fruits.remove("cherry")
# print(fruits)
# # help(fruits.remove) # remove(...) method of builtins.set instance
    # Remove an element from a set; it must be a member.

    # If the element is not a member, raise a KeyError.

# Add the key/value pair "color" : "red" to the car dictionary.
# car =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# car["color"] = "red" # {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'} 
# print(car)

# if 5 > 2:
#     print("Five is greater than two!")
# hasilnya akan sama dengan yang di bawah
# if 5 > 2: print("Five is greater than two!")

# if 5 > 2:
#     print("Yes")
# else:
#     print("No")
# hasilnya akan sama dengan yang di bawah
# print("Yes") if 5 > 2 else print("No")

# i = 1
# while i < 6:
#   print(i)
#   i += 1
# else:
#     print("i is no longer less than 6")

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#     print(x) # printnya jadi 1 1 ke bawah

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#     if x == "banana":
#         continue

# print(x) # jadinya cuma print cherry aja

# # If you do not know the number of arguments that will be passed into your function, 
# # there is a prefix you can add in the function definition, which prefix? yaitu *

# def my_function(*kids):
#     print("The youngest child is " + kids[2])
 
# If you do not know the number of keyword arguments that will be passed into your function, 
# there is a prefix you can add in the function definition, which prefix? yaitu **
# def my_function(**kid):
#     print("His last name is " + kid["lname"])


# indexing and slicing
# index berdasarkan no. kamar
x = "halo dunia lain"
#0123456789
#-15-14-13-12-11-10 dst
# print(x[0]) # h
# print(x[4]) # spasi
# print(x[3]) # 0
# print(x[14]) # n
# print(x[-15]) # h
# print(x[-16]) #error string index out of range

# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# thisdict["year"] = 2018 # {'brand': 'Ford', 'model': 'Mustang', 'year': 2018}

# print(thisdict)


# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#     print(x)
#     if x == "banana": # stop sampai banana
#         break

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#     if x == "banana":
#         break
#     print(x) # apple



#slicing harus len+1, spasi harus di hitung
# start, stop, step 
# print(x[0:4]) # halo
# print(x[5:10]) # dunia
# print(x[5:]) # dunia lain
# print(x[x.index('d'):]  ) # 
# print(x[:x.index('l')])
# print(x[:11])
# print(x[:-4])
# start:stop:step 
# print(x[0:15:2])
# print(x[0:15:1])
# print(x[::-1])
# print(x[-1:-5:-1])
# print(x[:])

#kerjakan soal 1-4,6

# #boolean value
# print(True+True) #true = 1
# print(True+False) #false = 0
# a = 1 #= declaration == conditional statement
# b = 2
# c = 1
# print(a==b)
# print(a==c)
#penting untuk for while loop, if else juga penting, mengecek apakah kondisi sudah benar atau tidak

# latian di file pdf

# nama = input ("what's your name? ")
# print("Nama : " + nama)
# umur = input ("how's your age? ")
# print("Umur : " + umur)
# jenis_kelamin = input ("what's your gender ")
# print("Jenis kelamin saya : " + jenis_kelamin)
# pekerjaan = input ("what do you do for a living?: ")
# print("Saya bekerja sebagai " + pekerjaan)
# ## nice work william

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

# # problem no 2
# # diketahui sbb 
# # silahkan masukkan angka berapapun : 4
# # ditanyakan 
# # kuadrat dari 4 = 16
# # jawab 
# a = input ("silahkan masukkan angka yang diinginkan : ")
# b = input ("silahkan masukkan pangkat yang diinginkan : ")
# c = int(a)**int(b)
# print(c)
# # selesai

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

import math
# help(SyntaxError)
# help(print)
# for i in range(10):
#     print(i)
# username = input("masukkan nama anda: ").lower()
# if username == "petanikode":
#     print("selamat datang admin")
#     print("silahkan ambil tempat duduk")
# else:
#     print("maaf anda bukan admin")
# n = input("any number: ")
# m = n
# print(m)
# help("keywords")