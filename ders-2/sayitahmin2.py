import random
puan = 100
can=int(input('Oyun kaç haklı olmalıdır: '))

result=(100/can)

rasgele=random.randint(0,10)
     

hak = 1
while hak  <= can:
    tahmin=int(input(f'{hak}.tahmininizi giriniz: '))
    while True:
        if 0<=tahmin and tahmin<=10:
            if tahmin == rasgele:
                print(f'{hak}.tahmininiz doğrudur')
                break
            elif tahmin < rasgele:
                print(f'{hak}.tahmininiz yalnıştır.Tahmin ettiğiniz sayı rasgele sayıdan küçüktür')
                puan -= result
                break
            else:
                print(f'{hak}.tahmininiz yalnıştır.Tahmin ettiğiniz sayı rasgele sayıdan büyüktür')
                puan -= result
                break
        else:
            tahmin=int(input(f'{hak}.tahminiz 0-10 arasında olmalıdır.Lütfen tekrar tahminizi giriniz: '))
    if tahmin == rasgele:
        break
    hak += 1

            
print(f'Oyun bitmiştir.Oyun puanınız: {puan}.')