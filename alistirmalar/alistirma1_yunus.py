# Alıştırma.Vücut Kitle İndeksi(BMI) Hesaplayıcı
# Kullanıcıdan boyunu(metre cinsinden) ve kilosunu(kilogram cinsinden) alacak bir Python programı yazın.
# Program, bu değerleri kullanarak vücut kitle indeksini hesaplamalı ve sonucu yazdırmalıdır.
# (BMI hesaplama formülü: kilo / (boy ^ 2))
#
# Çıktı Örneği:
# Boyunuzu metre cinsinden giriniz: 1.75
# Kilonuzu kilogram cinsinden giriniz: 68
# Vücut Kitle İndeksiniz(BMI): 22.2

boy_metin = "Lütfen Boy Değerinizi Metre Cinsinden Griniz: "
kilo_metin = "Lütfen Kilo Değerinizi Kilogram Cinsinden Griniz: "

boy = float(input(boy_metin))
kilo = input(kilo_metin)
bmi = float(kilo)/(boy*boy)
print(f"Boy (Metre Cinsinden) : {boy}")
print(f"Kilo (Kilogram Cinsinden) : {kilo}")
print(f"Vücut Kitle İndeksiniz(BMI) : {bmi}")

