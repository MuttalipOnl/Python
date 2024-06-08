import time
import os

# Kullanıcı veritabanı
users = {}

# Hesap veritabanı
accounts = {}

# Global kulanici_adi
userss = None


# Terminal Penceresini Temizleyen fonksiyon
def clear():
    """
        Bu fonksiyon terminal penceresini ilk haline getirir.
    """
    if os.name == 'nt':
        _ = os.system('cls')


# Verileri metin dosyasından okuma
def veri_okuma():
    try:
        with open("user_data.txt", "r", encoding="utf-8") as file:
            for line in file:
                kullanici_adi, sifre, bakiye = line.strip().split(",")
                users[kullanici_adi] = sifre
                accounts[kullanici_adi] = float(bakiye)
    except FileNotFoundError:
        # Eğer dosya bulunamazsa, kullanıcı ve hesap veritabanları boş kalır.
        pass

# Verileri metin dosyasına yazma
def save():
    with open("user_data.txt", "w", encoding="utf-8") as file:
        for kullanici_adi, sifre in users.items():
            bakiye = accounts.get(kullanici_adi, 0)
            file.write(f"{kullanici_adi},{sifre},{bakiye}\n")


# Giriş işlemi
def giris():
    global userss
    kullanici_adi = input("Kullanıcı adınızı girin: ")
    sifre = input("Şifrenizi girin: ")
    if kullanici_adi in users and users[kullanici_adi] == sifre:
        userss = kullanici_adi
        return True
    else:
        print("Hatalı kullanıcı adı veya şifre.")
        return False


# Kayıt işlemi
def kayit():
    kullanici_adi = input("Kullanıcı adı oluşturun: ")
    if kullanici_adi in users:
        print("Bu kullanıcı adı zaten kullanılıyor. Menüye Yönlendiriliyorsunuz...")
        time.sleep(1)
    else:
        sifre = input("Şifre belirleyin: ")
        users[kullanici_adi] = sifre
        accounts[kullanici_adi] = 0
        print("Kayıt başarılı. Menüye Yönlendiriliyorsunuz...")
        time.sleep(1)

# Şifre sıfırlama işlemi
def sifre_sifirlama():
    kullanici_adi = input("Kullanıcı adınızı girin: ")
    if kullanici_adi in users:
        yeni_sifre = input("Yeni şifrenizi girin: ")
        users[kullanici_adi] = yeni_sifre
        print("Şifre başarıyla değiştirildi. Menüye Yönlendiriliyorsunuz...")
        time.sleep(1)
    else:
        print("Bu kullanıcı adı mevcut değil. Menüye Yönlendiriliyorsunuz...")
        time.sleep(1)

# Para yükleme işlemi
def para_yukle():
    global userss
    if userss in accounts:
        amount = float(input("Yatırmak istediğiniz miktarı girin: "))
        accounts[userss] += amount
        print(f"{amount} TL hesabınıza yatırıldı. Yeni bakiyeniz: {accounts[userss]} TL\n Menüye "
              f"Yönlendiriliyorsunuz...")
        time.sleep(1)
    else:
        print("Bu kullanıcı adı mevcut değil. Menüye Yönlendiriliyorsunuz...")
        time.sleep(1)

# Para çekme işlemi
def para_cek():
    global userss
    if userss in accounts:
        amount = float(input("Çekmek istediğiniz miktarı girin: "))
        if amount <= accounts[userss]:
            accounts[userss] -= amount
            print(f"{amount} TL hesabınızdan çekildi. Yeni bakiyeniz: {accounts[userss]} TL\n"
                  f" Menüye Yönlendiriliyorsunuz...")
            time.sleep(1)
        else:
            print("Yetersiz bakiye. Menüye Yönlendiriliyorsunuz...")
        time.sleep(1)
    else:
        print("Bu kullanıcı adı mevcut değil. Menüye Yönlendiriliyorsunuz...")
        time.sleep(1)

# Bakiye sorgulama işlemi
def bakiye_gor():
    global userss
    if userss in accounts:
        print(f"Hesabınızda {accounts[userss]} TL bulunmaktadır. Menüye Yönlendiriliyorsunuz...")
        time.sleep(1)
    else:
        print("Bu kullanıcı adı mevcut değil. Menüye Yönlendiriliyorsunuz...")
        time.sleep(1)

# Kullanıcı Verilerini Gösterme İşlevi
def veri_goster():
    print("\nKullanıcılar:")
    for kullanici_adi, sifre in users.items():
        print(f"Kullanıcı adı: {kullanici_adi}, Şifre: {sifre}")

    print("\nHesaplar:")
    for kullanici_adi, bakiye in accounts.items():
        print(f"Kullanıcı adı: {kullanici_adi}, Bakiye: {bakiye} TL")

# Hesabı silme işlemi
def hesap_sil():
    kullanici_adi = input("Kullanıcı adınızı girin: ")
    sifre = input("Şifrenizi girin: ")
    if kullanici_adi in users and users[kullanici_adi] == sifre:
        del users[kullanici_adi]
        del accounts[kullanici_adi]
        print("Hesap başarıyla silindi. Menüye Yönlendiriliyorsunuz...")
        time.sleep(2)
    else:
        print("Hatalı kullanıcı adı veya şifre. Menüye Yönlendiriliyorsunuz...")
        time.sleep(2)


def main():
    clear()
    veri_okuma()
    while True:
        print("\nBanka Uygulaması")
        print("1. Giriş")
        print("2. Kayıt Ol")
        print("3. Şifre Unuttum")
        print("4. Hesap Silme")
        print("5. Çıkış")
        secim = input("Yapmak istediğiniz işlemi seçin: ")
        if secim == "1":
            if giris():
                print("Giriş başarılı.")
                mains()
            else:
                print("Giriş başarısız. Menüye Yönlendiriliyorsunuz...")
                time.sleep(1)
                main()
        elif secim == "2":
            kayit()
        elif secim == "3":
            sifre_sifirlama()
        elif secim == "4":
            hesap_sil()
        elif secim == "5":
            print("Çıkış yapılıyor.")
            time.sleep(1)
            break
        elif secim == "9":
            veri_goster()
        else:
            print("Geçersiz işlem seçimi. Menüye Yönlendiriliyorsunuz...")
        time.sleep(1)
        save()

def mains():
    while True:
        clear()
        print("1. Para Yükle")
        print("2. Para Çek")
        print("3. Para Miktarı Öğrenme")
        print("4. Çıkış")
        secim2 = input("Yapmak istediğiniz işlemi seçin: ")

        if secim2 == "1":
            para_yukle()
        elif secim2 == "2":
            para_cek()
        elif secim2 == "3":
            bakiye_gor()
        elif secim2 == "4":
            print("Ana Meniye Yönlendiriliyorsunuz...")
            main()
        else:
            print("Geçersiz işlem seçimi. Menüye Yönlendiriliyorsunuz...")
            time.sleep(1)
        save()


# Programı başlat
if __name__ == "__main__":
    main()