##### Çarşamba günü işledik #####
# str alıyoruz
# s harfleri saydır
import time

kelime = input("Lütfen bir kelime giriniz: ")
sayac = 0

if kelime.isdigit():
    print("Girdiğiniz değer bir kelime değildir. Lütfen kelime giriniz.")
else:
    for harf in kelime:
        if harf in "aeiouıöü":
            sayac += 1
    print(f"Kelimenizdeki sesli harf sayısı: {sayac}")
##### Çarşamba günü işledik #####

# Kullanıcıdan sınav notunu alıp (100 üzerinden isteyen)
# Derse ait harfi çıktı veren bir if-elif-else od bloğu yazınız:
# >= 90: A
# >= 80: b
# >= 70: C
# >= 60: D
# <  60: f
import time

try:
    score = float(input("Ders Notunuzu (0-100 arasında) giriniz: "))
    print("Notunuz Hesaplanıyor...")
    time.sleep(2)

    if 0 <= score <= 100:
        if score >= 90:
            print("Ders Notunuz: A")
        elif score >= 80:
            print("Ders Notunuz: B")
        elif score >= 70:
            print("Ders Notunuz: C")
        elif score >= 60:
            print("Ders Notunuz: D")
        else:
            print("Ders Notunuz: F")
        print("Program Sonlandı.")
    else:
        print("Lütfen geçerli bir not giriniz! (0-100 arasında)")
except ValueError:
    print("Bir Sayı değeri girmediniz!")