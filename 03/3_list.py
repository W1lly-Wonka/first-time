mobil = ['Toyota', 'Honda', 'Mercedes']

# print(type(mobil)) # list
# print(mobil) # ['Toyota', 'Honda', 'Mercedes']

# # indexing
# print(mobil[0]) # toyota
# print(mobil[1]) # honda
# # print(mobil[5]) # error ga ada di index

# slicing
# print(mobil[0:2]) # ['Toyota', 'Honda']
# print(mobil[:3]) # ['Toyota', 'Honda', 'Mercedes']
# print(mobil[2:7]) # ['Mercedes'] , kalo ada sampai 7 ya lanjut
# print(mobil[::-1]) # ['Mercedes', 'Honda', 'Toyota']

# append = menambahkan element di posisi paling belakang
mobil.append('BMW') # ['Toyota', 'Honda', 'Mercedes', 'BMW']
print(mobil)
mobil.append('Mercedes') # ['Toyota', 'Honda', 'Mercedes', 'BMW', 'Mercedes']
print(mobil)

# pop = meremove element yang ada di posisi paling belakang
hasil_pop = mobil.pop() # ['Toyota', 'Honda', 'Mercedes', 'BMW'] 
print(mobil)
print(hasil_pop) # Mercedes

# index = mengetahui index dari sebuah element tertentu
print('Index dari mobil Toyota:', mobil.index('Toyota')) # 0
print('Index dari mobil Mercedes:', mobil.index('Mercedes')) # 2

print(mobil[0].index('y')) # ngecek yang ada di mobil urutan 0 index y no berapa
print(mobil[mobil.index('Mercedes')].index('s')) # sama dengan di atas
#     mobil[0].index('y')
#     'Toyota'.index('y')

# copy = membuat copy dari list
mobil_copy = mobil.copy() # ['Toyota', 'Honda', 'Mercedes', 'BMW'] 
print(mobil)
print(mobil_copy) # ['Toyota', 'Honda', 'Mercedes', 'BMW'] 

# copy = seperti kloning data, jadi 1 data bisa dimanipulasi tanpa
# mempengaruhi di atasnya

mobil_copy.pop()
print(mobil) # tidak akan terdampak oleh pop dari mobil_copy
# ['Toyota', 'Honda', 'Mercedes', 'BMW']
print(mobil_copy) 
# ['Toyota', 'Honda', 'Mercedes']
mobil2 = mobil
print(mobil)
# ['Toyota', 'Honda', 'Mercedes', 'BMW']  
print(mobil2)
# ['Toyota', 'Honda', 'Mercedes', 'BMW']  
mobil2.pop()
print(mobil)
# ['Toyota', 'Honda', 'Mercedes']
print(mobil2)
# ['Toyota', 'Honda', 'Mercedes']