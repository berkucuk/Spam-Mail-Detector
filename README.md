

# Spam Email Classifier

## Proje Amacı

Bu proje, gelen e-postaların spam olup olmadığını tespit etmek için bir yapay zeka modelini kullanmaktadır. Bert dil modeli tabanlı bir derin öğrenme ağı kullanarak e-postaları sınıflandırır. Kullanıcıdan aldığı bir e-posta metnini analiz eder ve bu metnin **"Spam"** veya **"Not Spam"** olup olmadığını tahmin eder.

## Özellikler
- **Veri İşleme**: Metin verileri temizlenir, durak kelimeler (stopwords) ve noktalama işaretleri kaldırılır. Lemmatizasyon ile kelimelerin kök halleri elde edilir.
- **BERT Modeli Kullanımı**: BERT dil modeli kullanılarak metinlerin anlamlı vektör temsilcileri çıkarılır ve sınıflandırma yapılır.
- **Çapraz Doğrulama**: Modelin doğruluğunu test etmek için veri seti eğitim, doğrulama ve test bölümlerine ayrılır.
- **Sonuçların Görselleştirilmesi**: Modelin sonuçları bir karışıklık matrisi ile görselleştirilir.

## Proje İçeriği

- `model.pth`: Eğitilmiş modelin ağırlıkları.
- `train_model`: Modeli eğitmek için kullanılan kod.
- `test_model`: Modeli test etmek ve performansını ölçmek için kullanılan kod.
- `predict`: Kullanıcıdan alınan e-posta metnini analiz ederek sınıflandırma yapan fonksiyon.
- `confusion_matrix`: Test sonuçlarını görselleştiren karışıklık matrisi.

## Kurulum

Bu projeyi çalıştırmak için aşağıdaki adımları takip edin:

1. **Gereksinimleri Yükleyin:**

   Aşağıdaki komutları kullanarak gerekli Python kütüphanelerini yükleyin:

   ```bash
   pip install torch torchvision transformers scikit-learn matplotlib pandas numpy
   ```

2. **Veri Seti ve Modelin Yüklenmesi:**

   Projede kullanılan veri setini `kaggle` üzerinden indirip kullanabilirsiniz:

   ```bash
   kaggle datasets download -d devildyno/email-spam-or-not-classification
   unzip email-spam-or-not-classification.zip
   ```

3. **Modelin Eğitilmesi (Opsiyonel):**

   Eğer modelinizi sıfırdan eğitmek isterseniz, `train_model` fonksiyonunu kullanarak veri setinizle modeli eğitin. Eğitilen model `model.pth` dosyasında saklanacaktır.

4. **Modeli Yükleyin ve Tahmin Yapın:**

   Projeyi çalıştırmak ve terminalden tahmin yapmak için:

   ```bash
   python3 predict.py
   ```

   Terminalde size bir e-posta mesajı sorulacaktır. Girilen mesaj model tarafından analiz edilecek ve sonuç olarak "Spam" veya "Not Spam" yazdırılacaktır.

## Kullanım

1. **Eğitim**:
   
   Eğer modeli eğitmek isterseniz, veriyi indirdikten sonra `train_model` fonksiyonunu çalıştırarak eğitimi başlatabilirsiniz. Model 4 epoch boyunca eğitim görür ve ağırlıklar `model.pth` dosyasına kaydedilir.

2. **Tahmin Yapma**:
   
   Eğitilmiş modeli kullanarak herhangi bir e-posta mesajını sınıflandırabilirsiniz. Projeyi çalıştırdığınızda terminalde şu komut satırını göreceksiniz:

   ```
   Enter the message to classify: 
   ```

   Buraya herhangi bir e-posta metni girip Enter'a bastığınızda model, metni analiz edip "Spam" ya da "Not Spam" sonucunu döndürecektir.

## Örnek Kullanım

```bash
Enter the message to classify: You have won a $1000 gift card! Click here to claim your prize.
The message is: Spam
```

```bash
Enter the message to classify: Meeting is scheduled for 10 AM tomorrow. Please be on time.
The message is: Not Spam
```

## Modelin Performansı

Modelin doğruluğu, test verisi üzerinde ölçülerek bir karışıklık matrisi ile görselleştirilmiştir. Performans sonuçları ise %90 üzerinde doğruluk ile başarılı bir şekilde sınıflandırma yapmaktadır.

## Lisans

Bu proje [MIT Lisansı](https://opensource.org/licenses/MIT) ile lisanslanmıştır.

---

Bu `README.md` dosyasını projenizin GitHub deposuna ekleyerek kullanıcıların projeyi nasıl kullanabileceklerini ve nasıl çalıştığını anlatabilirsiniz.
