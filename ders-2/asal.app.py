
while True:
    sayi = int(input('sayi: '))
    if sayi == 1:
        print('1 sayısı asal değildir')

    for i in range(2,sayi-1):
        
        if sayi%i==0:
            print(f'{sayi} asal değildir.{i}"e bölünür.')
            break
        else:
            print(f'{sayi} asaldır.')
            
       

