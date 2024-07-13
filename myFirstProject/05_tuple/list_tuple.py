mylist = [75, 87, 64]
mytuple = (75, 87, 65)

print(mylist[1])
print(mytuple[1])

mylist[1] = 90
print(mylist[1])

mytuple[1] = 90 # TypeError: 'tuple' object does not support item assignment

mylist.reverse()

mytuple.count(75)
mytuple.index(75)

mylist.pop()

type(mylist.pop())


##### Tuple unpacing
tuple1 = ("Fenerbahçe", 102)

# bu mantıksız ama çalışır
# team = tuple1[0]
# points = tuple1[1]

# mantıklı olan bu
team, points = tuple1

team, points, goal = tuple1 # ValueError: not enough values to unpack (expected 3, got 2)
print(len(tuple1)) # 2
team, points = tuple1 # bu olması gerekiyor

# iç içe tuple'lar

nested_tuple = (1, 2, (3, 4, (5, 6, (7,))))
nested_tuple[2][2][2][0]

# list of tuples (tupleların listesi)
turnuva = [
    ("Galatasaray", "Türkiye"),
    ("Slavia Prag", "Cek"),
    ("Manu", "England"),
    ("Arsenal", "England"),
]

print(turnuva)