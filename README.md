İşte doğrudan GitHub'daki README.md dosyana kopyalayıp yapıştırabileceğin, bir yazılım mühendisinin portfolyosuna yakışacak kadar profesyonel ve teknik bir dille yeniden düzenlenmiş proje özeti:

🤖 Otonom AI Test Otomasyonu: Spotify QA Botu
Bu proje, tamamen yerel donanım üzerinde çalışan büyük dil modelleri (LLM) ve yapay zeka ajanları kullanılarak, insan müdahalesi olmadan web tabanlı yazılım testleri (QA) oluşturmak ve otomatize etmek amacıyla geliştirilmiştir.

Proje kapsamında, Spotify web uygulamasının giriş yapma ve çalma listesi oluşturma süreçleri hedeflenmiş; yapay zeka tarafından önce manuel test senaryoları tasarlanmış, ardından bu senaryolar Selenium WebDriver kullanılarak çalıştırılabilir Python otomasyon kodlarına dönüştürülmüştür.

🛠️ Kullanılan Teknolojiler ve Araçlar
Yapay Zeka Motoru: Ollama (Llama 3.2 Modeli - Tamamen çevrimdışı ve yerel çalışır)

Otonom Ajan Çatısı: CrewAI

Otomasyon Aracı: Selenium WebDriver

Programlama Dili: Python

🚀 Projenin Gelişim Aşamaları ve Mimari
1. Altyapı ve Performans Optimizasyonu (Pivot)
Proje başlangıçta izole bir Linux (Kali) sanal makinesi üzerinde planlanmış, ancak 8 GB RAM sınırı nedeniyle sistemin OOM (Out of Memory) hatası vermesi üzerine mimari değiştirilmiştir. Sanallaştırma katmanı aradan çıkarılarak "Bare Metal" (doğrudan ana Windows işletim sistemi) kurulumuna geçilmiş ve donanımın tam gücünden faydalanılmıştır.

2. Otonom Ajanın (SDET) İnşa Edilmesi
Sıradan bir sohbet botu yerine, CrewAI kütüphanesi kullanılarak hedefe yönelik otonom bir ajan (Agent) yaratılmıştır. Ajana "Kıdemli Test Otomasyon Mühendisi (SDET)" kimliği verilerek; sınır (boundary), pozitif ve negatif test durumlarını kapsayan acımasız test senaryoları üretmesi sağlanmıştır.

3. Otomatik Kod Üretimi (LLM to Code)
Ajanın planladığı manuel test senaryoları, yeni bir sistem komutuyla (prompt engineering) doğrudan Python Selenium betiklerine dönüştürülmüştür. Yazılan kodlarda statik bekleme (time.sleep()) yerine dinamik algoritmalar (WebDriverWait ve ExpectedConditions) kullanılarak kurumsal standartlarda bir otomasyon elde edilmiştir.

4. Saha Testi ve "Hayalet Tarayıcı"
Yapay zekanın ürettiği otomasyon kodu (spotify_test.py) yerel makinede çalıştırılmış, botun kendi kendine Google Chrome'u açarak Spotify adresine gitmesi, giriş yapması ve çalma listesi oluşturma tıklamalarını %100 otonom bir şekilde başarıyla gerçekleştirmesi sağlanmıştır.

🎯 Projenin Kazanımları
Hiçbir dış API'ye (OpenAI vb.) veya internet bağlantısına bağımlı kalmadan tamamen offline ve sıfır maliyetle kurumsal düzeyde AI test altyapısı kuruldu.

LLM (Büyük Dil Modeli) halüsinasyonlarını engellemek için prompt optimizasyonları ve "Cold Start" kriz yönetimi başarıyla uygulandı.

Manuel QA süreçlerinin ve tekrarlayan test döngülerinin yapay zeka ajanları ile nasıl %100 otomatize edilebileceği kanıtlandı.

Nasıl Çalıştırılır?

Bu depoyu bilgisayarınıza klonlayın.

Gerekli kütüphaneleri kurun: pip install selenium crewai

Tarayıcı otomasyonunu izlemek için: python spotify_test.py

Ajanı yeniden görevlendirmek için: python operasyon.py (Bilgisayarınızda Ollama ve Llama 3.2 kurulu olmalıdır).
