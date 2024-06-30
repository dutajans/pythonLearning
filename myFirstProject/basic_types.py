# Python'da Temel Veri Tipleri
# str (string) metin                --> "Car", "tire"
# int (integer) tam sayı            --> 5, 6, 7, 100000, -5
# float (float) ondalıklı sayı      --> 5.2, 7.89, 0.0
# bool (boolean) mantık ifadesi     --> True, False
# complex (complex) karmaşık sayı   --> 1j
# NoneType(None)                    --> None

####################### STRINGS (Metinler) #######################
mystr = "This is a string."
print(mystr)

# Bir değişkenin tipini incelemek
print(type(mystr))              # <class 'str'>

# Metinleri Farklı Satırlarda Yazma
mystr = ("This is "
         "a string.")
print(mystr)

# Triple Quates - Her satırı aynı şekilde alt alta yazar
mystr = """BilgeAdam
Python
Course"""
print(mystr)

mystr2 = "BilgeAdam\nPython\nCourse"
print(mystr2)

mystr3 = "BilgeAdam\tPython\tCourse"
print(mystr3)

####################### INTEGERS & FLOAT #######################

x = 5
print(type(x))                  # <class 'int'>

y = 5.0
print(type(y))                  # <class 'float'>

z = 2 + 1J
print(type(z))                  # <class 'complex'>

####################### BOOLEANS (MANTIKSAL) #######################
myboll = False
print(type(myboll))             # <class 'bool'>
print(myboll)

# VE (AND) İŞLEMLERİ
salim = True
yunus = True
deniz = True

print(salim and yunus)                              # True
print(not salim and deniz)                          # False
print(salim and deniz and not yunus)                # False
print(not salim and not deniz and not yunus)        # False
print(not(not salim and not deniz and not yunus))   # True

# VEYA (OR) İŞLEMLERİ
print(salim and yunus)                              # True or True = True
print(not salim or yunus)                           # False or True = True

####################### NONETYPE #######################
mynone = None
print(mynone)
print(type(mynone))                                 # <class 'NoneType'>

print(True and None)                                # None

print(True and bool(None))                          # False