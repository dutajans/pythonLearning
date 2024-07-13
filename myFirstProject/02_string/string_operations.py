# String Length
my_string = "Hello World!"
print("Stringin Uzunluğu: ", len(my_string))

print(my_string.__len__())  # special method

####################### String Concatenation (Birleştirme) #######################

first_string = "Hello"
second_string = "World!"

# String addition
sentence = first_string + ", " + second_string

# % Operator
sentence = "%s, %s" % (first_string, second_string)
print(sentence)

# .format() string Method
sentence = "{}, {}".format(first_string, second_string)
print(sentence)

a = "BilgeAdama"
b = "Kursu"
c = "Python"

sentence = "{0} {2} {1}". format( a, b, c)
print(sentence)

# f-string
sentence = (f"{first_string}, {second_string}")
print(sentence)

# String Multiplication
letter = "7"
print(letter * 3)

print(int(letter * 3) + 3)

####################### String Indexing and Slicing #######################

# String Indexing
word = "BilgeAdam"
       #012345678
       #987654321   negatif
print(len(word))

print(word[0])  # ilk karakter
print(word[-9]) # son karakter

print(word[5])  # A

print(word[9])  # IndexError: string index out of range
print(word[-10])  # IndexError: string index out of range

print(word[-len(word)])

# String Slicing
word = "BilgeAdam"

print(word[0:5])   # start:stop start indeksi dahil (inculuded) stop indexi hariç (excluded)
print(word[5:8])
print(word[5:])
print(word[5:10])  # hata vermez

print(word[-3:-1])
print(word[-1:-5])

print(word[2:7:2]) # start:stop:step - başlangıç indexi, bitiş indexi ve adım indexi

print(word[-1:-5:-1]) # madA
print(word[-1:4:-1])  # madA

word = "BilgeAdam"
print(word[2::3])   # lAm
print(word[:6:2])   # Ble

# in, not, in Operators
word = "BilgeAdam"
print("B" in word)      # True
print("b" in word)      # False
print("Ada" in word)    # True

print("z" not in word)  # True

# Escape Characters
txt = "Hello\nWorld!"
print(txt)