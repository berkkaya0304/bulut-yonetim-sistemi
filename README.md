# Huawei Cloud Yönetim Paneli

Bu proje, Huawei Cloud kaynaklarını Terraform kullanarak yönetmek için Streamlit tabanlı bir web arayüzü sunar.

## Özellikler

- VPC yönetimi (oluşturma, listeleme, silme)
- ECS instance yönetimi (oluşturma, listeleme, silme)
- Güvenlik grubu yönetimi (oluşturma, listeleme, silme)
- Terraform durum görüntüleme

## Kurulum

1. Gerekli Python paketlerini yükleyin:
```bash
pip install -r requirements.txt
```

2. Huawei Cloud kimlik bilgilerinizi ayarlayın:
- `access_key` ve `secret_key` değerlerini Huawei Cloud konsolundan alın
- Bu değerleri Terraform değişkenleri olarak ayarlayın

3. Uygulamayı başlatın:
```bash
streamlit run app.py
```

## Kullanım

1. Web tarayıcınızda `http://localhost:8501` adresine gidin
2. Sol menüden yapmak istediğiniz işlemi seçin
3. İlgili form alanlarını doldurun
4. İşlemi gerçekleştirmek için butona tıklayın

## Güvenlik Notları

- Huawei Cloud kimlik bilgilerinizi güvenli bir şekilde saklayın
- Hassas bilgileri asla kaynak koduna eklemeyin
- Terraform state dosyasını güvenli bir şekilde yönetin

## Gereksinimler

- Python 3.7+
- Terraform 0.12+
- Huawei Cloud hesabı ve kimlik bilgileri 