mobil = ["Toyota", "Honda", "Mercedes"]
campur = [1, "surabaya", 2, True, [4,5,6]]
campur2 = [1,2,3,"4",5,6]
# print(type(campur)) # list
# print(type(campur2)) # list
# # series = 1 dimensi array = 2 dimensi

# # print(type(mobil)) # list
# print(mobil)
# # indexing
# print(mobil[0])
# print(mobil[1])
# # print(mobil[5]) tidak bisa karena lewat dari index

# # slicing
# print(mobil[0:2])#jika ingin mengambil index 1 [toyota, honda]
# print(mobil[:3])#[toyota, honda, mercedes]
# print(mobil[2:7])#mercedes
# print(mobil[::-1])#[mercedes, honda, toyota]
# print("cobain", mobil[3:])#[]

# # append = menambahkan element di posisi paling belakang
# mobil. append("BMW")
# print(mobil) #[toyota,honda, mercedes, bmw]
# mobil. append("Mercedes") #penambahan berulang masih bisa nanti nambah terus tanpa memperhatikan yang sudah ada
# print(mobil)#[toyota,honda, mercedes, bmw,mercedes]

# # pop = meremove element di posisi paling belakang ke suatu tempat di luar yang sudah ada
# # untuk memunculkan yang sudah dihapus oleh pop harus di define cth sbb
# hasil_pop = mobil.pop() #kurung kosong = function / method
# mobil.pop() #mobil.pop panggil atribut
# print(mobil)#[toyota,honda, mercedes, bmw]
# print(hasil_pop) #mercedes
# mobil.pop(1)
# print(mobil)

# # "python".append("a") # str does not attribute append. list punya function sendiri

# # index = mengetahui index dari sebuah element tertentu
# print("index dari mobil Toyota: " , mobil.index("Toyota"))
# print("index dari mobil Mercedes: " , mobil.index("Mercedes"))
# print( mobil[0].index("y"))
# print(mobil[mobil.index("Toyota")].index("y"))
# # mobil[0].index("y")
# # "Toyota".index("y")
# print(mobil[mobil.index("Mercedes")].index("s"))

# # copy = membuat copy dari list
# mobil_copy = mobil.copy()
# print(mobil)
# print(mobil_copy)

# mobil_copy.pop() #ketika mengcopy, tidak ada berdampak pada variabel mobil
# print(mobil) #tidak akan terdampak oleh pop dari mobil_copy
# print(mobil_copy)

# mobil2 = mobil #akan berdampak pada variabel mobil
# print(mobil)
# print(mobil2)
# mobil2.pop() 
# print(mobil)
# print(mobil2)


# # insert = memasukkan element ke index yang ditentukan tapi di taro di depan, yang lain tergeser
# mobil.insert(0,"Hummer")
# print(mobil)
# mobil.insert(10,"Citroen")
# print(mobil)
# mobil.insert(2,"Jaguar")
# print(mobil)
# # mobil.insert(3,["BMW", "Porsche"])
# # print("tes masukin list", mobil)
# # bikin bingung list dalam list mau di sort 

# #sort = mengurutkan (reverse = True / False) awal abjad, huruf kedua dst atau awal angka
# # print(mobil.sort(reverse=True).index("Citroen") #tidak bisa
# # print(mobil)
# mobil.sort(reverse=False)
# mobil.sort()
# print(mobil) # ['Citroen', 'Hummer', 'Jaguar', 'Toyota'] 
# print(mobil.index("Citroen"))

# # reverse = membalik urutan dari list 
# mobil.reverse() 
# print(mobil) # ['Toyota', 'Jaguar', 'Hummer', 'Citroen'] 

# #callable = function yang kita buat sendiri misal buat hitung luas persegi
# a = [4,3,2,5,6,7]
# print(a[::-1])
# a.reverse()
# print(a)
# a.sort(reverse=True)
# print(a)
# a.sort(reverse=False)
# print(a)

# b = ["Python","Java","C","Javascript"]
# b.reverse()
# print(b)
# b.sort(reverse=True)
# print(b)

