# def sayHello():
#     print('Hello')

# sayHello()

# def sayHello(name='user'):
#     print('Hello'+name)

# sayHello('sami')
# sayHello()#bu şekilde olduğu zaman fonksiyona bir parametre göndermediğimiz için fonksiyon çalışmayacaktır.
# #onun yerine fonksiyon için name='user' gibi bir ifade kullanarak
# #boş bilgi gittiğinde fonksiyon user ifadesini yazdıracaktır.
# #Hello sami
# Hello user
# def sayHello(name='user'):
#     return 'Hello'+name

# msg=sayHello('sami')#sami bilgisi name bilgisine gelir ve return komutu ile hello sami geri dönr fonkisyonun olduğu yere yazar
# print(msg)#Hellosami

# def total(num1,num2):

#     return num1+num2

# result=total(int(input('1.sayı')),int(input('2.sayı')))
# print(result)

def yasHesapla(dogumYili):
    return 2019-dogumYili

# agenamis = yasHesapla(1992)
# agegulis = yasHesapla(1967)
# ageozge = yasHesapla(1997)
# print(agegulis,agenamis,ageozge)

def EmekliligeKacYilKaldi(dogumYili,isim):
    '''dogum yiliniza gore emekliliginize kac yil
    kaldi 
    input:doğum yili 
    output:kalan emeklilik bilgisi
    '''
    
    yas = yasHesapla(dogumYili)
    emeklilik = 65-yas

    if emeklilik>0:
        print(f'{isim}  emekliliğinize {emeklilik} yıl kaldı')
    else:    
        print(f'{isim}  emekli oldun.')
EmekliligeKacYilKaldi(1943,'Ali')

#print(help(EmekliligeKacYilKaldi))#bu fonksiyon içindeki fonksiytonla ilgili bilgiyi yazdırır.
# do­um y²l²n²za g÷re emeklili­inize ka y²l
#     kald²
#     input:do­um y²l²
#     output:kalan emeklilik bilgisi