#1-1-100 arasında rasgele üretilecek bir sayıyı aşşağıdaki ifadeler ile bulmaya çalışalım
#random modülü kullan

import random
puan = 0
soru = 1
can=int(input('Oyun kaç haklı olmalıdır: '))
while soru<=5:
    

    rasgele=random.randint(0,100)
     
    
    print(f'{soru}.soru için')
    hak = 1
    while hak  <= can:
        tahmin=int(input(f'{hak}.tahmininizi giriniz: '))
        while True:
            if 0<=tahmin and tahmin<=100:
                if tahmin == rasgele:
                    print(f'{hak}.tahmininiz doğrudur')
                    puan += 20
                    break
                elif tahmin < rasgele:
                    print(f'{hak}.tahmininiz yalnıştır.Tahmin ettiğiniz sayı rasgele sayıdan küçüktür')
                    break
                else:
                    print(f'{hak}.tahmininiz yalnıştır.Tahmin ettiğiniz sayı rasgele sayıdan büyüktür')
                    break
            else:
                tahmin=int(input(f'{hak}.tahminiz 0-100 arasında olmalıdır.Lütfen tekrar tahminizi giriniz: '))
        if tahmin == rasgele:
            break
        hak += 1
    soru += 1
            
print(f'Oyun bitmiştir.Oyun puanınız: {puan}.')

        
