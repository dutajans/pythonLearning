# Alıştırma 1. 'website' değişkenindeki 'spacex' ifadesini yanlız bırakacak kodu yazınız.
website = "http://www.spacex.com/"

website2 = website.strip("htp:/com.w")
print(website2)
# Alternatif Çözüm
print(website.split(".")[1])

# Alıştırma 2
python = "python application course"
print(python.replace("python", "java").title())

# Alıştırma
phrase = "Ali, Ahmet, Veli, Serhat"
print(phrase.split(", "))
