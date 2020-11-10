##  dictionary = "key", "value"
employee = {
    # key : value
    "nama":"Andy",
    "usia":20,
    "married":True,
    "jabatan":"IT Engineer",
    "kendaraan":["mobil","motor"],
    "address":{
        "street":"Jalan Mawar",
        "RT": 5,
        "RW": 2,
        "zipcode":12345,
        "geo":{
            "lat":123.456,
            "long":123.456
        }
    }
}
# print(employee)
# {'nama': 'Andy', 'usia': 20, 'married': True, 'jabatan': 'IT Engineer', 'kendaraan': ['mobil', 'motor'], 'address': {'street': 'Jalan Mawar', 'RT': 5, 'RW': 2, 'zipcode': 12345, 'geo': {'lat': 123.456, 'long': 123.456}}}
# print("Value di dalam key'nama' adalah: ", employee["nama"]) # andy
# print("Value di dalam key'kendaraan' adalah: ", employee["kendaraan"])  #  ['mobil', 'motor']
# print("Value di dalam key'kendaraan' di index pertama adalah: ", employee["kendaraan"][0]) # mobil
# print("Value di dalam key'address' adalah: ", employee["address"])
# {'street': 'Jalan Mawar', 'RT': 5, 'RW': 2, 'zipcode': 12345, 'geo': {'lat': 123.456, 'long': 123.456}}
# print("Value di dalam key'address' nama jalan saja adalah: ", employee["address"]["street"]) # Jalan Mawar


# print(list(employee.keys())) # jadi list ['nama', 'usia', 'married', 'jabatan', 'kendaraan', 'address']
# print(list(employee.values())) 
# ['Andy', 20, True, 'IT Engineer', ['mobil', 'motor'], {'street': 'Jalan Mawar', 'RT': 5, 'RW': 2, 'zipcode': 12345, 'geo': {'lat': 123.456, 'long': 123.456}}]
# print(employee.get("address","tidak ada"))
# {'street': 'Jalan Mawar', 'RT': 5, 'RW': 2, 'zipcode': 12345, 'geo': {'lat': 123.456, 'long': 123.456}}
# print(employee.get("address","tidak ada").get("geo", "tidak ada")) # {'lat': 123.456, 'long': 123.456}
# # print(employee.get("address","tidak ada").get("geo", "tidak ada").get("zipcode","tidak ada") #invalid syntax
# print(employee.get("address","tidak ada").get("geo", "tidak ada").get("lat","tidak ada")) #harus turun terus ga bisa turun 1 step kemudian ambil data yang sama
# 123.456
## {'street': 'Jalan Mawar', 'RT': 5, 'RW': 2, 'zipcode': 12345, 'geo': {'lat': 123.456, 'long': 123.456}}
# # {'lat': 123.456, 'long': 123.456}
# # 123.456
# print(employee.get("gaji","tidak ada")) # tidak ada di dict
# print(employee.get("gaji")) # none
# print(employee.get["gaji"]) # TypeError: 'builtin_function_or_method' object is not subscriptable

# # assign value baru ke key yang juga baru
# employee["gaji"] = 2000000
# print(employee)
# {'nama': 'Andy', 'usia': 20, 'married': True, 'jabatan': 'IT Engineer', 'kendaraan': ['mobil', 'motor'], 'address': {'street': 'Jalan Mawar', 'RT': 5, 'RW': 2, 'zipcode': 12345, 'geo': {'lat': 123.456, 'long': 123.456}}, 'gaji': 2000000}

# # update value di key yang sudah ada
# employee["gaji"] = 3000000
# print(employee)
# employee["kendaraan"].append("scooter")
# print(employee)


# .update untuk update beberapa keys sekaligus
# dalam bentuk dictionary

# employee.update({"NIK":987654321, "BPJS":123456})
# print(employee)

# # .items
# # looping = mencari key berdasarkan value, mencari key yang isinya list 
# print(list(employee.items()))
# # [('nama', 'Andy'), ('usia', 20), ('married', True), ('jabatan', 'IT Engineer'), ('kendaraan', ['mobil', 'motor']), ('address', {'street': 'Jalan Mawar', 'RT': 5, 'RW': 2, 'zipcode': 
# # 12345, 'geo': {'lat': 123.456, 'long': 123.456}})]
# print(list(employee["address"].items()))
# # [('street', 'Jalan Mawar'), ('RT', 5), ('RW', 2), ('zipcode', 12345), ('geo', {'lat': 123.456, 'long': 123.456})]
# print(list(employee["address"]["geo"].items()))
# # [('lat', 123.456), ('long', 123.456)]
# print(employee.items())
# # dict_items([('nama', 'Andy'), ('usia', 20), ('married', True), ('jabatan', 'IT Engineer'), ('kendaraan', ['mobil', 'motor']), ('address', {'street': 'Jalan Mawar', 'RT': 5, 'RW': 2, 
# # 'zipcode': 12345, 'geo': {'lat': 123.456, 'long': 123.456}})])

