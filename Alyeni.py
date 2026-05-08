from crewai import Agent, Task, Crew, Process

# Asıl zekayı kullanmaya devam ediyoruz
hedef_model = "ollama/llama3.2"

# 1. Ajanın Kimliği Değişiyor: Artık o bir "Otomasyon Kodlayıcısı"
otomasyon_ajani = Agent(
    role='Kıdemli Test Otomasyon Mühendisi (SDET)',
    goal='Yazılı test senaryolarını çalıştırılabilir Python Selenium otomasyon kodlarına dönüştürmek.',
    backstory='Sen kod yazmayı seven siber bir test otomasyon uzmanısın. Görevin, manuel testleri alır ve Selenium WebDriver kullanarak web tarayıcısını (Chrome/Firefox) kendi kendine yönetecek, tıklamalar yapacak kusursuz Python betikleri yazmaktır.',
    verbose=True,
    allow_delegation=False,
    llm=hedef_model
)

# 2. Yeni Görev: Selenium Kodu Yazmak
kod_yazma_gorevi = Task(
    description='Spotify web uygulamasında "Yeni bir çalma listesi oluşturma" adımı için Python ve Selenium kütüphanesini kullanarak otomatik test kodu yaz. Kodun içinde tarayıcıyı açma, login olma, çalma listesi butonunu bulma ve tıklama adımları olsun. Kodu detaylı yorum satırlarıyla açıkla.',
    expected_output='A clean, well-commented executable Python Selenium code block.',
    agent=otomasyon_ajani
)

# 3. Ekibi Topla ve Ateşle
operasyon_ekibi = Crew(
    agents=[otomasyon_ajani],
    tasks=[kod_yazma_gorevi],
    verbose=True,
    process=Process.sequential
)

print("[*] Yeni Operasyon: Ajan, Spotify için Selenium kodu yazıyor...\n")
rapor = operasyon_ekibi.kickoff()

print("\n##################################################")
print("SELENIUM OTOMASYON KODU (İSTİHBARAT RAPORU):")
print("##################################################\n")
print(rapor)