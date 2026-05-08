from crewai import Agent, Task, Crew, Process

# Asıl zekayı kullanmaya devam ediyoruz
hedef_model = "ollama/llama3.2"

# 1. Ajan (Tamamen İngilizce ve Kod Odaklı)
otomasyon_ajani = Agent(
    role='Senior Python SDET',
    goal='Write executable Python Selenium WebDriver code for web automation.',
    backstory='You are a master Python test automation engineer. You write clean, well-commented Selenium code.',
    verbose=True,
    allow_delegation=False,
    llm=hedef_model
)

# 2. Görev (Sadece Selenium Kodu İsteniyor)
kod_yazma_gorevi = Task(
    description='Write a complete Python script using Selenium WebDriver to automate logging into a music web player (like Spotify) and clicking the "Create Playlist" button. Include standard imports, webdriver setup (Chrome), and comments. Return ONLY the Python code.',
    expected_output='A fully functional Python Selenium script.',
    agent=otomasyon_ajani
)

# 3. Ekibi Topla ve Ateşle
operasyon_ekibi = Crew(
    agents=[otomasyon_ajani],
    tasks=[kod_yazma_gorevi],
    verbose=True,
    process=Process.sequential
)

print("[*] Yeni Operasyon: Ajan, Selenium otomasyon kodunu yazıyor...\n")
rapor = operasyon_ekibi.kickoff()

print("\n##################################################")
print("SELENIUM OTOMASYON KODU:")
print("##################################################\n")
print(rapor)