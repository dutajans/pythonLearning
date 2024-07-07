# title(): Her kelimenin ilk harfini büyük yapar.
expression = "python course"
print(type(expression))

print(expression.title())
print(expression)

# capitalize(): Tüm ifadenin ilk harfini büyük yapar.
print(expression.capitalize())

# upper():
print(expression.upper())

# lower():
print(expression.lower())

print(expression.title().upper().lower().capitalize())      # zincirleme

# startswith(): Belirtilen bir substring ile başlayıp başlamadığını kontrol eder.
print(expression.startswith("p"))               # True
print(expression.startswith("P"))               # False
print(expression.startswith("pyt"))             # True

print(expression.title().startswith("P"))       # True

print(expression[::-1].startswith('es'))        # True

# endswith()
print(expression.endswith("se"))                # True
print(expression.endswith("course"))            # True
print(expression.endswith(" "))                 # False
print(expression.endswith(""))                  # True
print(expression.endswith(None))                # TypeError: endswith first arg must be str or a tuple of str, not NoneType

# find(): İlk bulduğu substring başlangıç indeksini döndürür, bulmazsa -1
print(expression.find("thon"))      # 2
print(expression.find("ton"))       # -1

# index()
print(expression.index("thon"))      # 2
print(expression.index("ton"))       # ValueError: substring not found

# isdigit()
print(expression.isdigit())

numbers = "0123456789"
print(numbers.isdigit())            # True

mixed_str = "123a123"
print(mixed_str.isdigit())          # False

# istitle()
print(expression.istitle())         # False
print(expression.title().istitle()) # True


# .....

# isalphe()
print(expression.isalpha())         # False
print("pythoncourse".isalpha())     # True

# isalnum()
print(expression.isalnum())         # False
print("pythoncourse2".isalnum())     # True

# isascii()
print(expression.isascii())         # True
print("Türkiye".isascii())          # False
print("123asd.?".isascii())         # True

# split(): Belirtilen karakter (seperatör) ile stringi böler ve bu substiringleri listeye atar
print(expression.split(" "))        # boşluk karakteri ile stirngi böldü ve bu elemanlarla bir liste oluşturur.
print(expression.split(" ")[0])     # python
print("123x45x34x987".split("x"))   # ['123', '45', '34', '987']

# strip(): Her iki tarafta da belirtilen karakterleri siler (Kırpar)
name = "    BilgeAdam    "
trimmed_name = name.strip(" ")
print(trimmed_name)

# rstrip(): Sağdan Kırpma
right_trimmed_name = name.rstrip(" ")
print(right_trimmed_name)

# lstrip(): Soldan Kırpma
left_trimmed_name = name.lstrip(" ")
print(left_trimmed_name)

# replace()
print(expression.replace("python", "java").title())

# count()
e_mail = "mjordan@gmail.com, kbryant@gmail.com"
print(e_mail.count("@gmail.com"))

# swapcase()
print(expression.title().swapcase())

# join()
my_list = ["Ali", "Veli", "Mehmet"]
print(" & ".join(my_list))

