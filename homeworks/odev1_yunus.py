# Ödev-1 (Kullanıcı Girişi, Basit Hesaplamalar, Çıktı)
# Son tarih: 7 Temmuz 2024 23:59
# Yönergeler
# Alıştırma 1. Sıcaklık Dönüştürücü (Celsius'tan Fahrenheit'a)
# Kullanıcıdan Celsius sıcaklık değerini (ondalık sayı olabilir) girmesini isteyen, girilen değeri Fahrenheit dereceye dönüştüren ve sonucu yazdıran kısa bir Python programı yazın.
#
# Çıktı Örneği:
# Celsius sıcaklık değerini giriniz: 25
# Fahrenheit: 77.0 °F
veri = "Lütfen Fahrenheit'a Dönüştürmek İstediğiniz Celsius Sıcaklık Değerini Giriniz: "
donusturulecek_deger = input(veri);
donusturulecek_deger2 = float(donusturulecek_deger)

print(f"Girilen Celsius sıcaklık değeri: {donusturulecek_deger}")
print(f"Dönüştürülen Fahrenheit sıcaklık değeri: {(donusturulecek_deger2*1.8)+32} °F")


# Alıştırma 2. Mesafe Dönüştürücü (Kilometreden Mile)
# Kullanıcıdan kilometre cinsinden bir mesafe (ondalık bir sayı olabilir) girmesini isteyen,
# girilen mesafeyi mile çeviren ve sonucu yazdıran kısa bir Python programı yazın.
#
# Çıktı Örneği:
# Kilometre cinsinden bir mesafe giriniz: 100
# Mil: 62.1371

veri = "Lütfen Mil'e Dönüştürmek İstediğiniz Kilometre Değerini Giriniz: "
donusturulecek_deger = input(veri);
donusturulecek_deger2 = float(donusturulecek_deger)

print(f"Girilen Kilometre cinsinden mesafe değeri: {donusturulecek_deger}")
print(f"Dönüştürülen Mil cinsinden mesafe değeri: {donusturulecek_deger2*0.62137}")


# Alıştırma 3. Üçgen Alan Hesaplayıcı
# Kullanıcıdan bir üçgenin taban ve yüksekliğini (ondalık sayı olabilir) alacak bir program yazın.
# Program, bu değerleri kullanarak üçgenin alanını hesaplamalı ve sonucu yazdırmalıdır.
# (Üçgenin alanı hesaplama formülü: (taban x yükseklik) / 2)
#
# Çıktı Örneği:
# Üçgenin tabanını giriniz: 6
# Üçgenin yüksekliğini giriniz: 4
# Üçgenin alanı: 12.0

taban_veri = "Lütfen Üçgenin Taban Değerini Giriniz: "
yukseklik_veri = "Lütfen Üçgenin Yükseklik Değerini Giriniz: "

donusturulecek_taban_deger = input(taban_veri);
donusturulecek_yukseklik_deger = input(yukseklik_veri);
donusturulecek_taban_deger2 = float(donusturulecek_taban_deger)
donusturulecek_yukseklik_deger2 = float(donusturulecek_yukseklik_deger)

print(f"Girilen Üçgenin Taban Değeri: {donusturulecek_taban_deger}")
print(f"Girilen Üçgenin Yükseklik Değeri: {donusturulecek_yukseklik_deger}")
print(f"Hesaplanan Üçgenin Alan Değeri: {(donusturulecek_taban_deger2*donusturulecek_yukseklik_deger2)/2}")


# Alıştırma 4. Ortalama Sıcaklık Hesaplayıcı
# Kullanıcıdan bir şehir ve bu şehirde ölçülen bir günün en yüksek ve en düşük sıcaklıklarını
# (ondalık sayı olarak) alacak bir Python programı yazın. Program bu bilgileri kullanarak o gün
# için ortalama sıcaklığı hesaplamalı ve şu formatta ekrana yazdırmalıdır:
#
# Çıktı Örneği:
# Şehir: Ankara
# En yüksek sıcaklık: 28.5 °C
# En düşük sıcaklık: 13.2 °C
# Ortalama sıcaklık: 20.85 °C

sehir_veri = "Lütfen Bir Şehir Giriniz: "
sehir = input(sehir_veri);
en_yuksek_sicaklik_veri = f"Lütfen {sehir} için Günün En Yüksek Sıcaklık Değerini Giriniz: "
en_dusuk_sicaklik_veri = f"Lütfen {sehir} için Günün En Düşük Sıcaklık Değerini Giriniz: "
yulsek_sicaklik_deger = float(input(en_yuksek_sicaklik_veri));
dusuk_sicaklik_deger = float(input(en_dusuk_sicaklik_veri));

print(f"Şehir: {sehir}")
print(f"Girilen En Yüksek Sıcaklık Değeri: {yulsek_sicaklik_deger} °C")
print(f"Girilen En Düşük Sıcaklık Değeri: {dusuk_sicaklik_deger} °C")
print(f"Hesaplanan Üçgenin Alan Değeri: {(yulsek_sicaklik_deger+dusuk_sicaklik_deger)/2} °C")




# Kodlarınızı uygun formatta yazarak ödev1_adınız.py isimli Python dosyasına kaydediniz.