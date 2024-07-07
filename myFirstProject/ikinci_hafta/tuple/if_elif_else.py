# Conditional Statements (Koşullu İfadeler)
# If Statement

if True:
    print("This expression is True")        # Bir girinti (indentation)

if False:
    print("This expression is False")       # Bu kod erişilemez

age = float(input("What is your age: "))

if age >= 18:
    print("You're an adult")
else:
    print("You're not an adult.")


age = float(input("What is your age: "))

if age >= 18:
    print("You're an adult")
elif 0 <= age < 18:
    print("You're not an adult.")
else:
    print("Invalid age.")

mylist = [""]

if mylist:
    print("A")
else:
    print("B")

