# Kullanıcıdan daire yarıçapı (r) alan, daire alanı ve daire çevresini hesaplayıp
# ekrana çıktı veren bir program yazınız!
# Yarıçap uzunluğu ile
# çevreyi hesaplamak için 2 x π x r (YARIÇAP) formülü,
# çap uzunluğu ile çevreyi
# hesaplamak için π x R (ÇAP) formülü kullanılır.
import math
import time

# Kullanıcıdan alınan girdiler
r = float(input("Lütfen Daire yarıçapını giriniz: "));

# Hesaplamalar
print("Dairenin alanı hesaplanıyor...")
time.sleep(2)
alan = math.pi * r ** 2
# Kullanıcıya gösterilen Çıktı
print(f"Hesaplanan Dairenin Alanı: {round(alan, 2)} cm2")

print("Dairenin çevresi hesaplanıyor...")
time.sleep(2)
cevre = 2 * math.pi * r
# Kullanıcıya gösterilen Çıktı
print("Hesaplanan Dairenin Çevre Değeri:", round(cevre, 2), "cm")

