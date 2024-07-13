# Ödev-2 (Veri Yapıları, if-elif-else)
# Son tarih: 14 Temmuz 2024 23:59
# Yönergeler
# Alıştırma 1: E-posta Adresi Format Kontrolü
# Açıklama: Kullanıcıdan bir e-posta adresi alın ve bu adresin geçerli bir format olup olmadığını
# kontrol edin. Geçerli bir e-posta adresi için aşağıdaki kuralları uygulayın:
# En az bir "@" işareti içermelidir.
# "@" işaretinden önce ve sonra en az bir karakter olmalıdır.
# Son kısım en az iki karakterden oluşan bir alan adı (örneğin ".com", ".net", ".org") içermelidir.
# Örnek Girdi: kullanici@example.com
# Örnek Çıktı: True
import time
soru = "Lütfen E-Posta Adresinizi Griniz! :"
eposta = input(soru)
gecerli_uzantilar = [".com", ".org", ".net", ".edu", ".gov", ".tr"]

try:
    print("E-Posta kontrolü yapılıyor.")
    time.sleep(2)
    if '@' not in eposta:
        print("Girdiğiniz veri geçerli bir e-posta adresi değil. '@' işareti eksik.")

    solkontrol, sagkontrol = eposta.split('@')

    if len(sagkontrol) == 0:
        print("Mail adresiniz hatalı, @ işaretinin sağ tarafı boş.\nLütfen mail adresinizi doğru giriniz!")
    if len(solkontrol) == 0:
        print("Mail adresiniz hatalı, @ işaretinin sol tarafı boş.\nLütfen mail adresinizi doğru giriniz!")

    domain = sagkontrol.split('.')[-1]
    uzanti = '.' + domain

    if uzanti not in gecerli_uzantilar:
        print(f"E-posta adresi geçerli bir uzantı ile bitmiyor. Geçerli uzantılar: {', '.join(gecerli_uzantilar)}")

    print("Girdiğiniz e-posta adresi geçerli ve uygun bir uzantı ile bitiyor.")
    print(f"Girdiğiniz Mail Adresi: {eposta}")
    print("E-Posta Uygundur.")
except:
    print(f"Lütfen E-Posta adresiniz doğru şekilde giriniz!\nÖrneğin: 'test@mail.com'\nHatalı Girilen Mail Adresi: {eposta}")


# Alıştırma 2: String İçindeki Harf Sayısını Bulma
# Açıklama: Kullanıcıdan bir cümle ve bir harf alın. Girilen cümle içinde, kullanıcının girdiği harfin kaç
# kez geçtiğini bulun ve ekrana yazdırın.
# Örnek Cümle: "Bu bir deneme cümlesidir."
# Örnek Harf: "e"
# Örnek Çıktı: "e" harfi 4 kez geçmektedir.

soru = "Lütfen Bir Cümle Griniz! :"
soru2 = "Lütfen tekrar eden harf bilgisi giriniz :"
cumle = input(soru)
harf = input(soru2)

sayilan_harf = cumle.count(harf)

print(f"Verilen Cümle: {cumle}\nAranacak harf: {harf}\n'{harf}' harfi {sayilan_harf} kez geçmektedir.")


# Alıştırma 3: Formula 1 Sıralama Simülasyonu
# Açıklama: Aşağıda verilen bilgilere göre, hangi pilotun yarışı kazandığını belirleyin ve sonucu yazdırın.
# Verilen Bilgiler: Pilotların isimleri ve süreleri bir liste içinde tuple olarak veriliyor.
# yariscilar = [("Lewis Hamilton", 312), ("Max Verstappen", 315)]
# Örnek Çıktı: Lewis Hamilton yarışı kazandı.

yariscilar = [("Lewis Hamilton", 312), ("Max Verstappen", 315)]
yarismaci, sure = yariscilar

kazanan = yariscilar[0]

for yarismaci in yariscilar:
    if yarismaci[1] < kazanan[1]:
        kazanan = yarismaci

print(f"{kazanan[0]} yarışı kazandı.")


# Alıştırma 4: NBA Skor Takibi
# Açıklama: Bir NBA maçında, iki takımın attığı" basket sayılarını içeren bir liste veriliyor.
# Kullanıcıdan iki takımın adını ve her çeyrek için attıkları sayıları içeren bir liste alın ve hangi takımın
# kazandığını ekrana yazdırın.
# Verilen Bilgiler: [("Lakers", [30, 25, 20, 25]), ("Celtics", [25, 30, 25, 20])]
# Örnek Çıktı: Lakers 100 - 100 Celtics. Maç berabere bitti.

#basket_sayilari = [("Lakers", [30, 25, 20, 25]), ("Celtics", [25, 30, 25, 20])]

import time
basket_takim_listesi = []
for i in range(2):
    takim_adi = input(f"Lütfen {i+1}. Takımın Adınızı Giriniz: ")

    gol_sayisi = []
    for g in range(4):
        gol = int(input(f"{takim_adi} takımın {g+1}. çeyrekteki gol sayısını giriniz: "))
        gol_sayisi.append(gol)

    basket_takim_listesi.append((takim_adi, gol_sayisi))

print("Maçın kazananı hesaplanıyor...")
time.sleep(2)

ilk_takim_toplam_gol = sum(basket_takim_listesi[0][1])
ikinci_takim_toplam_gol = sum(basket_takim_listesi[1][1])

if ilk_takim_toplam_gol > ikinci_takim_toplam_gol:
    print(f"{basket_takim_listesi[0][0]} {ilk_takim_toplam_gol} - {ikinci_takim_toplam_gol} {basket_takim_listesi[1][0]}. Maçın kazananı {ilk_takim_toplam_gol} Skor ile {basket_takim_listesi[0][0]}")
elif ilk_takim_toplam_gol < ikinci_takim_toplam_gol:
    print(f"{basket_takim_listesi[0][0]} {ilk_takim_toplam_gol} - {ikinci_takim_toplam_gol} {basket_takim_listesi[1][0]}. Maçın kazananı {ikinci_takim_toplam_gol} Skor ile {basket_takim_listesi[1][0]}")
else:
    print(f"{basket_takim_listesi[0][0]} {ilk_takim_toplam_gol} - {ikinci_takim_toplam_gol} {basket_takim_listesi[1][0]}. Maç berabere bitti")

print("Listede bulunan takım bilgileri yükleniyor...")
time.sleep(2)
for basket_takim in basket_takim_listesi:
    print(f"Takım: {basket_takim[0]}, Goller: {basket_takim[1]}")