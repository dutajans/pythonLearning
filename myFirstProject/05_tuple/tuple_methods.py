mytuple = (1, 2, 3, 1, 2, 2, 6, 4)

mytuple.count(2)    # Verilen değerin tekrar etme sayınızı verir
mytuple.index(2)    # Verilen değerin index numarasını verir.

mytuple.index(2, 3)             # 4
mytuple.index(6,1,5)     # ValueError: tuple.index(x): x not in tuple

# Error handling
try:
    mytuple.index(6,1,5)
except:
    print("Girdiğiniz değer tuple içerisinde bu aralıkta değildir.")

# Tuple Birleştirme
first_tuple = (1, 3)
second_tuple = (2, 4)

third_tuple = first_tuple + second_tuple
print(third_tuple)

fourth_tuple = [first_tuple] + [second_tuple]
print(fourth_tuple)

# Tuple Elemanlarını değişkenlere atama
team1 = ("Fenerbahçe", "Türkiye")
team, country = team1
team, country, points = team1       # ValueError: not enough values to unpack (expected 3, got 2)
print(team)
print(country)