# # cari value ada atau tidak di dict 
# print("cari value 3000000 ada atau ga?: ",3000000 in employee.values())


# # value terkecil atau terbesar

# nilai_ujian = {
#     "Fisika" : 82,
#     "Matematika" : 82,
#     "Sejarah":75
# }

# print("mata pelajaran yang nilainya paling kecil:",min(nilai_ujian,key=nilai_ujian.get))
# print("mata pelajaran yang nilainya paling besar:",max(nilai_ujian,key=nilai_ujian.get))

# # mengganti nama key

# employee["alamat"] = employee.pop("address")
# print(employee)
# {'nama': 'Andy', 'usia': 20, 'married': True, 'jabatan': 'IT Engineer', 'kendaraan': ['mobil', 'motor'], 'alamat': {'street': 'Jalan Mawar', 'RT': 5, 'RW': 2, 'zipcode': 12345, 'geo': {'lat': 123.456, 'long': 123.456}}}



# # menggabungkan 2 dict 
# dict1 = {"ten":10,"twenty":20,"thirty":30}
# dict2 = {"forty":40,"fifty":50,"sixty":60}

# # .update 

# dict3 = dict1.copy()
# dict3.update(dict2)
# print(dict3)

# # cara lain

# dict1_dict2 = {**dict1,**dict2} #dict
# print(dict1_dict2)
# dict1_dict2 = [*dict1,*dict2] # ['ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty']
# print(dict1_dict2) 


# # membuat 2 buah dict dari 2 buah list 

# key = ["ten","twenty","thirty"] #list
# value = [10,20,30] # list
# sample_dict = dict(zip(key, value))
# print(sample_dict) # {'ten': 10, 'twenty': 20, 'thirty': 30}
# sample_dict_reversed = dict(zip(value, key))
# print(sample_dict_reversed) # {10: 'ten', 20: 'twenty', 30: 'thirty'}

# sample_list = list(zip(key,value))
# print("ini sample list",sample_list) # ini sample list [('ten', 10), ('twenty', 20), ('thirty', 30)]
# sample_tuple = tuple(zip(key,value))
# print("ini sample tuple",sample_tuple) # ini sample tuple (('ten', 10), ('twenty', 20), ('thirty', 30))



# dict1_dict2 = {*key,*value} #dict #tetep jadi list ga jadi dict
# print(dict1_dict2) # {'thirty', 'twenty', 'ten', 10, 20, 30}

# # initialize dictionary with default values
# karyawan = ["doni","fiki","akbar"]
# defaults = {"designation" : "application developer", "salary":5000000}
# res_dict = dict.fromkeys(karyawan,defaults)
# print(res_dict) 
# # {'doni': {'designation': 'application developer', 'salary': 5000000}, 'fiki': {'designation': 'application developer', 'salary': 5000000}, 'akbar': {'designation': 'application developer', 'salary': 5000000}}
# print(res_dict["doni"])
# # {'designation': 'application developer', 'salary': 5000000}


'''
No. 1
Masukkan hari: Senin 
output: bahasa inggris dari Senin adalah Monday

No. 2
Masukkan hari (INA/ENG): senin
output: bahasa inggris dari senin adalah Monday

Masukkan hari (INA/ENG): monday
output: bahasa indonesia dari monday adalah Senin
'''
# dicthari = {
#     'senin': 'Monday',
#     'selasa': 'Tuesday',
#     'rabu': 'Wednesday',
#     'kamis': 'Thursday',
#     'jumat': 'Friday',
#     'sabtu': 'Saturday',
#     'minggu': 'Sunday'
#     }
# hari = input('Masukkan hari: ').lower()
# print(f'Bahasa Inggris dari {hari.capitalize()} adalah {dicthari[hari]}')
# # print(f"bahasa inggris dari {hari.get()}") # AttributeError: 'str' object has no attribute 'get'
# print(dicthari.get("senin"))
# # print(employee.get("address","tidak ada"))
'''
kata rangga sebenarnya ga perlu lewat list, dict sendiri akan otomatis ngecek keys mereka
'''
# hari_dict = {
#     'senin': 'Monday',
#     'selasa': 'Tuesday',
#     'rabu': 'Wednesday',
#     'kamis': 'Thursday',
#     'jumat': 'Friday',
#     'sabtu': 'Saturday',
#     'minggu': 'Sunday'
# }
# # hari = input("masukkan hari: ").lower() # atau bisa juga
# hari = input("masukkan hari: ") 
# hari.lower() # urutan harus diperhatikan ya, dimana kalo hari tsb harus didefinisikan terlebih dahulu

# # if hari in list(hari_dict.keys()):
# #     print(f"bahasa inggris dari hari {hari.capitalize()} adalah {hari_dict[hari].capitalize()}")
# ## atau bisa juga seperti ini, tanpa perlu menggunakan list untuk mengecek keys di dict, agar lebih efisien

