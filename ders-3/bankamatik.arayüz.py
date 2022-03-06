
User =[{'samiyagmur':{
    'ad':'sami yagmur',
    'sifre':3859,
    'hesapNo':68597865,
    'bakiye':7200,
    'ekHesap':1500
}},
{'nazmiyeöniz':
{
    'ad':'nazmiye öniz',
    'sifre':2879,
    'hesapNo':68597865,
    'bakiye':4800,
    'ekHesap':3700
}}]
def kullanicigirisi():
    global ad
    global sifre
    ad=(input('Lütfen kullanıcı adınızı giriniz: '))
    sifre=int((input('Lütfen sifrenizi giriniz: ')))
    return ad,sifre
               
            
def paratransfer():
    global ad1
    global sifre1
    global bakiye1
    global ekbakiye1
    global hesapno1
    
    ad1=ad
    sifre1=sifre
    bakiye1=bakiye
    ekbakiye1=ekbakiye
    hesapno1=hesapno          

def tekrarislem(baskaislem):
    while True:
        if baskaislem=='evet':
            global islem
            islem=int(input('yapmak istediğiniz işlem numarasını tuşlayınız: '))
            return islem            
                        
        elif baskaislem=='hayir' :
            break
        else:
            while (baskaislem != 'hayir') and (baskaislem != 'evet'):                        
                baskaislem=input('Hatalı giriş.Başka işlem yapmak istermisisniz: ')
                continue

def paracekme(bakiye,ekbakiye) :
    global islem
    global newbakiye
    global yeniekbakiye
    print(f'Hesabınızdaki toplam bakiyeniz= {bakiye} tl')

    tutar =(int(input('Çekmek istediğiniz tutarı giriniz: ')))
    while True:
        if tutar>bakiye:
            print('Bakiyeniz yetersiz ek hesap kontrol ediliyor.Lütfen bekleyiniz.')
            hesap2=(input(f'Hesap bakiyeniz: {bakiye} ek hesap bakiyeniz:{ekbakiye} toplam çekebileceğiniz tutar:{bakiye+ekbakiye} .Ek hesap kullanmak istermisiniz: '))
            
            if hesap2=='evet':
                if tutar > (bakiye+ekbakiye):
                    while tutar > (bakiye+ekbakiye):
                        tutar =(int(input('Ek hesapta dahil toplam bakiyeniz yetersiz.Lütfen çekmek istediğiniz tutarı miktarını tekrar giriniz.: ')))
                    continue
                else:
                    kalanmiktar = bakiye-tutar
                
                    yeniekbakiye = ekbakiye + kalanmiktar
                    
                    print(f'ek hesabınızda kalan bakiyeni: {yeniekbakiye} tl')
                    
                    baskaislem=(input('Başka bir işlem yapmak istiyormusunuz '))
                    return tekrarislem(baskaislem)
                    
            elif hesap2=='hayir':
                baskaislem=(input('Başka bir işlem yapmak istiyormusunuz '))
                return tekrarislem(baskaislem)
                 
            else:
                while hesap2!='hayir' and hesap2!='evet':
                    hesap2=(input(f'Hatalı giriş.Ek hesap kullanmak istermisiniz: '))
                continue        
        elif tutar <= bakiye and 0<=tutar:
            newbakiye = bakiye-tutar            
            
            print(f'hesabınızda kalan bakiyeni: {newbakiye} tl')                
            baskaislem=(input('Başka bir işlem yapmak istiyormusunuz: '))
            return tekrarislem(baskaislem)           
            
        else:
            tutar =(int(input('Çekmek istediğini bakiye sıfırdan küçük olamaz.lütfen çekmek istediğiniz tutarı tekrar giriniz')))    
    
def parayatirma(bakiye) :
    global islem
    global newbakiye
    newbakiye=bakiye
    print(f'Hesabınızdaki toplam bakiyeniz= {newbakiye} tl')
    tutar =(int(input('yatırmak istediğiniz tutarı giriniz: ')))
    
    while True:
        if 0 >= tutar:
           tutar =(int(input('Yatırmak istediğini tutar sıfırdan küçük olamaz.lütfen yatırmak istediğiniz tutarı tekrar giriniz'))) 
            
        else:
            
            newbakiye += tutar           
            print(f'Hesabınızda yeni bakiyeni: {newbakiye} tl')                
            baskaislem=(input('Başka bir işlem yapmak istiyormusunuz: '))
            return tekrarislem(baskaislem),newbakiye 

newbakiye=0        
yeniekbakiye=0

kullanicigirisi()

for i in User:    
    for a,b in i.items():
        if a == ad:                       
            if b['sifre'] == sifre:
                bakiye = b['bakiye']
                ekbakiye = b['ekHesap']
                hesapno = b['hesapNo']
                
                print(f'Hoşgeldiniz')
                print(f'Para çekmek için: 1')
                print(f'Para yatırmak için: 2')
                print(f'Havale için: 3')
                print(f'Fatura yatırmak için: 4')
                print(f'hesap işlemleri için: 5')

                islem=int(input('Tuşlayınız: '))
                if islem<0 or islem>=5:
                    continue                
                    

                break       
else:
    print('Yalnış kullanıcı girişi yaptınız lürfen tekrar deneyiniz')
    kullanicigirisi()

while 0<islem and islem<=5:   
    if islem==1:
        msg=paracekme(bakiye,ekbakiye)
        bakiye=newbakiye
        ekbakiye=yeniekbakiye
        if msg == (None,bakiye) or (None,ekbakiye):
            print('Bankamızı tercih ettiğiniz için teşekkür ederiz.İyi günler dileriz.')
            break
    elif islem==2:
        msg=parayatirma(bakiye)
        bakiye=newbakiye                      
        if msg == (None,bakiye):           
            print('Bankamızı tercih ettiğiniz için teşekkür ederiz.İyi günler dileriz.')
            break    
    
    else:
        continue
    


###1. bir süre sonra tıkanıyor.
###admin girişi yapılacak.

     




            

        






