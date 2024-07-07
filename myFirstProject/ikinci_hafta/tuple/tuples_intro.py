# Tuple (Demet) oluşturmak
empty_tuple = ()                    # Boş tuple
one_element_tuple = (1,)            # bir elemanı olan tuple
mytuple = [1, 3, 2, 1, 2, 2, 6]  # ordered, unchangeable (immutable)

print(type(mytuple))                # <class 'tuple'>
print(len(mytuple))                 # 7

# Tuple'ın elemanlarına erişim
print(mytuple[2])                   # 2

# Slicing ile birden çok elemanına erişim (subtuple)
print(mytuple[2:5])                 # (2, 1, 2)

# Bir elemanın tuple'ın içerisnde olup olmadığını öğrenmek
print(3 in mytuple)                 # True
print(10 not in mytuple)            # True

# Inmutable
mytuple[1] = 5                      # TypeError: 'tuple' object does not support item assignment