# # count = menghitung ada berapa element tertentu dalam sebuah list
# print(mobil.count("Toyota"))
# mobil.append("Toyota")
# print(mobil.count("Toyota"))

# # extend = memasukkan beberapa element sekaligus 
# # mobil.append("Ferrari", "Honda", "Toyota") tidak bisa maximal 1 argument
# mobil.append(["Ford", "Honda", "Toyota"])
# print(mobil)
# print(mobil[5])
# mobil.extend(["Ford", "Honda", "Toyota"])
# print(mobil)
# # mobil.extend("Ferrari") # string bagian dari iterable
# # print(mobil)

# print(mobil[5][0]) #manggil spesifik 
# # ["Ford","Honda","Toyota"][0]
# # Ford
# print(mobil[5][0][1])

# # cara mengganti element pada index tertentu
# # mobil[5] = "Ford"
# # print(mobil)
# mobil[5][1] = "Porsche"
# # mobil[5][1][3] = "a" TypeError: 'str' object does not support item assignment
# print(mobil)

# # broadcasting
# mobil[0:3] = "Porsche","Ford","Toyota"
# print(mobil)
# mobil[3],mobil[5],mobil[7] = "Ford","Toyota","BMW"
# print(mobil)
# # mobil[0:3] = "Mercedes" #['M', 'e', 'r', 'c', 'e', 'd', 'e', 's', 'Ford', 'Toyota', 'Toyota', 'Ford', 'BMW', 'Toyota']
# mobil[0:3] = ["Mercedes"] # bisa tapi mengurangi panjang dari list kita
# # ['Mercedes', 'Ford', 'Toyota', 'Toyota', 'Ford', 'BMW', 'Toyota']
# print(mobil)

# # in = untuk mengecek apakah element tertentu ada di dalam sebuah list
# print("Toyota" in mobil) #True
# print("Porsche" in mobil) #False
# print(mobil[4] in mobil) #"Toyota" in mobil

## tuple = value yang di dalam tidak bisa diubah, mirip list
# angka = (1,2,3,4,5,6,7,2,2)
# print(type(angka)) # tuple
# # count = menghitung element tertentu
# print(angka.count(2)) # 3
# # angka.append(9) AttributeError: 'tuple' object has no attribute 'append'
# # angka.pop() AttributeError: 'tuple' object has no attribute 'pop'
# # angka.extend([1]) AttributeError: 'tuple' object has no attribute 'extend'
# # angka.reverse() AttributeError: 'tuple' object has no attribute 'reverse'
# print(angka[3]) # 4
## list of tuple
# kartu_kredit = [(1212121212121212, 606),(1212121212121212, 414)]
# print(kartu_kredit)
# huruf = ("a","b","c","c","d") # 2, ini tuple
# print(huruf.count("c"))
# kata = "python forever" # 2, ini string
# print(kata.count("o"))

# # set
# # {} set dan dictionary (key)
# z = {1,2,3,1,2,3,4,4,4,4,4}
# print(type(z)) # set
# z2 = {}
# print(type(z2)) # dict
# print(z)
# z_list = list(z)
# print(z_list)

# z.add(5) #menambah element baru
# print(z)
# z.add("Budi") # {1, 2, 3, 4, 5, 'Budi'}
# print(z)
# # update = menambahkan beberapa element sekaligus
# # harus memasukkan data dalam bentuk iterable (list,tuple, set, string(akan terpecah))
# z.update([5,6,7,8]) # {1, 2, 3, 4, 5, 6, 7, 8, 'Budi'}
# print(z)
# print(type(z))
# z.update("Andy","Caca") # {1, 2, 3, 4, 5, 6, 7, 8, 'n', 'A', 'y', 'c', 'Budi', 'a', 'C', 'd'}
# print(z)
# # error karena ga berurutan, set dengan tuple
# # print(z[1]) TypeError: 'set' object is not subscriptable
# # print(z[1:]) #TypeError: 'set' object is not subscriptable
# # z.add("Andy"){1, 2, 3, 4, 5, 6, 7, 8, 'Andy'}
# # print(z)
# z.update("Andy") # {1, 2, 3, 4, 5, 6, 7, 8, 'n', 'A', 'y', 'c', 'Budi', 'a', 'C', 'd'}
# print(z)
# #ga ada pengaruh karena andy sudah ada sebelumnya