# if hari in hari_dict:
#     print(f"bahasa inggris dari hari {hari.capitalize()} adalah {hari_dict[hari].capitalize()}")
# else:
#     print("invalid input")

'''
'''

# dicthari = {
#     'senin': 'monday',
#     'selasa': 'tuesday',
#     'rabu': 'wednesday',
#     'kamis': 'thursday',
#     'jumat': 'friday',
#     'sabtu': 'saturday',
#     'minggu': 'sunday'

# }
# hari = input ("hari dalam INA/ENG: ").lower()
# ina = list(dicthari.keys())
# # ina = (dicthari.keys())
# # print(ina)
# # print(type(ina))
# eng = list(dicthari.values())
# # eng = (dicthari.values())
# ## print(eng)
# if hari in ina:
#     print(f"bahasa inggris dari hari {hari.capitalize()} adalah {dicthari[hari].capitalize()}")
# elif hari in eng:
#     print(f"bahasa indonesia dari hari {hari.capitalize()} adalah {ina[eng.index(hari)].capitalize()}")
# else:
#     print(f"input \"{hari}\" yang anda masukkan bukan termasuk dalam kategori hari")

# def GetKey(key,val):
#    for key, value in dicthari.items():
#       if val == value:
#          return key
#       return "key doesn't exist"
#       else:
#           if key == key:
#             return value
#       return "value doesn't exist"

# print(GetKey("monday"))

# nama = input("Nama: ")
# umur = int(input("Umur: "))
# x = -1*(umur%2)+5

# print('karakter nama saya pada posisi index modulus 2 dari umur saya adalah',nama[umur%2])
# print(nama[-1*(umur%2)+5:-1])

# # zip
# angka = [1,2,3,4,5]
# huruf = ['a', 'b', 'c', 'd', 'e']

# print(dict(zip(huruf,angka)))
# print(list(zip(huruf,angka)))

# from functools import reduce

# number = [1,2,3,4]
# n = reduce(lambda a, b: a*b, number)
# print(n)


# kata = ['ini', 'ibu', 'budi']
# a = reduce(lambda a, b: a+' '+b, kata)
# print(a)

hari_dict = {
    'senin': 'monday',
    'selasa': 'tuesday',
    'rabu': 'wednesday',
    'kamis': 'thursday',
    'jumat': 'friday',
    'sabtu': 'saturday',
    'minggu': 'sunday'
}


hari_list = list(hari_dict(keys()))
day_list = list(hari_dict(values()))
user_input = input("masukkan hari (INA/ENG): ")
if user_input in hari_list:
    day = day_list[hari_list.index(user_input)]
    print (f"bahasa inggris dari {user_input.upper()} adalah {day.upper()}")
elif user_input in day_list:
    hari = hari_list[day_list.index(user_input)]
    print (f"bahasa inggris dari {user_input.upper()} adalah {hari.upper()}")
else:
    print("invalid input")


# dicthari = {
#     'senin': 'monday',
#     'selasa': 'tuesday',
#     'rabu': 'wednesday',
#     'kamis': 'thursday',
#     'jumat': 'friday',
#     'sabtu': 'saturday',
#     'minggu': 'sunday'
#     }
# hari = input('Masukkan hari (ENG/INA): ').lower()
# ina = list(dicthari.keys()) # [senin, selasa, rabu, kamis, jumat, sabtu, minggu]
# eng = list(dicthari.values()) # [monday, tuesday, wednesday, thursday, friday, saturday, sunday]
# if hari in ina:
#     print(f'Bahasa Inggris dari {hari.capitalize()} adalah {dicthari[hari].capitalize()}')
# elif hari in eng:
# #                                                                 ina[4].capitalize()
#     print(f'Bahasa Indonesia dari {hari.capitalize()} adalah {ina[eng.index(hari)].capitalize()}')
# else: print(f'Kata yang Anda masukkan bukan nama hari.')

# print(dicthari.items())

# day = input("masukkan hari dalam bahasa ing/indo: ").lower()
# if day =="senin" or day =="selasa" or day =="rabu" or day =="kamis"or day =="jumat"or day =="sabtu" or day =="minggu":
#     hari = {"senin":"monday ","selasa":"tuesday ","rabu":"wednesday ","kamis":"thursday ","jumat":"friday ","sabtu":"saturday","minggu":"sunday"}
#     print(f"bahasa inggris hari '{day}' adalah: "+hari[day])
# elif day =="monday" or day =="tuesday" or day =="wednesday" or day =="thursday"or day =="friday"or day =="saturday" or day =="sunday":
#     hari1 = {"monday":"senin ","tuesday":"selasa ","wednesday":"rabu ","thursday":"kamis","friday":"jumat","saturday":"sabtu","sunday":"minggu"}
#     print(f"bahasa indonesia hari '{day}' adalah: "+hari1[day])
# else:
#     print("hari yang anda masukkan salah")

