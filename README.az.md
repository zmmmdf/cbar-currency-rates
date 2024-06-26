# CBAR Currency Rates

### Məqsəd

cbar-currency-rates, Azərbaycan Respublikası Mərkəzi Bankının (CBAR) XML faylından valyuta mübadilə məzənnələrini asanlıqla əldə etmək məqsədi ilə yaradılıb. Bu, proqramçıların tətbiqlərinə güncəl valyuta məzənnələrini daxil etmələrini və maliyyə hesablamaları və analizlərini asanlaşdırmağını təmin edir.

### Quraşdırma

cbar-currency-rates'i pip vasitəsi ilə quraşdıra bilərsiniz:

```bash
pip install cbar-currency-rates
```

### İstifadə

```python
from cbar_currency_rates import rates

# CBARRates obyektini yaratmaq
cbar = rates.CBARRates()

# Valyuta məzənnələrini əldə etmək
rates = cbar.get_rates()

# Valyuta məzənnələrini çap etmək
for code, value in rates.items():
    print(code, "-", value)
```

### Testlər

cbar-currency-rates geniş test qapsamı ilə etibarlılığı və dəqiqliyi təmin etmək üçün testlər daxil edir. Testləri işləmək üçün pytest istifadə edə bilərsiniz:

```bash
pip install pytest
pytest
```

### Əməkdaşlıq Təlimatları

cbar-currency-ratesə əməkdaşlıqlar dəstəklənir və təşvik olunur! Əməkdaşlıq etmək üçün, zəhmət olmasa, aşağıdakı təlimatları izləyin:

1. Depozitariyanı forklayın.
2. Öz xüsusiyyətiniz üçün yeni bir şöbə yaradın (`git checkout -b feature/my-feature`).
3. Dəyişikliklərinizi əlavə edin (`git commit -am 'Bir xüsusiyyət əlavə etdim'`).
4. Dəyişikliklərinizi şöbənizə göndərin (`git push origin feature/my-feature`).
5. Dəyişiklikləriniz barədə aydın izahatlarla bir pull istəyi göndərin.