# -*- coding: utf-8 -*-

import json
import re
import os

# Başlangıç ve hedef dili seçtiğimiz fonksiyon
def dil_secme(kelime, kelime_listesi,mesaj_tipi):
    mesaj_tipi.capitalize()
    kelime = tr_lower(kelime)
    if kelime.startswith("i"):
        kelime = "İ" + kelime[1:]
    kelime = kelime.capitalize()
    for dil in (kelime_listesi):
        if kelime == dil:
            print(f"{mesaj_tipi} seçildi.")
            return True
     
    print(f"{mesaj_tipi} Mevcut değil.Lütfen geçerli bir dil giriniz.")
    return False

#Seçilen kelimeyi hedef dile çeviren fonksiyon
def cevir(baslangic_dili, hedef_dil, secilen_kelime, kelime_listesi):
    secilen_kelime = tr_lower(secilen_kelime)

    if baslangic_dili.startswith("i"):
        baslangic_dili = "İ" + baslangic_dili[1:]
    baslangic_dili = baslangic_dili.capitalize()

    if hedef_dil.startswith("i"):
        hedef_dil = "İ" + hedef_dil[1:]
    hedef_dil = hedef_dil.capitalize()

    for sozluk in (kelime_listesi):

        if sozluk.get(baslangic_dili) == secilen_kelime: #elemanı sözlük içinden (türkçe/ingilizce/fransızca gruplarının hepsi birer sözlük) almak için kullandık
            return sozluk.get(hedef_dil)
    return "hata"  # Eşleşme bulunmazsa 

#Küçük harfe çevirme fonksiyonu
def tr_lower(x):
    text = x
    text = re.sub(r"İ", "i", text)
    text = re.sub(r"I", "ı", text)
    text = re.sub(r"Ç", "ç", text)
    text = re.sub(r"Ş", "ş", text)
    text = re.sub(r"Ü", "ü", text)
    text = re.sub(r"Ğ", "ğ", text)
    text = text.lower() 
    return text

file_path =  os.path.join(os.path.abspath(os.path.dirname(__file__)), 'config.json')
with open(file_path, encoding='utf-8') as f:
    diller = json.load(f)
# encoding türkçe karakterleri doğru bastırmak için yazıldı
# f file anlamında
file_path =  os.path.join(os.path.abspath(os.path.dirname(__file__)), 'words.json')
with open(file_path, encoding='utf-8') as f:
    kelimeler = json.load(f)

print("Sözlüğe hoş geldiniz!")

for dil in (diller["languages"]):
    print(dil)

while True:
    while True:
        x= input("Başlangıç dilini seçiniz:")
    
        if dil_secme(x,diller["languages"], "Başlangıç dili"): 
            break  
    while True:
        y= input("Hedef dili seçiniz:")
        if dil_secme(y,diller["languages"], "Hedef dil") :
            break
    if x==y:
        print("Başlangıç dili ile hedef dil aynı olamaz.Lütfen tekrar seçim yapınız.")
    else :
        print("Başlangıç dili ve hedef dil seçildi.")
        break

while True:
    a = input("Çevirisinin yapılmasını istediğiniz kelimeyi yazınız:")
    a = tr_lower(a)
    sonuc= cevir(x, y, a, kelimeler)
    if sonuc == "hata":
        print("Kelime bulunamadı.Lütfen tekrar deneyin.")
    else:
        print(sonuc.capitalize())
    while True:
        cevap = input("Çeviriye devam etmek istiyor musunuz?(evet/hayır):")
        cevap = tr_lower(cevap)
        if cevap == "evet" :
            break
        elif cevap== "hayır" :
            print("Sözlüğü kullandığınız için teşekkür ederiz.")
            exit()
        else :
            print("Lütfen geçerli bir cevap giriniz.")

        


    








    
    



