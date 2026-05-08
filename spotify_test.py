# Gerekli Kütüphaneler
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Tarayıcıyı Başlatma
def setup_webdriver():
    driver = webdriver.Chrome()
    return driver

# Spotify'a Giriş ve Tıklama Fonksiyonu
def create_playlist(driver):
    url = "https://www.spotify.com"
    driver.get(url)

    # Login butonunu bekle ve tıkla
    element_to_click = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@class='c-Button__text']"))
    )
    element_to_click.click()

    # Kullanıcı adı ve şifre kutularını bul
    username_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='email']"))
    )
    password_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@name='password']"))
    )
    
    # ---------------------------------------------------------
    # DİKKAT: AŞAĞIDAKİ İKİ SATIRA KENDİ BİLGİLERİNİ YAZABİLİRSİN
    username_element.send_keys("kendi_mailin@gmail.com")
    password_element.send_keys("kendi_sifren")
    # ---------------------------------------------------------

    # Onay butonuna bas
    submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//form[@id='login-form']/button[@class='c-Button__text c-Button__text--primary']"))
    )
    submit_button.click()

    # Çalma listesi oluştur butonunu bekle ve tıkla
    playlist_link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[@data-control-name='Playlist creation']"))
    )
    create_playlist_button = driver.find_element(By.XPATH, "(//button)[last()]")
    create_playlist_button.click()
    
    # Kapanmadan önce olan biteni izlemen için 5 saniye bekletiyoruz
    time.sleep(5)

# Ana Çalıştırma Bloğu
def main():
    driver = setup_webdriver()
    try:
        create_playlist(driver)
    finally:
        driver.quit() # İşlem bitince tarayıcıyı kapat

if __name__ == "__main__":
    main()