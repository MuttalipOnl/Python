import webbrowser
from datetime import datetime
import speech_recognition as sr
import time
from gtts import gTTS
from playsound import playsound
import random
import os
import requests

# Recognizer nesnesi oluştur
rec = sr.Recognizer()

# Uyandırma kelimesi
uyandir = "hey siri"

durum = 1


def kayit(soru=False):
    global durum
    with sr.Microphone() as source:
        if soru:
            konusma("Ne aramak istiyorsun")
        # Mikrofonu başlatmadan önce bir saniye bekleyin
        # rec.adjust_for_ambient_noise(source, duration=1)
        # print("Ses kaydediliyor...")
        # İlk cümleyi dinle ve ses verisine dönüştür
        audio = rec.listen(source)
        try:
            # Google Web Speech API kullanarak konuşmayı tanı
            voice = rec.recognize_google(audio, language="tr-TR")
            print(voice)
            return voice
        except sr.UnknownValueError:  # Sesisni Algılanmadığı Durum
            durum = 0
            konusma("Seni Anlayamadım Tekrar Söyler Misin")
            durum = 1
        except sr.RequestError as e:  # Sistemin Çalışmadığı Durum
            konusma(f"Ses Tanıma servisine istek gönderilemedi; {e}")


def get_weather():
    # Hava durumu API'sinden veri al
    api_key = "YOUR_API_KEY"
    city = "İstanbul"  # Kullanıcıya sorarak veya algoritma ile belirlenebilir
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    weather_data = response.json()
    # Hava durumu bilgisini döndür
    if response.status_code == 200:
        weather_description = weather_data['weather'][0]['description']
        temperature = weather_data['main']['temp']
        konusma(f"{city} şehrinde hava {weather_description}, sıcaklık: {temperature}°C")
    else:
        konusma("Hava durumu bilgisi alınamadı.")


def cevap(voice):
    global durum
    if durum == 1:
        if "nasılsın" in voice or "ne haber" in voice:
            konusma("İyim Sen Nasılsın")
        elif "müzik çal" in voice:
            import random
            konusma("Açıyorum")
            music_list = ["https://www.youtube.com/watch?v=dQw4w9WgXcQ",  # Örnek şarkı linkleri
                          "https://www.youtube.com/watch?v=bmFaaLLF56c",
                          "https://www.youtube.com/watch?v=Oa-R0LvqTpE",
                          "https://www.youtube.com/watch?v=CKThDnCf2C8",
                          "https://www.youtube.com/watch?v=dY-F8BY8UkQ",
                          "https://www.youtube.com/watch?v=NS6z1QTTnds",
                          "https://www.youtube.com/watch?v=pI9rRex40Lk",
                          "https://www.youtube.com/watch?v=wGiqpSxw1BE"]
            selected_music = random.choice(music_list)
            webbrowser.open(selected_music)
        elif "saat kaç" in voice or "saati söyle" in voice:
            konusma(datetime.now().strftime("%H:%M:%S"))
        elif "arama yap" in voice:
            ara = kayit(soru=True)
            if ara:
                url = "https://google.com/search?q=" + ara
                webbrowser.get().open(url)
                konusma(ara + " için bulduklarım")
            else:
                konusma("Arama işlemi başarısız oldu.")
        elif "hava durumu" in voice:
            get_weather()
        elif "görüşürüz" in voice or "kapat" in voice or "güle güle" in voice:
            konusma("Görüşürüz Kendine İyi Bak")
            exit()


def konusma(string):
    ts = gTTS(text=string, lang="tr", slow=False)
    rand = random.randint(1, 10000)
    file = "audio" + str(rand) + ".mp3"
    ts.save(file)
    playsound(file)
    os.remove(file)


def dinle_ve_uyandir():
    while True:
        print("Uyandırma kelimesi bekleniyor...")
        voice = kayit()
        if voice and uyandir in voice.lower():
            konusma("Nasıl Yardımcı Olabilirim")
            time.sleep(1)
            while True:
                voice = kayit()
                if voice:  # Eğer voice None değilse
                    cevap(voice)
                else:
                    break  # Eğer voice None ise döngüden çık ve tekrar uyandırma kelimesi bekle


dinle_ve_uyandir()
