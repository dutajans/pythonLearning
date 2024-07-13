# Dictionary (Sözlük) oluşturmak
# mydict = {"key1":"value1", "key2":"value2"}

mydict = {"Ankara": 25, "İstanbul": 23, "Agri": 20}

# Eğer dictionary olmasaydı aşağıdaki gibi veriyi saklamam gerekirdi.
mytenp = [25, 23, 20]
mycity = ["Ankara", "İstanbul", "Agri"]

for i in range(len(mycity)):
    print(f"Şehir: {mycity[i]}, Sıcaklık: {mytenp[i]}")

# Mydict ile ekrana yazdırma type ve içindeki toplam veri değer sayısı
print(mydict, type(mydict), len((mydict)))

# Boş sözlük oluşturma
empty_dict = {}
empty_dict2 = dict()

# sözlükten Değer (Value) Çağırmak
print(mydict)
print(mydict["İstanbul"])

print(mydict["Istanbul"])   # KeyError: 'Istanbul'

mydict.get("İstanbul")
mydict.get("Istanbul")      # None Döndürür

# Örnek
fruits = {"apple": 5, "banana": 3, "pear": 2}
print(fruits)

fruits = dict(apple=5, banana=3, pear=2)
print(fruits)

total_weight = fruits["apple"] + fruits["banana"] + fruits["pear"]
print("Total weight:", total_weight)

# Örnek
player = {
    "name": "Kobe Bryant",
    "height": 1.90,
    "weight": 96,
    "active": False,
    "number": (8,24),
    "points": {
        "2014-15": 22.3,
        "2015-16": 17.6
    }
}

print(player, len(player))

print(player["name"])
print(f"Name of the player {player['name']}\nActive Status: {player['active']}")

a,b = player["number"]

print(f"Season 2014-15 Points: {player['points']['2014-15']}")

# Sözlüğe Eleman Ekleme
player["country"] = "USA"

# Elemanın Değerini Değiştirmek
player["height"] = int(player["height"] * 100)

# Sözlükten Eleman (Item) Silmek
del player["country"]

# örnek
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

# users sözlüğünün uzunluğu nedir?
print("Sözlüğün Uzunluğu :", len(users))
# burakt isimli kullanıcının yaş bilgisi nedir?
print(users['burakt']['yas'])
# ahmetc isimli kullanıcının adres bilgiini büyük harflerle yazdırın
print(users['ahmetc']['adres'].upper())

