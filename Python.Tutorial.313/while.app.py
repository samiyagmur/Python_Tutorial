sayilar = [1,3,5,7,9,12,19,21]

#1.sayilar listesini while ile ekrana yazınız.#
# i=0
# while i<len(sayilar):

#     print(sayilar[i])

#     i += 1

#2.başlangıç ve bitiş değerlerini kulanıcıdan alıp araki tüm tek sayıları tekrar yazınız.

# sayilar[0]=int(input('ilk sayıyı giriniz: '))
# sayilar[-1]=int(input('son sayıyı giriniz: '))

# i=0
# while i<len(sayilar):

#     print(sayilar[i])
#     i += 1
#3.1-100 arasındaki sayıları azalan şekilde yazdırın

# i=100

# while i>0 :
#     print(i)
#     i -= 1

#4.kullanıcıdan alacağınız 5 sayıyı ekrana sıralı bir şekilde yadırırn

# lst=[]
# i=1
# while i<=5:

#     a=int(input(f'{i}.sayıyı giriniz:'))
#     lst.append(a)
    
#     i += 1
# lst.sort()
# print(lst)

#Kullanıcıdan alacağınız sınırsız ürün bilgisini urunler listesi içine saklayın

lst=[]
adet=int(input('ürün miktarını giriniz'))
i=0
while i < adet :

    name=input('ürün ismi')
    price=input('ürün fiyatı')
    lst.append({

    'name':name,'price':price

    })

    i += 1

for urun in lst:

    print(f'Ürün adı:{urun["name"]} ürün fiyatı:{urun["price"]}')




