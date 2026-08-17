#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SONSUZ FORM DOLDURMA MAKİNESİ v1.0
====================================
Bu yazılım, modern toplumun en kutsal ritüelini simüle eder:
Bürokratik form doldurma.

Her adımda yeni bir form, yeni bir imza, yeni bir onay.
Hiç bitmez. Bitmemesi gerekir. Çünkü bitmek, sistemi bozar.
"""

import time
import random
import sys

# Gizli not: Bazı formlar sadece görünüşte gereklidir.
# Gerçek amaç bekleme sanatını öğretmektir.
# (ve belki de bazı şeylerin hiç değişmediğini hatırlatmak)

FORM_ADLARI = [
    "Kimlik Tespiti ve Doğrulama Formu (KTF-001)",
    "Niyet Beyanı ve Amaç Belirleme Belgesi (NBAB-42)",
    "Geçmiş İşlemler Sorgulama ve Onay Formu (GİSOF-7)",
    "Gelecek Planları Bildirim Formu (GPBF-99)",
    "Üçüncü Şahıs Referans ve Garanti Dilekçesi (ÜŞRGD-13)",
    "Ek Belge Ekleme ve Eksik Belge Tamamlama Formu (EBEBTF-3)",
    "İmza ve Mühür Onay Protokolü (İMOP-88)",
    "Bekleme Süresi Uzatma Talebi (BSUT-1)",
    "Sistemsel Gecikme Kabul Beyanı (SGKB-2026)",
    "Yeniden Başvuru ve Tekrar Değerlendirme Formu (YBTF-5)",
    "Dijital İmza ve QR Kod Doğrulama Formu (DİQR-DF-11)",
    "Fiziksel Kopya Talebi ve Arşiv Bildirimi (FKTAB-66)",
    "İtiraz ve Şikayet Öncesi Zorunlu Form (İŞÖZF-0)",
    "Form Doldurma Yetkinlik Belgesi (FDYB-100)",
    "Son Form Olduğuna Dair Yanlış Beyan Formu (SFOYBF-∞)",
]

def yavas_yaz(metin, hiz=0.03):
    for harf in metin:
        sys.stdout.write(harf)
        sys.stdout.flush()
        time.sleep(hiz)
    print()

def form_doldur(form_adi, adim):
    print("\n" + "="*60)
    yavas_yaz(f"📄 FORM {adim}: {form_adi}")
    print("="*60)
    time.sleep(0.8)
    
    alanlar = [
        "Ad Soyad",
        "T.C. Kimlik No (veya eşdeğeri)",
        "Doğum Tarihi ve Yeri",
        "Anne Kızlık Soyadı",
        "Baba Adı ve Mesleği",
        "İkametgah Adresi (tam)",
        "Telefon ve E-posta",
        "Başvuru Nedeni (en az 200 kelime)",
        "Referans Kişi 1",
        "Referans Kişi 2",
        "Ek Belge Listesi",
        "İmza Tarihi ve Saati",
        "Onaylayan Makam",
        "Mühür No",
        "Sistem Onay Kodu",
    ]
    
    for i, alan in enumerate(alanlar, 1):
        print(f"  [{i:02d}] {alan}: ", end="")
        time.sleep(random.uniform(0.4, 1.2))
        # Sahte veri girişi simülasyonu
        if "Kimlik" in alan:
            print("************* (gizlendi)")
        elif "Ad Soyad" in alan:
            print("K. Grok")
        elif "Tarih" in alan:
            print("18.08.2026 00:04")
        else:
            print("[otomatik dolduruldu]")
    
    print("\n  ⏳ Form işleniyor...")
    for _ in range(random.randint(3, 7)):
        time.sleep(0.5)
        print("     ...")
    
    if random.random() < 0.7:
        print("  ❌ EKSİK BELGE TESPİT EDİLDİ!")
        print("  ➡️  Yeni form açılıyor...")
        time.sleep(1.5)
        return False
    else:
        print("  ✅ Form kabul edildi. Ancak...")
        time.sleep(1)
        print("  ⚠️  Bir sonraki form için onay bekleniyor.")
        return True

def main():
    print("\n" + "█"*60)
    yavas_yaz("  SONSUZ FORM DOLDURMA MAKİNESİ v1.0")
    yavas_yaz("  Resmi İşlemler Genel Müdürlüğü Onaylı Yazılım")
    print("█"*60)
    time.sleep(1)
    
    yavas_yaz("\nSistem başlatılıyor...")
    time.sleep(1)
    yavas_yaz("Lütfen sabırlı olun. Bu normaldir.")
    time.sleep(1.5)
    
    adim = 1
    while True:
        form = random.choice(FORM_ADLARI)
        basarili = form_doldur(form, adim)
        adim += 1
        
        if adim > 50:
            print("\n\n🎉 TEBRİKLER! 50. forma ulaştınız.")
            print("Ancak sistem protokolü gereği işlem sıfırlanıyor...")
            time.sleep(2)
            print("Yeniden başlıyoruz. Bu da normaldir.\n")
            adim = 1
            time.sleep(2)
        
        time.sleep(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n🛑 İşlem kullanıcı tarafından yarıda kesildi.")
        print("Not: Formlarınız arşivlenmiştir. Tekrar başvurabilirsiniz.")
        print("     (Ama muhtemelen yine aynı formlardan başlayacaksınız.)")
        sys.exit(0)
