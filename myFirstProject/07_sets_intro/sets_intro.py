# Set oluşturmak
myset = {1, 2, 3, 4, 5, 6, 7, 8}
print(myset, len(myset))

set1 = set()
print(set1, len(set1))

mylist = [2, 4, 2, 2, 2, 3, 3, 6, 6, 6, 9, 4, 5, 4]
myset = set(mylist)         # conversion from list to set
print(myset, len(myset))

# in operatörü
print(5 in myset)   # True

######### SET METHODS #########

# add(): Eleman ekle
myset.add(7)
print(myset)

# update(): Birden fazla Eleman eklemek
myset.update([5, 6, 7, 8, 9])
print(myset, len(myset))

myset.update({5, 7, 8, 10})
print(myset, len(myset))

# discord(): Elaman Silmek
myset.difference(8)
print(myset, len(myset))

myset.remove(11)    # KeyError: 11
myset.discard(11)

# Küme İşlemleri (union, intersection, difference)
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# union(): Setlerin birleşimi
union_set = set1.union(set2)
print(union_set)
print(set1)
print(set2)

# intersection(): Setlerin kesişimi
intersect_set = set2.intersection(set1)
print(intersect_set)

# difference(): Setlerin Farkı
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
set1.difference(set2)
set2.difference(set1)

# issubset()
set3 = {1, 2, 3, 4}
set4 = {2, 3}
set5 = {3, 4, 5}

