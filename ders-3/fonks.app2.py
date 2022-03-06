# #2-kendine gönderlilen sınırsız sayıdaki parametreyi bir listeyle sıralayın
# def listeCevir(*params):#* işaretei sınırsız sayıda parametre girilebileceğini gösteriri

#     liste=[]

#     for param in params:
#         liste.append(param)

#     return liste

# result=listeCevir(10,20,30,'sami')
# print(result)
# 3- gönderlilen 2 sayının arasındaki tüm asal sayıları bulun

# def asal(sayi1,sayi2):
#     for sayi in range(sayi1,sayi2):
#         if sayi>1:
#             for i in range(2,sayi):
#                 if(sayi%i==0):
#                     lstnotasal.append(sayi)
#                     break
#             else:
#                 lstasal.append(sayi)
                       


# lstasal=[]
# lstnotasal=[]

# sayi1=input('1.sayiyi giriniz: ')
# sayi2=input('2.sayiyi giriniz: ')

# asal(int(sayi1),int(sayi2))

# print(lstasal)
# print(lstnotasal)
#4-kendisine gönderilen bir sayının tam böleni bir liste şeklinde döndürünüz.

def tambol(sayi):
    sayac=1
    while sayac<sayi:
        if sayi%sayac==0:
            lst.append(sayac)
        sayac += 1
    else:
        lst.append(sayi)
    return lst

lst=[]

tam=int(input('Bir sayı giriniz: '))

tambol(tam)


print(lst)
