users = {
    'ahmetc': {
        'yas': 35,
        'rol': ['user'],
        'email': 'ahmet@bilgeadam.com',
        'adres': 'İstanbul',
        'telefon': '5304616161'
    },
    'burakt': {
        'yas': 33,
        'rol': ['admin', 'user'],
        'email': 'burakt@bilgeadam.com',
        'adres': 'Ankara',
        'telefon': '5056060606'
    }
}

# keys(): Sözlüğün anahtarlarına Erişmek
print(users.keys())                                     # dict_keys(['ahmetc', 'burakt'])
users_keys = users.keys()
print(users_keys, type(users_keys), len(users_keys))    # dict_keys(['ahmetc', 'burakt']) <class 'dict_keys'> 2

for user in users_keys:
    print(user)

# values(): Sözlüğün değerlerine erişmek
users_values = users.values()
print(users_values, type(users_values), len(users_values))

for user in users_values:
    print(user)

ahmetc_values = users['ahmetc'].values()
print(ahmetc_values, len(ahmetc_values))

# itens(): Sözlüğün elemanlarına erişmek
users_items = user.items()
print(users_items)

# Örnek
mytech = {
    "Python": 1991,
    "Java": 1995,
    "Julia": 2012,
    "Mojo": 2023
}

print(mytech.keys())
print(mytech.values())
print(mytech.items())

for p, y in mytech.items():
    print(f"Language: {p}, Year: {y}")

# get() Method
print(mytech["Python"])
print(mytech.get("Python"))
print(mytech.get("Go"))

# copy() method
copied_mytech = mytech.copy()
print(copied_mytech)

# clear() method
copied_mytech.clear()
print(copied_mytech)

# pop() method: Belirtilen anahtar ile elemanı siliyor ve çıkarılan değeri döndürüyor.
mytech.pop("Julia")
print(mytech)

# popitem(): Son elemanı tuple olarak döndürür ve sözlükten çıkartır.
mytech.popitem()
print(mytech)

# update(): Sona tuple olarak veri ekliyor
# fromkeys():

# w3resource.com python exircises için kullan

dic1 = {1:10, 2:20}
dic2 = {3:10, 4:40}
dic3 = {5:50, 6:60}

dic1.update(dic2)
dic1.update(dic3)

print(mytech)
if "C++" in mytech:
    print("In this dict")
else:
    print("C++" in mytech.keys())