# #discard = menghapus 1 element tertentu
# z.discard("Budi")
# print(z)
# # z.discard(["A","n","d","y"]) TypeError: unhashable type: 'list'
# # print(z)

# # pop = meremove 1 element tertentu, random
# z.pop()
# print("pop pertama",z)
# z.pop()
# print("pop kedua",z)
# z.pop()
# print("pop ketiga",z)
# z.pop()
# print("pop keempat",z)
# z.pop()
# print("pop keempat",z)

#clear = menghapus semua element di dalam set
# z.clear()
# print(z)
# angka_list = list(angka)
# print(angka_list)

# rand_tuple = (1,3,5,6,7,8,9)
# print(rand_tuple)
# rand_list = list(rand_tuple)
# print(rand_list)
# # (1, 3, 5, 6, 7, 8, 9) => [1, 3, 5, 6, 7, 8, 9]
# rand_list.append(10)
# print(rand_list)
# back_to_tuple = tuple(rand_list)
# print(back_to_tuple)
# # [1, 3, 5, 6, 7, 8, 9, 10] => (1, 3, 5, 6, 7, 8, 9, 10)
# rand_set = set(back_to_tuple)
# print(rand_set)
# # (1, 3, 5, 6, 7, 8, 9, 10) => {1, 3, 5, 6, 7, 8, 9, 10}

# a = list ("abcdeaaaaaaaaaaa")
# b = list ("bcfga")
# c = ["Halo", "Apa", "Kabar"]
# d = "-".join(c) 
# print(d) # Halo-Apa-Kabar
# print(a,b)
# # ['a', 'b', 'c', 'd', 'e', 'a', 'a', 'a', 'a', 
# # 'a', 'a', 'a', 'a', 'a', 'a', 'a'] ['b', 'c', 
# # 'f', 'g', 'a']
# a_set = set(a)
# b_set = set(b)
# print(a_set, b_set)
# # {'c', 'e', 'd', 'a', 'b'} {'c', 'a', 'f', 'g', 'b'}
# print("irisan/intersection dari set_a dan set_b: ", a_set.intersection(b_set))
# # irisan/intersection dari set_a dan set_b:  {'a', 'b', 'c'}
# print("irisan/intersection dari set_a dan set_b: ", a_set&(b_set))
# # irisan/intersection dari set_a dan set_b:  {'a', 'b', 'c'}
# print("selisih/difference dari set_a dan set_b: ", a_set.difference(b_set))
# # selisih/difference dari set_a dan set_b:  {'e', 'd'}
# print("selisih/difference dari set_b dan set_a: ", b_set.difference(a_set))
# # selisih/difference dari set_b dan set_a:  {'f', 'g'}

# print("gabungan/union dari set_a dan set_b: ", a_set.union(b_set))
# # gabungan/union dari set_a dan set_b:  {'c', 'e', 'f', 'd', 'g', 'a', 'b'}
# print("beda setangkup/symmetric difference dari set_a dan set_b: ", a_set.symmetric_difference(b_set))
# # beda setangkup/symmetric difference dari set_a dan set_b:  {'f', 'g', 'e', 'd'}
# # total yang beda dari set_a dan set_b
'''
set
p = 1,2,4,7,9,19
q = 5,12,16,17,7,9,19,6
r = 19,6,3,8

1 union p q
2 union p r
3 union q r
4 irisan union p q dan q r
5 symmetric difference dari union q r dan p q
'''
# p = {1,2,4,7,9,19}
# q = {5,12,16,17,7,9,19,6}
# r = {19,6,3,8}
# # 1
# # print (p.union(q))
# p_q = p|q
# # 2
# # print(p.union(r))
# p_r = p|r
# # 3
# # print(q.union(r))
# q_r = q|r
# # 4
# print(p_q)
# print(p_r)
# print(q_r)
# print(p_q&q_r)
# print(q_r.symmetric_difference(p_q))