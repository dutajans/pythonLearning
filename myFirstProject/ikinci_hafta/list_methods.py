#### range() ####
my_range = range(5)
print(my_range)

for i in range(10):
    print(i)

my_list = list(my_range)
print(my_list)

# range(start:stop)
my_range = range(5, 10)
print(list(my_range))

# range(start, stop, step)
my_range = range(5, 10, 2)
print(len(list(my_range)))

my_range = range(10, 5, -2)
print(list(my_range))

for i in range(100):
    print(i ** 2)

# append() Sonuna eleman ekler
my_list = list(range(5))
print(my_list)
my_list.append("5")
my_list.append("hello")

a = my_list.append(6)
print(a)        # None
print(my_list)

# extend(): Liste Uzatma
new_list = [6, 7, 8]
my_list.extend(new_list)
print(my_list)

my_list.extend(range(8,10))
my_list.extend("apple")
print(my_list)

# insert() Belirli bir index'e eleman ekleme
my_list.insert(3, "H")
print(my_list)

# remove() Eleman silme
my_list.remove("H")
print(my_list)

# pop() Eleman silme
my_list.pop(6)
print(my_list)

popped_item = my_list.pop()
print(f"Çıkarılan değer: {popped_item}\nListenin Yeni Hali: {my_list}")

# index(): Elemanın indeksini bulmak
my_list.index(3)
my_list.index(8)

# count(): Elemanın Tekrar Etme Sayısını Bulmak
my_list.count(8)
print(my_list)

# sort(): Liste Sıralama
my_list2 = [3, 5, 8, 1, 9, 2, 5, 1, 9]

# Küçükten Büyüğe doğru sırala ve yeni bir nesne oluştur.
my_list2_sorted = sorted(my_list2)
print(my_list2_sorted)
print(my_list2)

# Büyükten Küçüğe Doğru
sorted(my_list2, reverse=True)
print(my_list2)

# Küçükten büyüğe sırala ve bu sıralama kalıcı olsun
my_list2.sort()
print(my_list2)

# Büyükten Küçüğe
my_list2.sort(reverse=True)
print(my_list2)

str_list = ["aba", "aae", "acb", "bca", "aaa", "ayt", "eft", "eyt", "oks"]
str_list.sort()
print(str_list)

# reverse(): Listeyi terse çevirme
my_list3 = [3, 5, 8, 1, 9, 2, 5, 1, 9]
my_list3.reverse()
print(my_list3)

# copy(): Liste kopyalama
a = [1, 2]
print(a, id(a))

b = a
print(b, id(b))

b[0] = 6
print("b", b)

b[0] = 6
print("b: ", b)
print("a: ", a)

c = a.copy()
print(c, id(c))

c[0] = 9
print(a, id(a))
print(c, id(c))