# Dizipal Güncel Link Bulucu

Bu Python script'i, "Dizipal" ile ilgili aktif siteleri belirlemek amacıyla özel meta etiketlerini ve başlıkta belirli anahtar kelimeleri arayarak "Dizipal" web sitesinin değişen adreslerini tespit etmek için geliştirilmiştir. Script, etkili işleme için eşzamanlı yürütme kullanır.

## Gereksinimler

Script'i çalıştırmadan önce gerekli kütüphanelerin yüklü olduğundan emin olun:

```bash
pip install requests beautifulsoup4
```

## Kullanım

1. Depoyu yerel makinenize klonlayın:

   ```bash
   git clone https://github.com/sametcn99/dizipal-guncel-link.git
   ```

2. Script dizinine gidin:

   ```bash
   cd dizipal-guncel-link
   ```

3. Script dosyasını (`script.py`) açın ve şu sabitleri ayarlayın:

   - `MAX_RETRIES`: Bir web sayfasını almak için maksimum yeniden deneme sayısı.
   - `CHUNKS`: Site URL'lerini paralel işleme için bölmek için kullanılan chunk sayısı.
   - `TIMEOUT`: HTTP istekleri için zaman aşımı değeri.
   - `START_RANGE` ve `END_RANGE`: Kontrol edilecek web sitesi endeks aralığı.
   - `HEADERS`: İstekler için HTTP başlıkları.
   - `ALLOW_REDIRECTS`: Güncel linke yönlendirmeye ayarlanmış eski link kontrolü.

4. Script'i çalıştırın:

   ```bash
   python script.py
   ```

## Kişiselleştirme

- `main` fonksiyonundaki `meta_tag_names` listesini "Dizipal" sitelerini tanımlamak için ilgili meta etiketlerini içerecek şekilde düzenleyin.
- `check_site` fonksiyonundaki anahtar kelimeleri, aktif bir siteyi gösteren başlık anahtar kelimeleriyle eşleştirmek için ayarlayın.

## Not

- Bu script, "Dizipal"ın değişen adreslerini bulmak için tasarlanmış olup, belirli site yapıları veya gereksinimlere bağlı olarak değişikliklere ihtiyaç duyabilir.
- Web sitelerinden veri çekerken yasal ve etik kurallara uyun ve erişilen web sitelerinin hizmet koşullarına uygun hareket edin.

Script'i keşfedin ve ihtiyaçlarınıza uyacak şekilde adapte edin!
